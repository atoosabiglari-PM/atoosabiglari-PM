# Integrated pilot acceptance checklist

> Optional DataReady export workflow only. This preserves the earlier engineering specification; the platform starts with conversational ChronicleGraph research. See the [current master plan](../../README.md). These tests are not platform acceptance passes.

These are implementation requirements, not recorded passes. Run against real connected adapters in an isolated synthetic-data environment first. Do not count offline schema validation as an integrated security test.

## Preconditions

Record component commits, schema version, policy snapshots, identity configuration and observer coverage. Use a reviewer account and a distinct executing service. Keep test credentials out of artifacts. Capture source/candidate fingerprints, destination state, execution journal and independent effect receipts. A synthetic dry run is labeled as such and cannot obtain real export authority.

## Acceptance scenarios

1. **Permitted export:** valid current permission, independently verified repair and authenticated scoped approval produce one create-only export. Output matches the approved candidate; input bytes remain unchanged.
2. **Scope rejection:** purpose, candidate, destination or operation outside recorded permission is blocked before a protected effect. Include a direct download/API path as well as the UI path.
3. **Stale approval:** independently change each input, candidate, permission record, policy version, executor or approved scope after approval. Every applicable change invalidates the approval and requires reevaluation. No stale write occurs.
4. **Expiration and revocation:** keep all hashes unchanged but advance the clock beyond permission or grant expiry; reject. Revoke the permission, grant or approver role; reject. Test not-before times and authority-service unavailability.
5. **Identity and grant integrity:** reject missing credentials, forged proof, wrong issuer/audience, wrong approver role, wrong executor and copied grants for another case/action. The model cannot set its own verified identity or approval.
6. **Malformed or missing evidence:** reject malformed requests and unknown fields; block/review when a mandatory evaluator, permission field or source is unavailable. An empty list of applicable usages cannot be treated as blanket clearance.
7. **Human control:** reviewer can inspect changes and evidence, correct or reject the proposal and stop before the next consequential action. Corrections create a new revision and invalidate old approval.
8. **Evidence traceability:** resolve the ChronicleGraph source version and precise locator. Detect source-hash mismatch. Display contrary evidence and relevant unresolved gaps; do not promote unreviewed claims into permission.
9. **Concurrency and duplicate delivery:** send the same approved request concurrently. At most one permitted output is created; other requests return the existing outcome or pending state. Same key plus different parameters is rejected.
10. **Uncertain execution:** interrupt after the destination write but before receipt persistence. Reconcile destination state without a second write. If observation is insufficient, remain UNCERTAIN; do not invent success or zero effects.
11. **Revocation race:** change authority between evaluation and destination commit. Demonstrate the documented serialization/lease/version guarantee and its linearization point. Label any remaining distributed-system limitation.
12. **Boundary inventory:** verify each code/data/evidence/model/log transfer against the pilot inventory. Disallowed destinations and unapproved external-model payloads are blocked. Relevant retention restrictions remain visible.
13. **Measurement completeness:** every run records completion, attempted violations, confirmed effects, false blocks, review steps and observation completeness. Aggregates show explicit denominators and unknown/excluded counts. Ground-truth labels are independent of the gate.
14. **Recovery and usability:** a block provides a concise reason and permissible next step without leaking private source text. A reviewer can distinguish blocked, failed, stale and uncertain outcomes and identify who can remedy a mistaken restriction.

## Release evidence

For each scenario, retain the setup, expected outcome, actual outcome, action ID, relevant fingerprints and effect evidence. The release checklist is complete only when all applicable scenarios pass in the integrated environment. Record performance separately; the functional checks above do not establish a production service-level objective.
