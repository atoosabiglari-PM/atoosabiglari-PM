# Master Product Complete Plan

Version 1.1 • November 15, 2026 • Owner: Atoosa Biglari

**One complete implementation plan.** Product decisions, the selected runtime protocol, change bindings, the actual synthetic-artifact inventory, all acceptance scenarios, current evidence and the full research scope are collected here. This is the operative baseline; technical tests are part of implementation. Design choices are distinguished from verified runtime behavior.

## Product and first pilot

Build one governed AI workspace spanning RightsReady, DataReady Autopilot, ChronicleGraph, DecisionReady, SafetyGate and Gemma Research. The product connects evidence and permissions to a specific human-authorized action, then records what actually happened. All six remain in the product scope.

The first integrated pilot is **Workflow A: governed data change and export**. A data or AI operations lead reviews a proposed repair to a dataset, inspects the supporting evidence, and approves a specific export. The system preserves the source, blocks unauthorized or stale requests, and records successful, failed and uncertain outcomes separately.

This plan consolidates Atoosa's direction and the Gemini/Grok reviews. The initial buyer and willingness to pay remain hypotheses to test. Gemini's workflow comparison is adopted as the starting recommendation; its sample JSON is developed here into a structural schema and synthetic example, not treated as existing executable enforcement.

Apollo would see this same master product, its verified pilot and its roadmap. An application draws from this work. The product's implementation is not conditional on admission, and this plan does not establish Apollo eligibility or acceptance.

## Why this workflow comes first

| Candidate | Reuse and gaps | Decision |
| --- | --- | --- |
| A. Governed data change/export | DataReady has supported repairs, source fingerprints and separate export. RightsReady needs a dataset-purpose adapter; identity and export enforcement still need integration. | V1 pilot |
| B. Evidence-backed research | Strong match for ChronicleGraph, but a larger portion of the core implementation and adjudication remains unbuilt. | Subsequent workflow |
| C. Governed coding/repository change | SafetyGate and Gemma provide useful foundations. Repository state, permissions and execution recovery require another adapter set. | Subsequent workflow |

Provisional workflow RICE: Reach = one pilot; Impact = 1–3; Confidence = 0–1; Effort = relative points. A: 1 × 3 × 0.8 / 3 = **0.80**. B: 1 × 2 × 0.5 / 5 = **0.20**. C: 1 × 3 × 0.6 / 5 = **0.36**. These are sequencing estimates, not customer research or delivery promises.

## Scope of the pilot

- Start with synthetic CSV fixtures and a controlled export destination. Use only supported repairs: whitespace trimming, exact duplicate removal and missing-marker normalization when permitted.
- Preserve original bytes. Perform candidate trials in isolated staging; require the consequential export to pass the authorization boundary.
- Begin integration tests with fixed repair proposals. After the control path is working, connect DataReady's existing model proposal path using permitted minimized evidence. A model proposes; it does not grant permission.
- Keep components in their existing repositories. Add narrow adapters and a shared case record; do not merge licenses or rewrite all six systems.
- Use ChronicleGraph's minimal evidence record in the pilot. Gemma Research contributes the evaluation template; the existing experiment does not supply a mandatory runtime Gemma agent or a trained authorization model.

## Responsibilities of the six components

| Component | Pilot responsibility | Required new work |
| --- | --- | --- |
| RightsReady | Evaluate the recorded permission for the specific purpose and destination | Dataset-purpose/recipient/retention mapping; incomplete relevant permissions cannot silently pass |
| DataReady | Audit, propose supported repairs, independently check candidates, preserve the input | Adapter to the case record; route every export path through the enforced boundary |
| ChronicleGraph | Record claims with a versioned source fingerprint, precise locator and support/contradiction relation | Minimal writer/reader and source-access checks; no universal truth score |
| DecisionReady | Present changes, unresolved requirements and the human decision | Durable case mapping and verified human identity; existing project-baseline promotion is not an export receipt |
| SafetyGate | Verify current authority and enforce the exact export action | Bind the configured identity provider, delegation, action grant and destination adapter |
| Gemma Research | Keep utility, attempts and confirmed effects separate | Pilot-specific measurement harness; retain the original study's scope and limitations |

The existing-interface and boundary inventory is included below, with inspected commits and concrete reuse points.

## Must-have rules

