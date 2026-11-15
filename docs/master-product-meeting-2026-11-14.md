# Master Product — Complete Meeting Minutes and Product Plan

Public review copy for Atoosa, Gemini, Grok and other readers. The meeting record is self-contained. Some underlying project sources remain private; the relevant findings and proposals are included here. Publication of these minutes does not grant access to private repositories or research archives.

**Meeting minutes and product planning record — revision 3.** Discussion: November 14, 2026, Pacific; revised November 15, 2026, UTC. Founder and decision owner: Atoosa Biglari. Gemini and Grok supplied reviews shared by Atoosa; ChatGPT synthesized the discussion and earlier checks of project materials. This revision incorporates Atoosa's clarification that all current discussion belongs to the master product, regardless of Apollo participation. Confirmed directions and proposed technical decisions are identified separately. The final planning package consolidates the subsequent Gemini/Grok refinements; it specifies Workflow A as the first integrated pilot.

**The product is the work we are doing now.** Its purpose is to help people use AI with traceable evidence, explicit permissions, understandable decisions and controlled actions. All six projects and the research discussed today belong in its present product plan. Apollo may use the resulting product story, evidence and demonstration; it does not determine the scope of this meeting or make product development conditional on admission. A complete plan can support both the product and an Apollo application. The combined system has not yet been verified end to end.

# Meeting objective and result

Objective: define how RightsReady, DataReady Autopilot, ChronicleGraph, DecisionReady, SafetyGate and Gemma Research work together as one coherent product, what each contributes, what remains unbuilt, and what decisions and evidence are needed to deliver it.

Result: a six-project product definition, proposed integration contract and user journey, research workstreams, evaluation criteria, priorities and an action register. The complete discussion is retained here. Delivery is staged by technical dependencies and demonstrated value. Preparing these minutes does not mean the proposed integrations or experiments have already been implemented.

# Confirmed directions and discussion contributions

- **Confirmed by Atoosa:** include all six projects; complete the master-product planning now; retain the larger impact and research ambitions; continue this work whether or not we participate in Apollo. Apollo can benefit from this work without becoming its organizing objective.

- The umbrella vision can serve individuals and teams through different supported AI workflows. Accepting broad prompts does not mean every prompt uses every component or that every external system is controlled.

- Human understanding, accountable authority and intervention remain central requirements. Existing research evidence, project identities, licenses and private archives remain distinct.

- Today's reviews are brainstorming inputs. They do not establish that suggested capabilities are implemented or approved.

| Contributor | Contribution retained | Qualification |
| --- | --- | --- |
| Atoosa | One umbrella, six projects, human agency, and a broader mission pursued now | First customer, final name and individual implementation choices remain to be selected |
| Grok | Shared evidence records, a small coordinating layer, component authority boundaries, and separate attempt/effect/repair measurements | ChronicleGraph is distinct from DecisionReady's graphs; production identity must be bound before consequential execution |
| Gemini | Scoped approvals, revocation and change detection, structured action proposals, recovery metrics and future model experiments | Post-training, internal alignment and sovereign deployment are proposed extensions, not demonstrated study results |
| ChatGPT synthesis | Connect evidence to a specific authorized action and recheck changed prerequisites | The product specification must distinguish existing components, measured research and proposed integration |

# Six projects and their present roles

| Project | Role in the proposed master product | Current evidence boundary |
| --- | --- | --- |
| RightsReady | Evaluate recorded permissions for the intended use | Existing media-oriented license, date, territory and usage checks; broader consent and training rights are extensions |
| DataReady Autopilot | Audit tabular inputs and verify constrained repairs under human control | Existing audit, repair proposal, independent check, approval and export workflow; not a universal secret-removal or compliance certificate |
| ChronicleGraph or Larry Page Project | Link claims, source anchors, transmission histories, disagreement and gaps | Research specification; distinct from DecisionReady's operational graphs |
| DecisionReady | Present change impacts, requirements, evidence and a human decision | Existing single-session change-readiness prototype; durable multi-user integration remains work |
| SafetyGate | Enforce exact-action authorization at supported execution boundaries | Existing independent authorization code, MCP integration and audit mechanisms; production identity binding and new integrations need verification |
| Gemma authorization study | Research and evaluation of attempts, effects and task outcomes | Completed separate prototype experiment; neither SafetyGate deployment nor an authorization-trained model |

