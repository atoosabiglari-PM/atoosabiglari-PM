> Historical export-workflow audit. The [current platform audit](../../INTERFACE_AUDIT.md) governs integration priorities.

# Initial interface and data-boundary audit

Read-only source inspection on November 15, 2026. This is an initial interface map, not a complete security audit or a live deployment verification.

## Inspected versions and integration gaps

| Component | Inspected commit | Concrete reuse point | Pilot gap |
| --- | --- | --- | --- |
| DataReady | b77ece50b2a79a24ab093b3f5a53d0e39cd64cc3 | app/services/authorization.py: authorize_repair_plan; app/services/executor.py: prepare_execution_context and execute_repair_plan; app/services/lineage.py | Map existing policy/repair objects to the case contract; bind export to the authenticated grant and ensure all export routes pass the gate |
| RightsReady | a8d9e2d6c2d494b9d958d8347d13c28fb46c0c0c | src/clearance_engine.py: ClearanceEngine.evaluate; src/rightsready_pipeline.py: RightsReadyPipeline.process | Existing inputs are production/assets/licenses/asset_usage. Define explicit dataset-purpose/recipient/retention semantics; never infer general dataset consent from media clearance |
| DecisionReady | 4a1e4d0d373df9d5342e479738e0ebb37b7e676f | src/decisionready/decision_lifecycle.py: apply_human_decision; src/decisionready/baseline.py: promote_approved_change | Map tabular changes to review requirements, add durable shared case state and verified approver identity, preserve distinction between approval and execution result |
| SafetyGate | f80f64f70316f47df154dd70e3327c4226fd7f37 | backend/app/services/trusted_workflow.py: run_oidc_governed_workflow; core/identity/principal.py: build_verified_principal; core/authorization/execution_store.py: claim_execution_record and mark_stale_pending_uncertain | Configure the application's production identity boundary; bind human delegation, full preconditions and a real export adapter; test destination effects and recovery |
| ChronicleGraph | No implementation repository established by this inspection | Existing research specification; concrete evidence structure supplied in this package | Implement a minimal writer/reader and source authorization; do not relabel DecisionReady's graphs as ChronicleGraph |
| Gemma Research | Existing study, not re-audited in this source pass | Separate attempt/effect/task-outcome measurement discipline | Build pilot-specific observers and labels; do not report the 96-episode study as pilot execution evidence |

### Important findings

- DataReady's execution context checks source hashes, source/output separation, approved actions and column alignment. These are useful controls, but are not proof that a new cross-component export is identity-bound.
- RightsReady intentionally permits structurally trusted records with clearance gaps to be ingested for review. Its trusted-ingestion status must not become permission for an unrelated export. Its clearance engine also needs nonempty applicable-use coverage enforced by the new adapter.
- DecisionReady checks change identity and readiness before approved baseline promotion. Its README describes a single-session prototype with persistent multi-user storage still beyond that build.
- SafetyGate's identity helper keys trusted role assignments by issuer and subject. Its execution store persists claims and marks stale pending attempts uncertain. Its README explicitly says the implemented OIDC path is not yet bound to a specific production identity provider at the application API boundary.
- No claim is made that these APIs already accept CaseRecord 0.1.2 or that all export paths are covered.

## P0 boundary inventory

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

## License record

The LICENSE file at each of the four inspected code commits names PolyForm Noncommercial 1.0.0. Their READMEs also preserve earlier Apache-2.0 releases. SafetyGate's README contains a legacy Apache heading as well as the later PolyForm section: reconcile this documentation inconsistency against the specific version and licensing records before packaging. The separate Gemma public study retains its own scoped release terms.

This is an inventory of observed declarations, not a conclusion that every combined commercial use is cleared. Review actual ownership, third-party material, historical grants and intended distribution for the pilot. No source license, repository visibility or private archive is changed by this plan.

## Sources

Inspected at the commits above: the four repositories' README and LICENSE files plus the named source files. Private source links remain subject to their existing access controls. The findings needed for this plan are summarized here; private source code is not reproduced.