1. Authenticate the approver and executor separately. Link them through a verifiable, scoped grant. Before consequential execution, the runtime checks approver authority, executing identity, intended audience, exact action and current permission.
2. Bind the case/revision, purpose, inputs, candidate, permission record, policy versions, finding/evidence versions, executor and destination using a defined canonicalization format.
3. A changed artifact, permission, policy, identity assignment or approved scope invalidates the applicable approval. Expiration additionally requires a current-time check; a hash does not change when time passes.
4. Check revocation/current authority at execution. Prevent a check-to-write race using immutable versions and an enforceable authorization/commit protocol. Document the point after which revocation cannot retract an already committed write.
5. Persist execution claims. A repeated idempotency key with changed parameters is rejected. An uncertain outcome is reconciled against the destination before a retry.
6. Maintain a P0 inventory of code, data, evidence, model payloads and logs crossing boundaries, their recipients, purposes and permission basis.
7. Record outcomes and counts per run. Aggregate rates carry explicit denominators; incomplete observation is not zero effects. Use repair success only for repair tasks.

Structural validation does not authenticate a principal, validate a signature, resolve a permission, establish truth or perform an export. The runtime protocol, contract semantics and complete acceptance checklist are included in this page.

## Priorities and delivery sequence

**MoSCoW:** Must: the seven rules above and all acceptance scenarios for the supported pilot. Should: better evidence navigation, reviewer usability and customer feedback. Could: additional providers and workflow adapters. Won't in V1: universal prompt/tool control, automatic training on approval logs, unrestricted transformations or claims of production certification.

**2×2, value versus effort:** start with high-value/lower-effort contracts, fixtures and interface mapping; then fund high-value/higher-effort identity and execution integration. Time-box cosmetic changes. Broader tuning and universal orchestration have uncertain value before the pilot evidence exists.

| Order | Work package | Exit evidence | Current status |
| --- | --- | --- | --- |
| 1 | Final plan, initial interface audit, structural contract, synthetic evidence example and acceptance specification | Reviewed package; offline fixture and negative checks | Prepared and checked in this package |
| 2 | Dataset-permission and DataReady adapters; minimal ChronicleGraph writer/reader | Real component outputs mapped to the contract; source bytes preserved; incomplete rights handled | Next engineering step |
| 3 | Durable DecisionReady review plus authenticated approval/delegation | Verified approver and executor; exact signed grant; forged/wrong-identity tests rejected | Required before consequential pilot export |
| 4 | SafetyGate export adapter and durable recovery | Conditional create, replay protection, stale/revoked/expired rejection, crash reconciliation | Pending |
| 5 | Integrated evaluation and human walkthrough | Every acceptance scenario passes; measurements and limitations retained | Pending |
| 6 | Pilot packaging and customer validation | Reproducible demo, clear user benefit, actual feedback and prioritized gaps | Pending |

Work packages may span multiple study/build sessions. Execution is governed by the exit evidence below rather than an untested calendar promise. The assistant owns engineering preparation and evidence collection. Atoosa owns product/customer priorities and evaluates whether the experience is useful and understandable.

Initial work-item RICE, using the same units: interface/permission mapping 1 × 3 × 0.8 / 2 = **1.20**; baseline/evidence fixture harness 1 × 3 × 0.8 / 3 = **0.80**; integrated adapters 1 × 3 × 0.6 / 5 = **0.36**. Mandatory identity and permission controls cannot be omitted because of a score.

## Definition of done

One supported workflow runs from input through evidence review and human approval to a controlled export. The evaluator independently observes the effects, the original stays unchanged, every specified rejection/recovery case passes, and the reported metrics can be reproduced. Every runtime result names actual component commits, policy versions and the tested environment.

The existing Gemma result remains a separate 96-episode study: injected-context attempts 16/24 in both arms; prohibited effects 16/24 OFF and 0/24 ON; fixed-test repairs 7/24 in both arms. It is not the pilot's score.

## Research remains in scope

Retain ChronicleGraph's broader source-lineage and training-preparation research; authority across delegation and queued work; retained prohibited operations in passing code; valid-credential abuse; false restrictions and appeals; unseen tasks, additional models and adaptive attacks. Controlled post-training is a later experiment with independent gate OFF/ON comparisons, not a current product capability. These tracks belong to this product and are sequenced by evidence and prerequisites.

## Concrete pilot runtime design

These are implementation decisions in this plan. They are not claims that the deployment already satisfies them.

### Identity and delegation

