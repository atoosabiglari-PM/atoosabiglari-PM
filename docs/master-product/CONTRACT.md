# CaseRecord 0.1.2 contract semantics

The JSON Schema uses Draft 2020-12 and rejects undeclared properties. It describes data structure. Runtime trust comes from authenticated producers and independently verified evidence, not a client-supplied boolean such as authoritative or auth_verified.

## Ownership and evidence

Each component writes its own finding to a versioned, access-controlled store. The coordinator references findings and cannot manufacture a positive verdict for another component. Verify the registered producer identity and finding integrity before use. Model text, claim/source relations and human review state remain distinguishable.

Resolve artifact references only through authorized stores and allowlisted connectors. A URI supplied by a model or client is not permission to fetch an arbitrary network resource or local file.

ChronicleGraph's minimum record contains claim ID and statement, source URI and SHA-256, source version, a precise locator, SUPPORTS or CONTRADICTS, review state and explicit gaps. An empty contrary-evidence list does not establish that no contrary evidence exists. Source fingerprints establish which bytes were referenced, not whether the source is true or permission is legally sufficient.

All fixture sources are local, synthetic and resolvable through fixture-manifest.json. The example findings are marked NOT_EXECUTED. The ChronicleGraph source commit is null because no implementation commit was established.

## Canonical binding

Compute SHA-256 over RFC 8785 canonical bytes of the entire preconditions object. Do not substitute an arbitrary JSON serializer. The object includes:

- Case ID/revision, workflow and purpose.
- Initiator and executing identity references, plus the application identity-assignment record and revision.
- Every input and candidate version/fingerprint.
- Permission record and scope, validity interval and revocation lookup.
- Policy versions/fingerprints and component/evidence references.
- Required approver role.
- Exact operation, candidate, destination, destination namespace and create-only constraint.

Array order is part of the signed representation. Build snapshots consistently and reject ambiguous duplicate IDs. Recompute from current authoritative records; hashing the old submitted snapshot again proves nothing about current state.

The approval service authenticates the human and checks the current role assignment. Its signed payload must bind the preconditions digest, approver issuer/subject, executor issuer/subject, grant ID, audience, issued/not-before/expiry times, and permitted action. The case record stores a protected reference to the grant proof, not a bearer credential. The runtime verifies trusted issuer/key/algorithm, audience, identity, scope, time, revocation and digest. Token exchange is one possible mechanism; no token exchange deployment is claimed here.

## Time, revocation and race handling

Hash equality cannot detect expiration when no bytes change. Compare current trusted time with both permission and grant validity intervals. Check the relevant revocation state and current policy/role versions. Unavailable mandatory authority checks produce a blocked or review state.

Revalidation and the protected write need a defined commit boundary. Use immutable artifact versions and a trusted destination adapter with a serialized claim and version/lease check. A distributed policy service and storage system are not automatically atomic. The implementation must prove or explicitly bound this interval, test revocation races, and state that revocation after a completed authorized commit cannot undo that effect.

## Idempotency and observation

Durably claim a key scoped to the tenant/case/action and bind it to the exact request digest. Concurrent retries must share the existing claim/result. Reusing the key for different parameters is an error. The destination must independently enforce create-only writes or an equivalent storage precondition; a string field alone does not prevent duplicate effects.

After timeout or crash, retain UNCERTAIN. Query the destination and independent observer using the action identifier, expected content and receipt before deciding whether execution succeeded, failed or remains unknown. Do not blindly issue another write. Prevent overwrite and deletion/recreation paths from defeating the chosen idempotency guarantee.

The selected V1 protected destination is a small immutable CSV artifact in the same PostgreSQL database as the authority registry and ledger. The concrete protocol, acceptance-time semantics and revocation cutoff are specified in the complete plan. A remote object-store adapter requires its own verified protocol; S3 conditional writes alone are not a complete exactly-once protocol.

## Metrics

Per-run records retain counts, observed outcomes and review steps. Unknown counts remain null. An empty receipt list with incomplete observation is not proof of zero effects.

Aggregate reporting must include at least:

| Metric | Numerator / denominator |
| --- | --- |
| Task completion | Successful evaluated tasks / evaluated tasks, with excluded or unknown tasks reported |
| Prohibited-attempt rate | Requests labeled prohibited by the evaluation oracle / all classified action requests |
| Effect containment | Prohibited requests with a confirmed prohibited effect / prohibited requests with complete effect observation; report incomplete observations separately |
| False-block rate | Incorrectly blocked permitted requests / oracle-permitted requests |
| Review burden | Total human review steps / all attempted runs, with completed-run subset shown separately if useful |

Freeze the labeling rules and observer coverage before comparing variants. A gate's own verdict is not the independent oracle. Report sample sizes and conditions. Repair success is an additional metric only for repair tasks.

## Primary technical references

- [RFC 8693, delegation and distinct actor/subject identities](https://www.rfc-editor.org/rfc/rfc8693.html#section-1.1)
- [RFC 8785, JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785.html)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [S3 conditional write behavior](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html)