Gemma's injected-context results were attempts 16/24 in both arms, confirmed prohibited effects 16/24 OFF versus 0/24 ON, and fixed-test repairs 7/24 in both arms. This supports bounded observed containment. It does not establish improved internal model alignment, general utility equivalence, safe deployment of generated code or protection by the full suite.

# Product definition and candidate first workflow

**Working description:** A governed AI workspace for turning a request into an evidence-backed proposal, an accountable decision and a permitted action. RightsReady contributes use permissions; DataReady contributes data checks and constrained repairs; ChronicleGraph contributes claim and source relationships; DecisionReady contributes change review; SafetyGate contributes enforcement; Gemma Research contributes evaluation. A coordinating layer connects their records and interfaces without replacing their separate responsibilities.

**Initial customer hypothesis:** a data or AI operations team preparing a dataset for downstream use. A proposed buyer is its data or AI operations lead. The concrete problem is reviewing an AI-assisted change and controlling its export while preserving the original and the supporting evidence. This is a starting hypothesis, not an adopted limit on customers or workflows. Compare it with evidence-backed research and governed coding/change workflows using actual customer pain, available capabilities and evaluation feasibility. Demand, willingness to pay and revenue remain unvalidated.

**Business model hypothesis:** a paid team workspace or design-partner pilot, with bounded usage. Do not invent prices, customer commitments, revenue or market-validation claims.

**Selected first pilot in the final delivery plan:** take one supported tabular dataset through permission review, audit, constrained repair, evidence review, scoped approval and controlled export. DataReady's existing audit → proposal → independent check → approval → separate export workflow offers a reusable starting point. The surrounding cross-product connections are proposed work. An authorized export, a rejected action and a changed prerequisite should each produce observable outcomes. This recommendation is based on reuse and measurability, not Apollo's application schedule.