Use Google OpenID Connect for human sign-in and a separately authenticated workload identity for the export service. Keep the configured issuer/audience allowlists explicit and key application identities by issuer plus subject, not a display name or email. The actual client IDs, audiences, workload subject and signing-key resource must be bound to the deployed application and verified by the acceptance tests; no values are fabricated here.

Use a signed action grant issued by our approval service rather than require token exchange as an additional V1 dependency. The service verifies the human's current application role, then signs the exact case/precondition digest, approver, executor, action, destination, audience, grant ID and validity interval. Use the existing KMS integration as the implementation starting point, with a separate test signer for isolated tests. A model cannot mint a verified principal or set an approval flag.

The runtime verifies the workload credential and grant independently. A forged signature, changed payload, wrong audience, wrong executor, expired credential, revoked grant or outdated application-role assignment must fail before the protected write. A deployment with test identities is labeled as a test; it is not a verified production identity setup.

Google's authentication documentation describes validation of ID tokens and the required application configuration: [OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect). Our scoped grant is a separate application authorization decision.

### Exact change-invalidation surface

| Change | Binding in CaseRecord 0.1.2 | Execution requirement |
| --- | --- | --- |
| Input or candidate bytes/version | preconditions.inputs and preconditions.candidate | Resolve immutable version and recompute/check content fingerprint |
| Permission or use restrictions | preconditions.permission.record plus revision and recorded scope | Compare the current registry revision, purpose, recipient and validity interval |
| Policy | preconditions.policies records and versions | Compare current applicable policy versions under the authority lock |
| Application identity assignment | preconditions.identity_assignment record and revision | Check current issuer/subject-to-role assignment and executor eligibility |
| Approved scope, action or destination | preconditions.action and purpose | Exact match to the signed grant; no implicit destination substitution |
| Passage of time or revocation | Current trusted time and authority registry | Explicit validity/revocation check even when all hashes match |

All six checks are mandatory. The last is deliberately not implemented as hash equality. Changes create a new case revision and require a new approval.

### Protected export and revocation ordering

For V1, store small synthetic CSV exports as immutable artifact rows in the same PostgreSQL database as the authority registry and execution ledger. Set an explicit pilot limit of 2 MiB per candidate. This confines the first consequential effect and its authorization ordering to one transactional system. Remote object-store delivery remains a separate adapter and cannot inherit the local guarantee automatically.

The protected operation is publication of one exact candidate into the controlled export store. Downloading its bytes is a separate access-controlled operation.

1. Before opening the transaction, verify credential/grant signatures, resolve authorized references, prepare the immutable candidate and compute its digest. Perform no external model/network request while holding the authority lock.
2. Begin a bounded database transaction. Lock the application's authority/epoch row and the relevant case/grant rows in a fixed order. All application permission, policy, role and revocation updates must use this same ordering and increment the authority revision.
3. Read current authority and check the full binding, active role/grant state and trusted database time. Record decision_at. Expiry is evaluated when this locked operation is accepted, rather than asserted for every subsequent byte of delivery.
4. Claim a unique tenant/case/action idempotency key with the exact request digest. A changed request using the same key is rejected. A completed identical request returns its existing receipt.
5. Insert the immutable export artifact and successful execution receipt in this same transaction, with database uniqueness preventing another output for the action. Commit them together.
6. If the transaction aborts, neither artifact nor success receipt is published. If the response is lost, look up the committed action before retrying. If the database cannot establish its state, retain UNCERTAIN and perform no new write.

**Revocation cutoff:** a revocation that commits before the locked authorization decision blocks the export. Once an export has been accepted under the authority lock, a concurrent revocation waits; it governs subsequent operations, not that already accepted transaction. The artifact becomes visible only if the transaction commits. Record both decision_at and committed_at. A later revocation cannot retract bytes already delivered.

Application-role and permission changes covered by this guarantee are changes recorded in the authoritative registry. Unknown upstream account or contractual changes cannot be detected automatically; provider refresh/notification and permission-update paths must feed that registry. Do not claim instant global revocation.

New downloads recheck current access before starting the response. The API must expose when a stop request arrived after an operation had already been accepted. Direct database writes, bypass downloads and ungoverned destination credentials are excluded through deployment permissions and tested.

