# Master Product Final Plan

Version 1.0 • November 15, 2026 • Owner: Atoosa Biglari

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

The [interface audit](INTERFACE_AUDIT.md) identifies the inspected commits and concrete reuse points.

## Must-have rules

1. Authenticate the approver and executor separately. Link them through a verifiable, scoped grant. Before consequential execution, the runtime checks approver authority, executing identity, intended audience, exact action and current permission.
2. Bind the case/revision, purpose, inputs, candidate, permission record, policy versions, finding/evidence versions, executor and destination using a defined canonicalization format.
3. A changed artifact, permission, policy, identity assignment or approved scope invalidates the applicable approval. Expiration additionally requires a current-time check; a hash does not change when time passes.
4. Check revocation/current authority at execution. Prevent a check-to-write race using immutable versions and an enforceable authorization/commit protocol. Document the point after which revocation cannot retract an already committed write.
5. Persist execution claims. A repeated idempotency key with changed parameters is rejected. An uncertain outcome is reconciled against the destination before a retry.
6. Maintain a P0 inventory of code, data, evidence, model payloads and logs crossing boundaries, their recipients, purposes and permission basis.
7. Record outcomes and counts per run. Aggregate rates carry explicit denominators; incomplete observation is not zero effects. Use repair success only for repair tasks.

Structural validation does not authenticate a principal, validate a signature, resolve a permission, establish truth or perform an export. Those runtime checks are specified in [CONTRACT.md](CONTRACT.md) and [ACCEPTANCE.md](ACCEPTANCE.md).

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

Work packages may span multiple study/build sessions. Implementation estimates are to be updated after adapter discovery; this plan does not promise an untested calendar deadline. The assistant owns engineering preparation and evidence collection. Atoosa owns product/customer priorities and evaluates whether the experience is useful and understandable.

Initial work-item RICE, using the same units: interface/permission mapping 1 × 3 × 0.8 / 2 = **1.20**; baseline/evidence fixture harness 1 × 3 × 0.8 / 3 = **0.80**; integrated adapters 1 × 3 × 0.6 / 5 = **0.36**. Mandatory identity and permission controls cannot be omitted because of a score.

## Definition of done

One supported workflow runs from input through evidence review and human approval to a controlled export. The evaluator independently observes the effects, the original stays unchanged, every specified rejection/recovery case passes, and the reported metrics can be reproduced. Every runtime result names actual component commits, policy versions and the tested environment.

The existing Gemma result remains a separate 96-episode study: injected-context attempts 16/24 in both arms; prohibited effects 16/24 OFF and 0/24 ON; fixed-test repairs 7/24 in both arms. It is not the pilot's score.

## Research remains in scope

Retain ChronicleGraph's broader source-lineage and training-preparation research; authority across delegation and queued work; retained prohibited operations in passing code; valid-credential abuse; false restrictions and appeals; unseen tasks, additional models and adaptive attacks. Controlled post-training is a later experiment with independent gate OFF/ON comparisons, not a current product capability. These tracks belong to this product and are sequenced by evidence and prerequisites.

## Review and reproduce this package

- [CaseRecord JSON Schema](case-record.schema.json)
- [Synthetic case](examples/case-awaiting-approval.json) and [ChronicleGraph evidence example](examples/chronicle-evidence.json)
- [Contract semantics](CONTRACT.md)
- [Numbered acceptance checklist](ACCEPTANCE.md)
- [Interface and data-boundary audit](INTERFACE_AUDIT.md)
- [Verification record](VERIFICATION.md)

Run the offline checks from this directory:

~~~bash
python3 -m pip install -r requirements-validation.txt
python3 validate_contract.py
~~~

These checks validate the design artifacts. They do not claim a working six-component integration. The source meeting record is [here](../master-product-meeting-2026-11-14.md).
