"""Offline structural/fixture checks, not an authorization or execution service."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

import rfc8785
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent
SCHEMA = json.loads((ROOT / "case-record.schema.json").read_text())
MANIFEST = json.loads((ROOT / "fixture-manifest.json").read_text())
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())

def check(condition, message):
    if not condition:
        raise ValueError(message)

def read_ref(record):
    entry = MANIFEST[record["uri"]]
    data = (ROOT / entry["path"]).read_bytes()
    actual = hashlib.sha256(data).hexdigest()
    check(actual == entry["sha256"] == record["sha256"], "Fixture hash mismatch")
    return data

def validate_case(case):
    VALIDATOR.validate(case)
    p = case["preconditions"]
    check(case["case_id"] == p["case_id"], "Case identity mismatch")
    check(case["revision"] == p["case_revision"], "Revision mismatch")
    check(hashlib.sha256(rfc8785.dumps(p)).hexdigest() == case["bound_preconditions_sha256"], "Binding mismatch")
    check(p["action"]["candidate_artifact_id"] == p["candidate"]["artifact_id"], "Candidate identity mismatch")
    check(p["action"]["candidate_sha256"] == p["candidate"]["content"]["sha256"], "Candidate hash mismatch")
    check(p["purpose"] in p["permission"]["allowed_purposes"], "Purpose outside recorded scope")
    check(p["action"]["target_resource"] in p["permission"]["allowed_destinations"], "Destination outside recorded scope")
    findings = p["domain_findings"]
    check(len(findings) == 4 and {f["component"] for f in findings} == {
        "rights_ready", "data_ready", "chronicle_graph", "decision_ready"
    }, "Missing or duplicate domain finding")
    for artifact in p["inputs"] + [p["candidate"]]:
        read_ref(artifact["content"])
    read_ref(p["permission"]["record"])
    read_ref(p["identity_assignment"]["record"])
    for policy in p["policies"]:
        read_ref(policy["record"])
    for finding in findings:
        read_ref(finding["finding"])
    anchors = json.loads(read_ref(p["evidence_manifest"]))
    anchor_validator = Draft202012Validator(
        {"$ref": "#/$defs/anchor", "$defs": SCHEMA["$defs"]},
        format_checker=FormatChecker(),
    )
    for anchor in anchors:
        anchor_validator.validate(anchor)
        data = json.loads(read_ref(anchor["source"]))
        check(anchor["locator"]["kind"] == "JSON_POINTER", "Unsupported fixture locator")
        for token in anchor["locator"]["value"].lstrip("/").split("/"):
            token = token.replace("~1", "/").replace("~0", "~")
            data = data[int(token)] if isinstance(data, list) else data[token]
        check(data == "internal_analytics", "Fixture source location did not resolve")

def main():
    Draft202012Validator.check_schema(SCHEMA)
    case = json.loads((ROOT / "examples/case-awaiting-approval.json").read_text())
    validate_case(case)
    mutations = [
        ("untrusted auth_verified flag", lambda x: x["preconditions"]["executor"].update(auth_verified=True)),
        ("missing executor", lambda x: x["preconditions"].pop("executor")),
        ("missing identity assignment", lambda x: x["preconditions"].pop("identity_assignment")),
        ("identity assignment changed after binding", lambda x: x["preconditions"]["identity_assignment"].update(revision="2")),
        ("malformed hash", lambda x: x.update(bound_preconditions_sha256="not-a-hash")),
        ("target changed after binding", lambda x: x["preconditions"]["action"].update(target_resource="fixture://other/export.csv")),
        ("artifact changed after binding", lambda x: x["preconditions"]["inputs"][0]["content"].update(sha256="0"*64)),
        ("policy changed after binding", lambda x: x["preconditions"]["policies"][0].update(version="2")),
        ("approval missing proof", lambda x: x["authorization"].update(status="APPROVED")),
        ("synthetic record claims execution", lambda x: x["observation"].update(execution_status="SUCCEEDED")),
        ("negative observed count", lambda x: x["observation"].update(false_block_count=-1)),
        ("case mismatch", lambda x: x.update(case_id="different-case")),
        ("duplicate domain component", lambda x: x["preconditions"]["domain_findings"][0].update(component="data_ready")),
    ]
    for name, mutate in mutations:
        changed = deepcopy(case)
        mutate(changed)
        if name == "duplicate domain component":
            changed["bound_preconditions_sha256"] = hashlib.sha256(rfc8785.dumps(changed["preconditions"])).hexdigest()
        try:
            validate_case(changed)
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            print("REJECTED:", name)
        except Exception as exc:
            from jsonschema.exceptions import ValidationError
            if not isinstance(exc, ValidationError):
                raise
            print("REJECTED:", name)
        else:
            raise AssertionError("Mutation accepted: " + name)
    print("PASS: schema, synthetic fixture, hashes, evidence locator, and 13 negative cases.")
    print("NOT TESTED: real identity, grant signatures, live revocation/time, runtime gates, storage effects, or end-to-end integration.")

if __name__ == "__main__":
    main()