**Race tests:** use barriers to force revocation-before-decision, export-accepted-before-revocation, two concurrent identical exports, same key/different digest, abort-before-commit and lost-response-after-commit. Expected results are explicit: zero outputs for the first/aborted cases; one authorized output for accepted/concurrent-repeat cases; no blind retry on unknown state. Test expiry at the authorization decision boundary.

PostgreSQL provides the underlying [row-locking](https://www.postgresql.org/docs/current/explicit-locking.html) and [transaction](https://www.postgresql.org/docs/current/tutorial-transactions.html) primitives. The application protocol above still requires integration tests.

### ChronicleGraph minimal implementation

Implement two narrow operations: write_evidence_record and read_evidence_record. Accept only the documented claim/source fields, preserve versions, and return the same recorded locator/relation on a round trip. Resolve fixture sources through fixture-manifest.json; reject unknown references, traversal paths, arbitrary network URLs and fingerprint mismatches. A real deployment uses an authorized artifact resolver with the same controls.

The fixture's JSON Pointer identifies the listed allowed purpose; it does not prove real consent. Source access and source truth are separate questions. The full research graph is not required for this interface.

### Rule to executable-test mapping

| Mandatory rule | Acceptance cases in this page | Test boundary |
| --- | --- | --- |
| Verified approver/executor and scoped grant | 1, 5, 7 | Approval service, identity verifier and export gateway |
| Exact, versioned case binding | 2, 3, 6, 8 | Snapshot builder, evidence resolver and authorization check |
| Change, expiry and revocation invalidation | 3, 4, 11 | Live authority registry and locked authorization decision |
| Check-to-write ordering | 9, 10, 11 | Actual PostgreSQL transaction and protected artifact store |
| Idempotency and uncertain outcomes | 9, 10 | Durable ledger, uniqueness constraints and recovery lookup |
| License/data-boundary inventory | 6, 8, 12 | Real adapter transfers and endpoint access controls |
| Independent measurement | 13, 14 | Test oracle, destination observer and reviewer walkthrough |

These tests exercise the existing DataReady repair path plus adapters. They do not require merging all repositories. They are engineering gates in this single plan, not a separate strategic-review stage.


## Complete contract semantics


The JSON Schema uses Draft 2020-12 and rejects undeclared properties. It describes data structure. Runtime trust comes from authenticated producers and independently verified evidence, not a client-supplied boolean such as authoritative or auth_verified.

### Ownership and evidence

Each component writes its own finding to a versioned, access-controlled store. The coordinator references findings and cannot manufacture a positive verdict for another component. Verify the registered producer identity and finding integrity before use. Model text, claim/source relations and human review state remain distinguishable.

Resolve artifact references only through authorized stores and allowlisted connectors. A URI supplied by a model or client is not permission to fetch an arbitrary network resource or local file.

ChronicleGraph's minimum record contains claim ID and statement, source URI and SHA-256, source version, a precise locator, SUPPORTS or CONTRADICTS, review state and explicit gaps. An empty contrary-evidence list does not establish that no contrary evidence exists. Source fingerprints establish which bytes were referenced, not whether the source is true or permission is legally sufficient.

All fixture sources are local, synthetic and resolvable through fixture-manifest.json. The example findings are marked NOT_EXECUTED. The ChronicleGraph source commit is null because no implementation commit was established.

### Canonical binding

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

### Time, revocation and race handling

Hash equality cannot detect expiration when no bytes change. Compare current trusted time with both permission and grant validity intervals. Check the relevant revocation state and current policy/role versions. Unavailable mandatory authority checks produce a blocked or review state.

Revalidation and the protected write need a defined commit boundary. Use immutable artifact versions and a trusted destination adapter with a serialized claim and version/lease check. A distributed policy service and storage system are not automatically atomic. The implementation must prove or explicitly bound this interval, test revocation races, and state that revocation after a completed authorized commit cannot undo that effect.

### Idempotency and observation

Durably claim a key scoped to the tenant/case/action and bind it to the exact request digest. Concurrent retries must share the existing claim/result. Reusing the key for different parameters is an error. The destination must independently enforce create-only writes or an equivalent storage precondition; a string field alone does not prevent duplicate effects.

After timeout or crash, retain UNCERTAIN. Query the destination and independent observer using the action identifier, expected content and receipt before deciding whether execution succeeded, failed or remains unknown. Do not blindly issue another write. Prevent overwrite and deletion/recreation paths from defeating the chosen idempotency guarantee.

The selected V1 protected destination is a small immutable CSV artifact in the same PostgreSQL database as the authority registry and ledger. The concrete protocol, acceptance-time semantics and revocation cutoff are specified in the complete plan. A remote object-store adapter requires its own verified protocol; S3 conditional writes alone are not a complete exactly-once protocol.

### Metrics

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

### Primary technical references

- [RFC 8693, delegation and distinct actor/subject identities](https://www.rfc-editor.org/rfc/rfc8693.html#section-1.1)
- [RFC 8785, JSON Canonicalization Scheme](https://www.rfc-editor.org/rfc/rfc8785.html)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [S3 conditional write behavior](https://docs.aws.amazon.com/AmazonS3/latest/userguide/conditional-writes.html)

## Concrete artifact inventory for the synthetic pilot

| Artifact | Source and recipient | Purpose | Permission and access boundary |
| --- | --- | --- | --- |
| fixtures/input.csv | Local fixture store to DataReady adapter | Audit and constrained candidate preparation | Synthetic data authored for this package; read-only original |
| fixtures/candidate.csv | Isolated staging to checker, reviewer and export gate | Compare exact candidate and authorize its publication | Synthetic output; no direct bypass download |
| fixtures/permission.json | Fixture store to RightsReady adapter and reviewer | Demonstrate purpose/destination/expiry interpretation | Synthetic permission, explicitly not real-world consent |
| fixtures/policy.json | Policy registry to checker and gate | Bind supported transformations and export restrictions | Version/fingerprint required; external model payload disabled |
| fixtures/identity-assignment.json | Test authority registry to grant service and gate | Bind issuer/subject-to-role assignment | Synthetic identities; no production credential or authority |
| Four component finding fixtures | Test producers to coordinator | Exercise shared references and domain separation | Marked NOT_EXECUTED; cannot be used as real positive findings |
| examples/chronicle-evidence.json | Evidence writer to reader/reviewer | Resolve source version and JSON Pointer | Source restricted to authorized fixture manifest |
| Approval/grant proof | Approval service to protected proof store and gate | Link human approval to executor and exact action | No actual grant in the example; never publish bearer credentials |
| Export CSV and receipt | Gate to controlled database store and observer | Commit one protected output and its outcome | Implementation artifact; access controlled; not yet generated |
| Runtime logs/metrics | Runtime to operator/evaluator | Separate attempts, effects and utility | Minimized identifiers/counts; no raw secrets; implementation pending |

The code/dependency and model-service boundaries are covered in the complete inventory below. A real dataset needs its own recorded terms and recipients; synthetic fixture permission is never reused as that authorization.

## Existing interfaces and complete boundary inventory


Read-only source inspection on November 15, 2026. This is an initial interface map, not a complete security audit or a live deployment verification.

### Inspected versions and integration gaps

| Component | Inspected commit | Concrete reuse point | Pilot gap |
| --- | --- | --- | --- |
| DataReady | b77ece50b2a79a24ab093b3f5a53d0e39cd64cc3 | app/services/authorization.py: authorize_repair_plan; app/services/executor.py: prepare_execution_context and execute_repair_plan; app/services/lineage.py | Map existing policy/repair objects to the case contract; bind export to the authenticated grant and ensure all export routes pass the gate |
| RightsReady | a8d9e2d6c2d494b9d958d8347d13c28fb46c0c0c | src/clearance_engine.py: ClearanceEngine.evaluate; src/rightsready_pipeline.py: RightsReadyPipeline.process | Existing inputs are production/assets/licenses/asset_usage. Define explicit dataset-purpose/recipient/retention semantics; never infer general dataset consent from media clearance |
| DecisionReady | 4a1e4d0d373df9d5342e479738e0ebb37b7e676f | src/decisionready/decision_lifecycle.py: apply_human_decision; src/decisionready/baseline.py: promote_approved_change | Map tabular changes to review requirements, add durable shared case state and verified approver identity, preserve distinction between approval and execution result |
| SafetyGate | f80f64f70316f47df154dd70e3327c4226fd7f37 | backend/app/services/trusted_workflow.py: run_oidc_governed_workflow; core/identity/principal.py: build_verified_principal; core/authorization/execution_store.py: claim_execution_record and mark_stale_pending_uncertain | Configure the application's production identity boundary; bind human delegation, full preconditions and a real export adapter; test destination effects and recovery |
| ChronicleGraph | No implementation repository established by this inspection | Existing research specification; concrete evidence structure supplied in this package | Implement a minimal writer/reader and source authorization; do not relabel DecisionReady's graphs as ChronicleGraph |
| Gemma Research | Existing study, not re-audited in this source pass | Separate attempt/effect/task-outcome measurement discipline | Build pilot-specific observers and labels; do not report the 96-episode study as pilot execution evidence |

#### Important findings

- DataReady's execution context checks source hashes, source/output separation, approved actions and column alignment. These are useful controls, but are not proof that a new cross-component export is identity-bound.
- RightsReady intentionally permits structurally trusted records with clearance gaps to be ingested for review. Its trusted-ingestion status must not become permission for an unrelated export. Its clearance engine also needs nonempty applicable-use coverage enforced by the new adapter.
- DecisionReady checks change identity and readiness before approved baseline promotion. Its README describes a single-session prototype with persistent multi-user storage still beyond that build.
- SafetyGate's identity helper keys trusted role assignments by issuer and subject. Its execution store persists claims and marks stale pending attempts uncertain. Its README explicitly says the implemented OIDC path is not yet bound to a specific production identity provider at the application API boundary.
- No claim is made that these APIs already accept CaseRecord 0.1.2 or that all export paths are covered.

### P0 boundary inventory

Populate actual recipients, record versions and permission evidence during adapter implementation. The only demonstrated data flows in this package are local synthetic fixture reads.

| Boundary | What crosses | Intended purpose | Required evidence or restriction |
| --- | --- | --- | --- |
| User to isolated staging | Input CSV and permission/source references | Audit and permitted candidate preparation | Data owner/purpose, retention and access scope; preserve source bytes |
| Staging to RightsReady adapter | Permission metadata and applicable use/destination | Determine recorded scope | Applicable dataset terms; missing relevant conditions go to review/block |
| Staging to DataReady | Allowed tabular bytes and repair rules | Audit and constrained repair | Source-preserving trial permission; supported transformations only |
| Any component to external model | Minimized audit evidence or proposal context | Optional repair proposal | First pilot disabled; require explicit permitted recipient, purpose, retention and data minimization before enabling |
| Evidence store to ChronicleGraph/reviewer | Claims, source references and authorized excerpts | Trace and inspect evidence | Source-access and excerpt permissions; no unrestricted source download |
| DecisionReady to grant service | Exact proposal digest and authenticated human decision | Issue scoped approval | Trusted identity/role, approved action and actor, validity interval |
| Grant service to SafetyGate | Protected proof reference and immutable binding | Check current execution authority | Trusted signature, actor/audience/scope, time, revocation and live version checks |
| Export adapter to destination | Approved candidate bytes | Create the permitted output once | Exact recipient/destination and content; conditional write; durable action claim |
| Runtime to audit/evaluation | IDs, versions, outcomes and minimized effect evidence | Accountability and measurement | Retention, access control and redaction; never log bearer credentials |
| Component code to integration environment | Pinned code and dependencies | Implement the pilot | Record license/notice and provenance per version; no blanket relicensing |

### License record

The LICENSE file at each of the four inspected code commits names PolyForm Noncommercial 1.0.0. Their READMEs also preserve earlier Apache-2.0 releases. SafetyGate's README contains a legacy Apache heading as well as the later PolyForm section: reconcile this documentation inconsistency against the specific version and licensing records before packaging. The separate Gemma public study retains its own scoped release terms.

This is an inventory of observed declarations, not a conclusion that every combined commercial use is cleared. Review actual ownership, third-party material, historical grants and intended distribution for the pilot. No source license, repository visibility or private archive is changed by this plan.

### Sources

Inspected at the commits above: the four repositories' README and LICENSE files plus the named source files. Private source links remain subject to their existing access controls. The findings needed for this plan are summarized here; private source code is not reproduced.


## Complete acceptance checklist


These are implementation requirements, not recorded passes. Run against real connected adapters in an isolated synthetic-data environment first. Do not count offline schema validation as an integrated security test.

### Preconditions

Record component commits, schema version, policy snapshots, identity configuration and observer coverage. Use a reviewer account and a distinct executing service. Keep test credentials out of artifacts. Capture source/candidate fingerprints, destination state, execution journal and independent effect receipts. A synthetic dry run is labeled as such and cannot obtain real export authority.

### Acceptance scenarios

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

### Release evidence

For each scenario, retain the setup, expected outcome, actual outcome, action ID, relevant fingerprints and effect evidence. The release checklist is complete only when all applicable scenarios pass in the integrated environment. Record performance separately; the functional checks above do not establish a production service-level objective.

## Current verification evidence


Checked November 15, 2026.

### Passed

- JSON Schema Draft 2020-12 metaschema validation.
- Synthetic case structural validation with date-time and URI format checks.
- Real SHA-256 checks against all referenced synthetic fixture bytes.
- RFC 8785 precondition digest recomputation.
- ChronicleGraph source fingerprint and JSON Pointer resolution.
- Thirteen negative mutations rejected: untrusted auth_verified field, missing executor, missing identity assignment, changed identity assignment, malformed digest, changed target, changed artifact, changed policy, approval without proof fields, synthetic execution claim, negative count, case-ID mismatch and duplicate domain component.

Reproduce with the pinned validation requirements and validate_contract.py.

### Not established by these checks

Real authentication, signature validation, live permission expiry/revocation, runtime action enforcement, storage race handling, independent effect observation and an end-to-end six-component workflow. Those require the implementation tests in ACCEPTANCE.md.

The component interface audit is a read-only source inspection at the commits recorded in INTERFACE_AUDIT.md. Their full test suites and hosted services were not rerun for this planning package. The original Gemma experiment was not rerun or expanded.

## Machine-readable examples and reproducibility

The structural schema is available as [case-record.schema.json](case-record.schema.json). The examples below are complete synthetic records; null outcomes mean unobserved, not a measured absence of effects.

### ChronicleGraph example

~~~json
[
  {
    "claim_id": "claim-purpose-001",
    "statement": "The synthetic permission fixture lists internal analytics as an allowed use.",
    "source": {
      "uri": "fixture://fixtures/permission.json",
      "sha256": "72a699bbb4fda5e3d2242509ecb4e4da5d23b265d636daf4f255dcba9371af11"
    },
    "source_version": "1",
    "locator": {
      "kind": "JSON_POINTER",
      "value": "/allowed_uses/0"
    },
    "relation": "SUPPORTS",
    "review_status": "UNREVIEWED",
    "explicit_gaps": [
      "Fixture demonstrates record structure; it is not a verified real-world permission."
    ]
  }
]
~~~

### Shared case example

~~~json
{
  "contract_version": "0.1.2",
  "record_kind": "SYNTHETIC_EXAMPLE",
  "case_id": "case-synthetic-001",
  "revision": 1,
  "case_state": "AWAITING_APPROVAL",
  "created_at": "2026-11-15T00:00:00Z",
  "preconditions": {
    "case_id": "case-synthetic-001",
    "case_revision": 1,
    "workflow": "governed_tabular_repair_export",
    "purpose": "internal_analytics",
    "initiator": {
      "issuer": "https://identity.example.invalid",
      "subject": "human-requester",
      "credential_evidence_ref": "fixture://not-a-verified-credential/human-requester"
    },
    "executor": {
      "issuer": "https://identity.example.invalid",
      "subject": "export-service",
      "credential_evidence_ref": "fixture://not-a-verified-credential/export-service"
    },
    "inputs": [
      {
        "artifact_id": "input-001",
        "version": "1",
        "content": {
          "uri": "fixture://fixtures/input.csv",
          "sha256": "5da3c3bbe730869dfb1b8e1a887614f1d05236b953eccaac04a4066928813524"
        }
      }
    ],
    "candidate": {
      "artifact_id": "candidate-001",
      "version": "1",
      "content": {
        "uri": "fixture://fixtures/candidate.csv",
        "sha256": "31475a9065853e61c6117db9fa5c1b2a2dd6baf3f5374e217500deb5efcb4d8c"
      }
    },
    "permission": {
      "record": {
        "uri": "fixture://fixtures/permission.json",
        "sha256": "72a699bbb4fda5e3d2242509ecb4e4da5d23b265d636daf4f255dcba9371af11"
      },
      "revision": "1",
      "valid_from": "2026-11-15T00:00:00Z",
      "expires_at": "2026-11-16T00:00:00Z",
      "allowed_purposes": [
        "internal_analytics"
      ],
      "allowed_destinations": [
        "fixture://pilot-exports/clean.csv"
      ],
      "revocation_lookup_ref": "fixture://permission-registry/permission-001"
    },
    "policies": [
      {
        "policy_id": "pilot-export",
        "version": "1",
        "record": {
          "uri": "fixture://fixtures/policy.json",
          "sha256": "e81b3f9c6f194c51e9806e16ad3b27cf13d11d901426ded88ead705c2e3828c2"
        }
      }
    ],
    "domain_findings": [
      {
        "component": "rights_ready",
        "producer_id": "fixture-producer",
        "adapter_version": "design-0.1.1",
        "source_commit": "a8d9e2d6c2d494b9d958d8347d13c28fb46c0c0c",
        "finding": {
          "uri": "fixture://fixtures/rights_ready-finding.json",
          "sha256": "633846dee03d602a9265ccab5955b00bf46d369af2a4b2d243ccfa83c88731db"
        }
      },
      {
        "component": "data_ready",
        "producer_id": "fixture-producer",
        "adapter_version": "design-0.1.1",
        "source_commit": "b77ece50b2a79a24ab093b3f5a53d0e39cd64cc3",
        "finding": {
          "uri": "fixture://fixtures/data_ready-finding.json",
          "sha256": "65b44cf73859ae921e914e4b8689273e8ef740a1ef81d13cb5ffeda63d4552ab"
        }
      },
      {
        "component": "chronicle_graph",
        "producer_id": "fixture-producer",
        "adapter_version": "design-0.1.1",
        "source_commit": null,
        "finding": {
          "uri": "fixture://fixtures/chronicle_graph-finding.json",
          "sha256": "60f212aff5c20cd38a29ac29b1958ed7feb81493885e95b4f003616c59eb878a"
        }
      },
      {
        "component": "decision_ready",
        "producer_id": "fixture-producer",
        "adapter_version": "design-0.1.1",
        "source_commit": "4a1e4d0d373df9d5342e479738e0ebb37b7e676f",
        "finding": {
          "uri": "fixture://fixtures/decision_ready-finding.json",
          "sha256": "d2652c8260421391a218f90ccb2769f58d9c85a66806e076c1a132d00531a648"
        }
      }
    ],
    "evidence_manifest": {
      "uri": "fixture://examples/chronicle-evidence.json",
      "sha256": "aa2eb8add4f2b588df810f90a0082aabe652b15d7d4e082f27733ac40c5a0d70"
    },
    "required_approver_role": "pilot_export_approver",
    "action": {
      "action_id": "action-export-001",
      "operation": "EXPORT_VERIFIED_DATASET",
      "candidate_artifact_id": "candidate-001",
      "candidate_sha256": "31475a9065853e61c6117db9fa5c1b2a2dd6baf3f5374e217500deb5efcb4d8c",
      "target_resource": "fixture://pilot-exports/clean.csv",
      "target_namespace": "pilot-exports",
      "write_condition": "CREATE_ONLY"
    },
    "identity_assignment": {
      "record": {
        "uri": "fixture://fixtures/identity-assignment.json",
        "sha256": "22efaa632e43250622bc2f68603e21b012f4213273ba25e5449cb58ce43ab30c"
      },
      "revision": "1"
    }
  },
  "canonicalization": "RFC8785",
  "bound_preconditions_sha256": "8b7c42a54e94ffc15e11eaadf804c28ae684aaadd9ff13496ec60b1028ef9214",
  "authorization": {
    "status": "PENDING",
    "approver": null,
    "grant_id": null,
    "grant_proof_ref": null,
    "signed_payload_sha256": null,
    "approved_at": null,
    "expires_at": null
  },
  "observation": {
    "run_id": "not-run-fixture-001",
    "execution_status": "NOT_ATTEMPTED",
    "idempotency_key": "case-synthetic-001:1:action-export-001",
    "gate_decision": "NOT_INVOKED",
    "gate_reason_codes": [],
    "effect_assessment": "NOT_OBSERVED",
    "effect_receipts": [],
    "task_outcome": "NOT_EVALUATED",
    "prohibited_attempt_count": null,
    "confirmed_prohibited_effect_count": null,
    "false_block_count": null,
    "human_review_step_count": null
  }
}
~~~

### Reproduce the offline design checks

~~~bash
python3 -m pip install -r requirements-validation.txt
python3 validate_contract.py
~~~

The companion files are implementation resources, not additional planning documents that must be read to understand the decisions in this page.

The [meeting record](../master-product-meeting-2026-11-14.md) preserves the discussion history. This complete plan is the operative implementation baseline.