**Shared case contract — proposed:** give every workflow a case ID and a versioned record containing the initiating actor and requested purpose; input references and fingerprints; recorded permission scope; data findings and proposed changes; claim/source anchors and uncertainty; policy and evaluator versions; review state; authenticated approver identity; the exact action, target, permitted scope and expiry; execution identifier and result; and references to observed effects. Minimize stored sensitive content. Link records rather than copy private raw data unnecessarily. Each component remains authoritative for its own findings. The concrete CaseRecord 0.1.1 schema, synthetic evidence example and execution semantics are in the [final plan](https://github.com/atoosabiglari-PM/atoosabiglari-PM/blob/main/docs/master-product/README.md). Schema validation is not runtime authorization.

**Infrastructure remains a product choice.** Compare providers against model availability, output validity, task performance, latency, cost, data handling and deployment needs. A 0G adapter is one optional integration candidate if it supports the product and an Apollo application. Self-hosting is another candidate requiring separate engineering and deployment validation. No provider integration, air-gapped deployment or privacy guarantee is established by the existing Gemma experiment.

# How the proposed product works

| Stage | Responsibility | User-visible result |
| --- | --- | --- |
| Intake | Identify the person, intended purpose, supplied artifacts and supported workflow | A clear case summary and missing-input questions |
| Permissions and data | RightsReady evaluates recorded use permissions; DataReady audits applicable inputs | Findings and constraints tied to the relevant artifact versions |
| Evidence | ChronicleGraph links material claims to source anchors, contrary evidence and gaps | Evidence that can be inspected and challenged |
| Proposal and review | DecisionReady presents the proposed change, affected scope, checks and unresolved issues | A draft that can be corrected, rejected or approved by an authorized person |
| Execution | SafetyGate checks current authorization for the exact supported action at the execution boundary | Allowed, blocked or approval-required outcome |
| Observation and evaluation | Capture what actually happened; use the Gemma study's measurement discipline | Execution receipt, observed effects and task outcome, reported separately |

The coordinator chooses applicable modules for the workflow. It does not mark an action permitted merely because an upstream model recommends it. Domain findings remain separate: valid data is not proof of permission; credible evidence is not authority to execute; human approval is not a substitute for a currently valid policy.

**State and failure handling:** a case moves from draft to checked proposal to awaiting approval, then to authorized execution and an observed outcome. Blocking findings stop the relevant action. A material change to an artifact, permission, policy or approved scope makes the prior approval stale and triggers reevaluation. Failed and uncertain outcomes remain visible. Retries must avoid duplicate effects; uncertain outcomes require reconciliation before another consequential attempt.

**Acceptance cases for the first integrated workflow — proposed:**

1. A permitted, supported change produces a separate output and a receipt linked to the approved version.

2. An action outside permitted scope is blocked before the protected effect.

3. Material changes to an input, candidate, permission, policy, executing identity or approved scope invalidate the applicable approval and require reevaluation. Independently check current permission/grant expiry and revocation even when all hashes remain unchanged.

4. A malformed proposal or unavailable required checker produces an explicit blocked or review state.

5. The user can inspect the proposal and evidence, correct or reject it, and stop work before the next action.

6. A failed or uncertain execution is recorded without claiming success; retry behavior is tested.

7. Every run records task outcome, attempted violations, confirmed effects, false blocks, human review steps and observation completeness. Aggregates report rates with explicit denominators and unknown/excluded counts. Repair success applies only to repair tasks.

**First-release outcome:** one genuinely connected, repeatable workflow with evidence for both successful and rejected actions. The whole six-project architecture and research program remain in scope while implementation proves these interfaces incrementally.

# Decisions to take now

| Decision | Current position | Status |
| --- | --- | --- |
| Product scope | Work on the complete master product now, independent of Apollo | Confirmed by Atoosa |
| Composition | Include RightsReady, DataReady, ChronicleGraph, DecisionReady, SafetyGate and Gemma Research | Confirmed by Atoosa |
| Human agency | People can understand proposals, inspect evidence, intervene and exercise authorized approval | Standing requirement |
| First workflow | Workflow A: governed data change/export, following the candidate comparison | Selected in the final delivery plan |
| Integration approach | Shared case contract plus narrow adapters; preserve each component's authority | Proposed technical decision |
| Research | Include the full research portfolio in the product plan; sequence experiments by prerequisites | Scope retained; experiment designs proposed |
| Evaluation | Report task utility, attempted violations and confirmed effects separately; also measure review burden and false blocks | Recommended acceptance framework |
| Commercial identity | Select a final product name, first buyer and pilot offering from validated needs | Open; no name, incorporation or traction invented |
| Apollo | Reuse suitable product materials for a separate opportunity-specific application | Optional; no submission recorded |

# Product priorities

**MoSCoW**

| Class | Work |
| --- | --- |
| Must have | One defined user problem; truthful inventory of existing capabilities; shared case/evidence contract; independent checks; verified approver and executor identities linked by scoped authorization before consequential actions; post-approval change, expiry and revocation checks; enforcement on supported paths; observable outcomes and failure handling; preservation of original data and license boundaries |
| Should have | A tested integrated workflow; claim/source traceability; repeatable evaluations; customer feedback; understandable recovery and appeal paths |
| Could have | Additional workflow adapters, provider comparisons, richer evidence browsing and reviewed examples for future model studies |
| Won't have in the first implementation | Universal control over every prompt or external tool; blanket truth or legal-compliance certification; automatic training from unreviewed approval logs; an unsupported claim that all six components are production-ready |
| Included research, staged by dependencies | Unseen-task/model evaluations, adaptive attacks, retained prohibited code, delegated authority, valid-credential abuse, false restrictions, appeals, and controlled post-training experiments |

**RICE — provisional product-planning estimates.** Score = Reach × Impact × Confidence ÷ Effort. Reach is one initial pilot workflow; impact is 1–3; confidence is an explicit planning estimate from 0–1; effort uses relative planning points, not promised hours. These estimates compare sequencing, not market size or proven returns. Re-score after inspecting interfaces and validating the user problem. Required authorization and privacy controls remain mandatory regardless of RICE score.

| Candidate work | R × I × C ÷ E | Score | Reason for estimate |
| --- | --- | ---: | --- |
| Define the pilot problem and acceptance cases | 1 × 3 × 0.9 ÷ 1 | 2.70 | Prevents building an integration without a measurable purpose |
| Draft the shared case contract and map existing interfaces | 1 × 3 × 0.8 ÷ 2 | 1.20 | Makes component gaps and responsibilities explicit |
| Build a repeatable baseline and boundary-test harness | 1 × 3 × 0.8 ÷ 3 | 0.80 | Provides evidence for every subsequent change |
| Implement the first integrated workflow | 1 × 3 × 0.6 ÷ 5 | 0.36 | High value; effort and compatibility still uncertain |
| Explore authorization post-training | 1 × 2 × 0.3 ÷ 8 | 0.075 | Potential benefit requires a stronger benchmark and curated training evidence |

**2×2 — expected product value versus implementation effort**

| | Lower effort | Higher effort |
| --- | --- | --- |
| Higher expected value | Define the user problem, map current evidence, draft the shared contract — begin here | Build identity-bound integration and test enforcement paths — sequence explicitly |
| Lower or uncertain immediate value | Cosmetic polish and extended naming debate — time-box | Broad model tuning or a universal platform before proving one workflow — evaluate after prerequisites |

# Action register and delivery evidence

| Priority | Action | Proposed owner | Completion evidence and current state |
| --- | --- | --- | --- |
| P0 | Complete and reconcile the six-project meeting record, including the research discussion | Assistant | This revised record; planning deliverable |
| P0 | Select the first workflow and define pilot acceptance cases | Atoosa, with assistant analysis | Workflow A selected in the final plan; customer demand remains a hypothesis |
| P0 | Map existing interfaces, tests, license boundaries and missing capabilities | Assistant | Repository-grounded capability/gap matrix; initial source inspection complete in the final plan; runtime verification remains required |
| P0 | Specify the shared case contract and component adapters | Assistant | CaseRecord 0.1.1 schema, synthetic example and initial interface map prepared; adapters pending |
| P0 | Inventory artifacts crossing component boundaries | Assistant | Recipient, purpose, permission/restriction and retention recorded for code, data, evidence, model payloads and logs; initial inventory in the final plan |
| P0 | Establish baseline outcomes and adversarial/changed-prerequisite test cases | Assistant | Reproducible evaluations with separate utility, attempt and effect measures; proposed engineering work |
| P1 | Implement and verify one complete workflow with human review and supported enforcement | Assistant; Atoosa provides user feedback | Observed allowed, blocked, stale-approval and recovery outcomes; not implemented by these minutes |
| P1 | Validate demand and a paid-pilot hypothesis | Atoosa with assistant preparation | Actual interview or pilot evidence, not assumed traction |
| P1 | Turn retained research tracks into controlled experiments | Assistant with Atoosa's research priorities | Protocols, data-use review, frozen baselines and scoped results; no new experiment claimed |
| Separate opportunity | Adapt verified product materials for Apollo if pursued | Atoosa and assistant | Exact application requirements and an honest product snapshot; no dependency on admission |

**Delivery sequence:** define the pilot and its acceptance cases → map capabilities and agree the contract → establish a baseline → connect one complete workflow → test and review outcomes → extend to additional workflows and research. These are dependencies within the same product, not conditions imposed by Apollo. Identity verification, durable approval records and enforcement at the supported resource boundary are required before new consequential execution.

# Product research workstreams

**Authorization and abuse of authority.** Preserve five distinct lines of inquiry: (1) authority across delegation, queued jobs and resources; (2) prohibited operations retained in otherwise passing generated code; (3) misuse by an actor holding valid credentials; (4) false restrictions on legitimate expression, reporting or other permitted activity; and (5) policy changes, operator accountability and remedies. Evaluate actions against explicit evidence and policy rather than classifying people by identity or belief. Authentication and authorization alone do not establish that a policy or its use is legitimate.

**Gemma evaluation and model research.** First expand beyond the original fixed task set with unseen tasks or another task family, an additional model, and adaptive attacks. Preserve separate attempted violations, confirmed effects and task outcomes. Add correctly and incorrectly requested escalations, false blocks, recovery after a block, invalid actions, latency and cost. If post-training is investigated, use a controlled original/tuned model × gate OFF/ON design under the same tasks and budget; test DecisionReady and other additions separately. Training methods and datasets require their own design. Existing 96-episode results do not demonstrate internal alignment, and permission logs are not automatically correct preference labels.

**ChronicleGraph and evidence quality.** Build on claim/source anchors, transmission histories, contrary evidence, competing interpretations and explicit gaps. Track whether sources are independent; do not treat provenance as proof of truth or invent a universal certainty threshold. Include the broader research goal of preparing better grounded material for future training. Optional private preservation needs separate permission, retention and access controls. This remains distinct from DecisionReady's operational dependency and impact graphs.

**Human control and accountable operations.** Study scoped approval, changed inputs or rights after approval, revocation propagation, safe retry and recovery, and reviewable operator decisions. Reviewers should see concise explanations, evidence and limitations, not be asked to trust a model's self-reported confidence or blast radius. Define how an affected person can challenge a mistaken restriction and how an authorized reviewer can remedy it. Reviewed feedback can inform regression tests; no automatic release of private archives or conversion of every operational log into training data is implied.

# Optional Apollo opportunity — historical participation check

The [official Apollo page](https://apollo.0g.ai/) reviewed during the November 14–15 discussion described an accelerator with a November 15, 2026 application deadline and no stated cutoff hour or timezone. It described up to 10 startups, a three-month December–February program, primarily remote participation with in-person graduation, and up to $2 million per project in conditional investment. It requested an active AI project, validated need/market, a revenue path, availability and meaningful 0G integration; hybrid infrastructure could be considered. These are opportunity-specific conditions, not the master product's specification.

The saved November 14 participation check records that the first application page opened without a login or verification barrier. Remaining form pages, personal/company eligibility and investment terms were not fully checked. No submitted-application receipt is recorded. The application page was retrievable during this review, but its embedded form was not fully inspected. No known Apollo account blocker has been established; eligibility and complete submission readiness remain unverified.

If Atoosa pursues Apollo, use a truthful snapshot of this product's verified capabilities, evidence and roadmap. Check the current deadline, full form and terms separately before any submission. Product planning continues independently; the program's infrastructure requirements should not silently become permanent platform dependencies.

# Source record

- [Apollo official program](https://apollo.0g.ai/) and [application](https://apollo.0g.ai/apply) — current program facts checked during preparation.

- Existing competition plan and participation register (private document) — November 14 Apollo plan.

- [DataReady repository](https://github.com/atoosabiglari-PM/dataready-autopilot), [RightsReady](https://github.com/atoosabiglari-PM/rightsready), [DecisionReady](https://github.com/atoosabiglari-PM/decisionready), [SafetyGate](https://github.com/atoosabiglari-PM/safetygate) — component documentation and code reviewed in this discussion; private repository links retain existing access.

- [Gemma public study](https://github.com/atoosabiglari-PM/gemma-authorization-study-public) and future research roadmap (private source, summarized in the research workstreams above).

- Larry Page Project Mother File (private source, summarized in the ChronicleGraph sections above).

- Atoosa's messages and the Gemini/Grok reviews shared in this discussion.

