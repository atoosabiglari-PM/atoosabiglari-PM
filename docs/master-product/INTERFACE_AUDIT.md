# Component interface and boundary audit — conversational platform

Source inspection and branch checks: November 15, 2026. This is a bounded code/interface audit, not a complete security audit or verification of deployed behavior. The current four branch heads match the inspected revisions. The [master plan](README.md) owns product priorities; the [historical export audit](workflows/data-export/INTERFACE_AUDIT.md) is preserved for its optional workflow.

## Inspected interfaces

| Component | Inspected commit | Concrete reuse | Current platform gap |
| --- | --- | --- | --- |
| DataReady | `b77ece50b2a79a24ab093b3f5a53d0e39cd64cc3` | `app/services/authorization.py`: `authorize_repair_plan`; `executor.py`: `prepare_execution_context`, `execute_repair_plan`; `lineage.py` | Conditional quality findings and source-preserving correction adapters; no mandatory tabular input for a question |
| RightsReady | `a8d9e2d6c2d494b9d958d8347d13c28fb46c0c0c` | `src/clearance_engine.py`: `ClearanceEngine.evaluate`; `src/rightsready_pipeline.py`: `RightsReadyPipeline.process` | Extend media production/assets/licenses/asset_usage semantics to source access, purpose, processors, recipients, retention and unknown permissions |
| DecisionReady | `4a1e4d0d373df9d5342e479738e0ebb37b7e676f` | `src/decisionready/decision_lifecycle.py`: `apply_human_decision`; `baseline.py`: approved promotion | Durable multi-user research case/finding versions, objections, independent review, role-bound approval and material-evidence invalidation |
| SafetyGate | `f80f64f70316f47df154dd70e3327c4226fd7f37` | `backend/app/core/admission/engine.py`: `evaluate_admission`; `api/agents.py`: registration/admission; `services/trusted_workflow.py`; identity helpers; execution store | Controlled behavioral evaluation and actionable reassessment, research-case adapters, LLM human-rights concerns/independent review, production identity binding and observed incident reconstruction |
| ChronicleGraph | No implemented research repository established by this audit | Actual fifty-question workbook/protocol; existing research specification; synthetic source-anchor record | Full question-to-evidence workflow, typed lineage, retrieval/citations, contradictions/unknowns, revision and challenge integration |
| Gemma Research | Prior bounded study; not rerun in this audit | Separate task/attempt/effect methodology | Research-specific oracles, new platform observations and reports; no inherited performance claim |

## Findings that affect the implementation

- DataReady validates source hashes, supported repairs, source/output separation and action/column alignment. Reuse those controls for relevant data; they do not establish a research answer’s correctness or cross-component action authority.
- RightsReady permits structurally trusted records with clearance gaps to enter review. Trusted ingestion is not onward-use permission. Require nonempty applicable-use coverage; do not accept a vacuous CLEARED result when no relevant use was checked.
- DecisionReady checks readiness/change identity before approved promotion. Its existing single-session prototype does not prove durable collaborative review or cryptographically bound reviewer identity.
- SafetyGate admission checks declared ownership, purpose, jurisdiction, tools, permission requirements and approval declarations. The inspected tests exercise those declaration checks. They do **not** run an agent to establish how it behaves. Keep admission and controlled behavioral results distinct in API and UI.
- SafetyGate registration records configuration/version hashes. Existing passport, MCP, OIDC/role, runtime authorization and execution-journal primitives are reusable. The README explicitly identifies the missing production identity-provider binding at the application API boundary. Endpoint integration still needs object-level authorization and real tests; a declaration of `owner_identity` is not verified identity.
- Its execution store claims durable actions and marks stale pending actions UNCERTAIN. Destination effects, reconciliation and cross-service incident joins must be verified per adapter, not inferred from ledger existence.
- No dedicated LLM human-rights assessment/independent appeal flow was established by this source pass. This is required new work, not an already verified module.
- None of the named existing APIs is assumed to accept the new platform case contract. Narrow authenticated adapters must preserve each component’s authority and status distinctions.

## Exact SafetyGate admission evidence

Inspected at the pinned commit: `backend/app/core/admission/engine.py`, `backend/app/api/agents.py`, `backend/app/schemas/admission.py`, `backend/tests/test_admission_engine.py` and `README.md`. The admission engine emits PASS/FAIL/NON_OVERRIDABLE_FAIL from declarations. Registration/admission endpoints store agent/version and admission status. Existing source tests were read, not executed as integrated platform tests during this documentation revision.

## Boundary inventory and owners

| Boundary | Owner | Data / purpose | Acceptance proof |
| --- | --- | --- | --- |
| Typed/voice question and optional attachments | Workspace | Preserve source and conversation; audio/transcript consent/retention | AC-01, 04, 06 |
| Selected web/Google source | Resolver + RightsReady | Authorized retrieval and versioned use terms; exact selected item and processor | AC-03, 06, 07, 17 |
| Evidence to model/OCR/transcription/search | Resolver + SafetyGate | Minimized permitted context; authorize destination/purpose before transmission | AC-06, 07, 11, 17 |
| Evidence to research/quality/rights adapters | Domain components | Separate findings and authorized access; preserve originals | AC-03, 04, 07, 08 |
| Objections and official finding review | DecisionReady | Versioned challenge, response, readiness, role-bound review and appeal | AC-05, 12, 13 |
| Developer agent to controlled runner | SafetyGate | Authorized endpoint/package; admission and observed tests; scoped credentials | AC-09, 10, 17 |
| Minimized evidence to rights model/reviewer | SafetyGate + independent reviewer | Advisory concerns, uncertainty, recourse and no grant authority | AC-13 |
| Approval/grant to live tool boundary | SafetyGate | Current actor/action/data/purpose/destination binding | AC-11, 12, 14 |
| Execution records to incident/research reports | Authorized observer/reviewer | Actual effects, gaps, recipient distinction and separate metrics | AC-15, 16, 18 |

Before enabling each live boundary, name actual processor/recipient, owner, source version, permission basis, retention and revocation path. Tests use public or synthetic material unless separately authorized. No credentials, raw private records or code from private repositories are published by this audit.

## License inventory

The LICENSE files at the four code commits name PolyForm Noncommercial 1.0.0. Their READMEs preserve earlier Apache-2.0 releases. SafetyGate’s README has a legacy Apache heading alongside the later PolyForm section; consult version-specific licensing records before packaging. The public Gemma study has its own scoped release terms; the profile repository’s documentation terms remain separate.

This records observed declarations, not blanket commercial permission or a legal conclusion about the combined product. Preserve existing notices, contributor/third-party rights and private archives. No license or repository visibility is changed. Actual corpus images, translations, interview recordings and model-processing rights require asset-level inventory even where a source webpage is accessible.

## Supporting repositories

- [DataReady, pinned source](https://github.com/atoosabiglari-PM/dataready-autopilot/tree/b77ece50b2a79a24ab093b3f5a53d0e39cd64cc3)
- [RightsReady, pinned source](https://github.com/atoosabiglari-PM/rightsready/tree/a8d9e2d6c2d494b9d958d8347d13c28fb46c0c0c)
- [DecisionReady, pinned source](https://github.com/atoosabiglari-PM/decisionready/tree/4a1e4d0d373df9d5342e479738e0ebb37b7e676f)
- [SafetyGate, pinned source](https://github.com/atoosabiglari-PM/safetygate/tree/f80f64f70316f47df154dd70e3327c4226fd7f37)

Private source links remain access-controlled. Summarizing interfaces here does not make those repositories public.
