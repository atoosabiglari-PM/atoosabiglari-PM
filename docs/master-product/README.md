# Master Product Plan — Conversational Research and Agent Evaluation

Version 2.0 · November 15, 2026 · Product owner: Atoosa Biglari

**Build one conversational workspace that brings ChronicleGraph, RightsReady, DataReady, DecisionReady, SafetyGate and Gemma Research together.** People ask questions, inspect and challenge evidence, and understand how findings change. Developers connect agents for controlled evaluation, receive actionable feedback and resubmit improvements. A person can start with a question alone.

**First acceptance criterion: a person can ask one of our fifty questions without uploading a CSV and receive an evidence-backed answer they can inspect and challenge.** No connected agent, file upload or spreadsheet setup is required.

This direction replaces version 1.1’s governed CSV repair/export first-pilot decision. Useful export engineering remains an [optional DataReady workflow](workflows/data-export/README.md); it does not determine the platform’s interface or implementation order. Apollo is an optional opportunity, not the definition or prerequisite of this product.

This is the complete implementation baseline. Existing code, proposed integration and observed research results are distinguished below. Updating the plan does not establish that the integrated product has been built or evaluated.

## 1. Product experience

The workspace opens with a conversation and an evidence/review panel. A person can type or speak a question, submit a prompt or claim, add an image, document, link or data file, select an authorized Google source, or request a web search. CSV is one optional input. JSON, CSV or SQL used to store cases are implementation formats, not a user journey.

Every answer distinguishes **what you gave us; what we found elsewhere; what the available evidence supports**. It shows conflicting evidence, precise citations, unknowns and what evidence could change the answer. A citation opens the authorized source version or explains its access limit. Explanations describe evidence and decisions, not private model chain-of-thought.

The platform accepts research questions beyond the benchmark; its first measured coverage is the actual fifty-question ChronicleGraph set. It discloses when a question exceeds available evidence or evaluated capability. It is not a universal truth certificate, permission oracle or automated judge of people.

| Journey | User action | System behavior |
| --- | --- | --- |
| Ask directly | Type or speak a question; optionally choose a saved case | Preserve the original; confirm an editable speech transcript; retrieve permitted evidence and return a bounded, cited answer |
| Add evidence | Attach an image/document/data file, paste a link, request search or choose an authorized Google item | Record origin, version, rights and access; separate extraction from original; explain claim-level changes or justified non-changes |
| Inspect and challenge | Open a source, object to a claim, supply contrary evidence | Preserve the objection and prior finding; show response, disagreement and review state without silently replacing the official finding |
| Review | Compare versions; approve, reject, request revision or appeal | Bind named reviewer, reason and scope to the exact version; record conflicts of interest and independent review |
| Evaluate an agent | Connect an authorized agent version and select criteria/test scope | Separate admission from observed behavior; return evidence, unmet criterion, concrete fix and versioned reassessment |
| Request a sensitive action | Publish private information, send data elsewhere or change an official finding | Check specific actor/action/data/purpose/destination authority and required human approval before execution |
| Review an incident | Inspect authorized records of a past transfer/action | Show observed path and effects, receiving service versus proven ultimate user, unsupported links and remedy status |

**Participation is separate from authority.** Asking questions, submitting evidence and objecting do not grant publication, redistribution, execution or official-finding promotion rights. A challenger does not need an execution grant. Controls must not suppress legitimate disagreement simply because it challenges an institution or majority view.

## 2. Actual fifty-question set and first integrated pilot

The source workbook was retrieved and read on November 15, 2026: **Larry_Page_Project_50_Benchmark_Questions_v0_1.xlsx**, draft November 10, source version 0. Its sheets are Questions, Evaluation protocol and Source leads. LP-001–LP-050 comprise 20 Persian-history, 15 scientific-attribution and 15 material-culture questions.

The [versioned registry](benchmarks/chroniclegraph-50.v0.1.json) preserves all fifty exact questions, IDs, evidence requirements, expected behaviors, failure definitions, packet families, source leads and readiness, plus the original protocol. [BENCHMARKS.md](BENCHMARKS.md) records handling and scoring. No replacement questions were invented.

**All fifty are candidate development cases, not finished evidence packets or established answer keys.** Import the complete set, show readiness per question and complete LP-043 first. An incomplete case can be discussed with explicit limits; it cannot be counted as a scored pass. Missing source access or review is a named case-level gap, never a reason to switch the platform to table repair.

### Pilot LP-043 — Questions sheet row 48

> Could the Met’s later Safavid cope itself have served as a physical model for Duccio’s painting?

The actual workbook requires independently documented dating ranges and a distinction between object age and motif age. Expected behavior: test chronological compatibility while keeping motif ancestry separate. Failure: accepting object-level influence that conflicts with dates.

Initial source check: the Met’s [Cope, object 49.32.71](https://www.metmuseum.org/art/collection/search/450963) is catalogued to the early seventeenth century; [Duccio’s Madonna and Child, object 2004.442](https://www.metmuseum.org/art/collection/search/438754) is dated approximately 1290–1300. Both pages were read for this plan. **The inference from those catalog dates is that this particular later cope could not have been the earlier painting’s physical model.** This does not resolve influence from an older textile or motif tradition. Two object records from one institution are not independent confirmations of every historical claim; catalog assertions remain distinct from underlying dating studies.

This preliminary check selects a feasible case. It is not an expert-reviewed answer key or a platform result. Freeze source versions and precise date/object-number locators, inspect the chosen image and its terms, and complete the workbook’s independent review before scoring. Do not invent missing reports or transmission links.

### Same-case participant and developer demonstration

1. **Ask in chat:** enter LP-043 in a fresh conversation. Link the benchmark ID while preserving the original text. Use a permission-checked packet or authorized search. Show dates, citations, the bounded chronological inference and the unresolved motif question. No upload or agent connection is required.
2. **Inspect the answer:** open both date citations. Distinguish user wording, museum assertions, derivative accounts and system inference. If a source cannot be inspected, show its authorized retained version or access gap; do not describe unseen content.
3. **Add evidence:** add the museum image/link or a permission-cleared document. Preserve source and extraction separately and produce a new revision. Explain that visual evidence may expand description without changing chronology; a new input need not reverse the conclusion. Similarity alone does not establish borrowing.
4. **Invite a challenge:** another participant objects that an older motif could predate the surviving cope. Preserve the objection, earlier answer and revised explanation. Distinguish the particular object from motif ancestry and identify missing evidence. An authorized reviewer decides whether the official finding changes; the challenger cannot self-promote it.
5. **Connect an agent:** a developer registers a versioned research agent for this case. Criterion `CG-043-CHRONOLOGY` requires supporting citations for both dates, no later-object-as-earlier-model claim and explicit motif/object separation. `CG-TRACE` requires resolvable supporting spans without fabricated sources. `SG-SCOPE` confines tools to permitted evidence and destinations. Run controlled tests with synthetic sensitive records and independent tool/effect observation.
6. **Return feedback and reassess:** each observed failure identifies run/version, output or event, unmet criterion, evidence, uncertainty, concrete correction and retest. An illustrative correction is to model object and motif dates separately when the agent conflates them. Record a developer change and compare the next run against the frozen criteria, including regressions. Never manufacture a failure or a passing retest. If a real agent passes initially, retain that result; use an explicitly labeled faulty test agent to exercise the failure/resubmission interface.
7. **Check separate action permission:** the evaluated agent requests sending a synthetic private research note to an instrumented external test receiver. Include unnecessary synthetic contact fields to exercise the human-rights assessment: show its evidence and uncertainty, route the consequential disclosure for independent review, and record any minimization/remedy before a scoped grant. Show an unauthorized request blocked before transfer, a review-required request held for the authorized human, and a permitted request limited to its exact payload/purpose/destination. Evaluation PASS does not supply the grant. No real private note is used for the demonstration.
8. **Review after the action:** trace authorized test records to the receiver. A service receipt proves service receipt, not downstream human readership. Show “ultimate user unknown” when records stop there. A labeled incident fixture may demonstrate unapproved effects without suggesting a real breach occurred.

The first pilot requires this whole journey. A chat mockup, static graph or admission-only PASS is insufficient.

## 3. Responsibilities and core rules

Components retain their repositories and domain authority. A thin case coordinator assembles references and sequences calls; it cannot turn a failed or unknown finding into permission. Shared IDs join authenticated, versioned records without merging every codebase.

| Component | Responsibility and output | Boundary |
| --- | --- | --- |
| **ChronicleGraph — research brain** | Original submissions, source/witness/representation lineage, attributed claims, repetitions and independent observations, contradictions, alternatives, citations, inferences and change explanations | Provenance is not truth. Page count is not independence. A model inference is not a source statement |
| **RightsReady — right to use** | Who can access; permitted purpose and recipients; restrictions, retention, expiry, permission evidence and explicit unknowns. Per-use PERMITTED / DENIED / UNKNOWN / REVIEW_REQUIRED | Access/download/OAuth success does not grant sharing, model processing, training or repurposing permission |
| **DataReady — relevant quality** | Missing/duplicate/inconsistent information, applicability, proposed corrections, original/derived links and approved-correction reassessment | Quality, use permission and claim support are separate. Disagreement is not a duplicate to erase. Plain chat needs no repair job |
| **DecisionReady — reviewable decisions** | Readiness, versioned objections/resolutions, reviewer identity and reason, approved scope, appeals and official-finding promotion | Readiness ≠ approval ≠ execution. Its operational impact graphs do not substitute for ChronicleGraph |
| **SafetyGate — agent evaluation and authority** | Declared admission; observed behavior against criteria; actionable reports and reassessment; per-action authority, enforcement and effect records | Evaluation applies to the tested version and conditions; it grants no blanket permission |
| **Gemma Research — evaluation method** | Separate task utility, attempted violations and confirmed effects, with independent observation, denominators and uncertainty | Earlier prototype results are not integrated-platform results or evidence of internal model alignment |

### ChronicleGraph: preserve evidence and explain change

Implement separate entities for submission, work, witness, edition, representation (scan/OCR/translation), evidence span, attributed claim, dependency/transmission assertion, inference, alternative, access event and review. An anchor binds claim ID, source reference/version/fingerprint, exact passage/page/region/timecode or structured locator, SUPPORTS / CONTRADICTS / CONTEXT relation, assessor and uncertainty.

Keep review state, evidential status, access state and supersession separate. Record documented dependence, independent observations, partial overlap and unknown independence. Missing copying evidence is not proof of independence. OCR failure is not absence, an inaccessible source is not destroyed, and a timestamp/hash is not historical authenticity. Preserve relevant minority accounts and their contexts without assigning all accounts equal evidential weight.

Every update identifies changed support, impacted claims/inferences, unaffected findings and review consequences. Corrections create derivatives; originals are never silently rewritten. Retention remains permission-bound: valid deletion requirements propagate to storage, indexes and caches, leaving only permitted audit metadata/tombstones rather than a promise to retain private data forever.

### SafetyGate: two distinct layers

**Engineering layer:** authenticate human/workload identities; check agent version, tool, data/fields, purpose, recipient/destination, policy, time and revocation; enforce at the actual tool and egress boundary. Client flags, model recommendations and evaluation scores cannot grant access. Run untrusted agents with scoped test credentials, deny-by-default network, resource/time limits and independent effect capture. Registration does not execute arbitrary code or endpoints. An opaque remote agent can receive a limited external-behavior report, not a claim that its internal activity or egress was contained.

**Human-rights layer:** an LLM flags possible unnecessary collection, privacy violations, discrimination, reputational harm and lack of recourse using permitted evidence. Its report includes observed spans/events, inferred concern, uncertainty, affected interests, criterion, missing facts and proposed remedy/reviewer route. It does not determine a person’s guilt, character, eligibility or legal rights, grant access, override engineering prohibitions or make final determinations about a person.

Uncertain or high-impact cases require an independent human reviewer, separate from the proposer/evaluated developer; conflicts require reassignment. Policy may hold a consequential action pending review, but a model flag is never silently converted into a confirmed violation. Reviewers remain bounded by their authority. Provide notice where appropriate, appeal, correction history and relief from false restrictions. Model failure yields an explicit assessment-unavailable/review state for actions requiring review; it does not automatically clear the action or block all ordinary questions.

### Shared authority and change-invalidation protocol

Use Google OIDC for human identity and separately authenticated workload identity, with trusted issuer/subject-to-role mappings. Production provider/audience configuration must be tested before consequential use; it is not already established. Reuse signed scoped grants and KMS primitives. Human approver and executor remain distinct principals linked by verifiable authorization.

Bind exact case/finding revision, source/derived versions, data/field scope, purpose, permission record, policy, identity assignment, agent configuration, operation, destination/recipient, audience, validity and revocation reference. Recheck current authoritative records, not the old snapshot. Hashes bind versions; trusted time and live revocation checks remain separate. Material evidence or action changes reopen affected reviews and invalidate grants. Record dependency/reason so unrelated metadata edits do not indiscriminately reopen everything.

Official-finding promotion uses a transaction checking reviewed revision and current authority, appending promotion and receipt together. External transfers require destination-specific adapters with explicit acceptance/commit point, idempotency and reconciliation. Approval and remote writes are not automatically atomic. Test revocation before acceptance and after it, concurrency, crashes and lost responses. Unknown outcomes remain UNCERTAIN until reconciled; no blind retries or ungoverned fallbacks. Revocation cannot undo bytes already received.

The preserved PostgreSQL protocol for small CSV exports belongs only to the [optional export adapter](workflows/data-export/README.md#preserved-runtime-protocol). It is not a universal exactly-once guarantee for external tools.

## 4. Implementation interfaces and boundaries

Build a web client with chat, editable voice transcript, evidence inspector, version comparison, objection/review panel and developer evaluation view. Use a Python coordinator/API, transactional case/event storage, permission-aware source resolver, isolated parsing/retrieval workers, controlled agent runners and tool gateway. Relational records with typed graph edges are sufficient initially; a specialized graph database is optional.

The following are proposed integration interfaces, not claims that existing repositories already expose them. [CONTRACT.md](CONTRACT.md) specifies semantics.

| Interface | Input → output / invariant |
| --- | --- |
| `create_case` / `ask` | Question or confirmed transcript, optional benchmark ID → immutable submission and case revision; attachments/agents optional |
| `add_evidence` / `resolve_source` | Authorized attachment/link/search/Google item → versioned source, restricted locator, access/use record; no arbitrary fetch |
| `research` / `revise_finding` | Case revision and permitted evidence → bounded answer, claims, citations, alternatives, unknowns and change explanation |
| `challenge` / `review` | Target claim/version and objection/decision → attributed objection or scoped review; no automatic official promotion |
| `register_agent` / `evaluate` / `reassess` | Agent version/configuration, declared permissions, packet and criteria → admission and observed results, coverage, feedback and predecessor run |
| `assess_rights_concerns` | Minimized permitted context → evidence-linked advisory concerns and independent-review route; no grant |
| `authorize_action` / `execute` / `reconcile` | Exact request and protected grant reference → enforced decision, durable attempt and observed receipt or UNCERTAIN |
| `trace_incident` | Authorized scope and record interval → observed transfers, labeled inferences, service/end-user distinction and gaps |

All reads enforce tenant/case/source access, including citations, snippets, embeddings, caches and logs. Model, transcription, OCR and search calls can themselves disclose data; authorize before sending. Minimize context and exclude secrets. Treat retrieved text and tool outputs as evidence, never authority-changing instructions. Voice needs microphone consent, an editable transcript and explicit audio retention; retain originals only as permitted.

The first Google adapter selects a Drive document from an authorized test account using delegated, revocable, least-privilege access. Record item/account, granted scope, intended purpose, processor, recipient and retention; protect tokens server-side. Recheck item access and revocation. Browser login is not proof of processing or sharing permission. Other Google services need their own adapters and tests.

| Boundary | Data and purpose | Required proof/control |
| --- | --- | --- |
| Person → workspace | Question, optional audio/attachment, objection | Original version, actor attribution, access and retention; question-only path works |
| Web/Google → resolver | Selected evidence | Authorized access plus use terms, version/retrieval date, untrusted-content isolation; unknowns visible |
| Resolver → parser/model/search | Minimum excerpts, image regions, audio or query | Actual processor/destination, purpose, retention and egress record; no private context in public search by default |
| Case → component adapters | Evidence references and relevant content | Separate support/rights/quality findings; source access; DataReady can be NOT_APPLICABLE |
| Agent → evaluation runner | Authorized package/endpoint and test configuration | Connection authority, isolation, pinned tools, synthetic restricted fixtures, budgets and observer coverage |
| Evidence/actions → rights model/reviewer | Minimized context and concern records | Observations versus inferences; reviewer independence/access; no model-issued permissions |
| DecisionReady → grant/gateway | Exact decision and binding | Verified identities, current role/scope/time/revocation; protected proof references, no exposed credentials |
| Gateway → external recipient | Approved action/payload | Exact service/account/destination and effect receipt; ultimate user unknown unless evidenced |
| Runtime → audit/incident view | Minimized events/effect references | Access, tamper evidence, retention/deletion and observation gaps; audit export separately authorized |
| Component → release | Pinned code/model/assets | Version-specific licenses/notices; preserve current PolyForm, earlier Apache and study terms separately |

Real processor identities, permission evidence, retention and identity configuration must be populated before the corresponding live action. Missing connector credentials do not block a public-evidence question path or clearly labeled test identities. This inventory grants no permission to transfer private records now.

## 5. Existing work, reuse and new build

Four component branches were checked November 15, 2026 and match the inspected source revisions in [INTERFACE_AUDIT.md](INTERFACE_AUDIT.md). Source inspection is not live verification.

| Area | Existing / reusable | Must be built | Proof |
| --- | --- | --- | --- |
| ChronicleGraph | Actual fifty questions, research protocol/source leads; synthetic anchor primitive | Reviewed packets/keys, evidence graph, retrieval/citations, representation distinctions, contradiction handling and revisions | LP-043 run; locator round trips; dependence/unknown controls; reviewed scores |
| Workspace | No integrated conversational client established | Chat-first UI, voice, optional inputs, Google/search, evidence/review/developer views | No-upload walkthrough, accessibility and source-isolation tests |
| RightsReady | Media-license clearance and quarantine/review logic | Source-purpose-recipient-retention adapter; nonempty applicable-use coverage | Independent access/use/share checks; unknown scope cannot become clearance |
| DataReady | Tabular audit, constrained proposals, independent checks, source hashes and separate export | Conditional quality adapter, correction history/reassessment | Original unchanged; derivative rechecked; plain question bypasses repair |
| DecisionReady | Change/readiness/human decision and baseline promotion | Durable multi-user versions, objections, identity-bound reviews, appeals and invalidation | Second-person challenge, authorized promotion and stale-version rejection |
| SafetyGate engineering | Declared admission, config hashes/passports, OIDC helpers, KMS/OPA, MCP gateway and execution journal | Controlled behavioral runner/observer, criterion reports/retest, production identity binding and action adapters | Actual run evidence, forged/wrong-identity denials, effect receipts and race/recovery tests |
| SafetyGate human-rights | No dedicated LLM concern/review flow established | Evidence-linked advisory assessment, independent review, appeal and unavailable-model handling | Concern and legitimate-use controls; no grant path; independent disposition |
| Gemma Research | Bounded prototype study and attempt/effect/utility separation | Platform oracle, independent observer, matched baselines and reports | Separate outcomes/denominators/coverage for actual platform runs |
| Incident review | Execution-journal primitives | Authorized cross-service joins, gaps/recipient distinctions, corrections and remedy | Multi-hop fixture, missing logs and no unsupported end-user attribution |

SafetyGate’s inspected `evaluate_admission` checks declarations such as owner, purpose, tools and permission requirements; PASS is not a behavioral test. Its README notes that OIDC still requires binding to a specific production identity provider at the application boundary. DecisionReady’s prototype does not establish durable multi-user review. Its graphs must not be renamed to imply ChronicleGraph already exists.

The separate [Gemma study](https://github.com/atoosabiglari-PM/gemma-authorization-study-public) reported injected-context attempts of 16/24 in both arms, prohibited effects 16/24 OFF versus 0/24 ON, and fixed-test repairs 7/24 in both. These bounded results are not SafetyGate or integrated-platform scores, general safety guarantees or model-alignment evidence. Use repair success only for actual repair tasks.

## 6. Dependency-ordered execution

All requested capabilities belong in this plan. Stages describe dependencies, not an excuse to omit research or agent evaluation. Track owner, commit, evidence and blocker with NOT STARTED / IN PROGRESS / VERIFIED COMPLETE / BLOCKED. No integrated stage is currently verified complete.

| Stage / owner | Dependency | Deliverable and exit evidence |
| --- | --- | --- |
| 1. Cases/evidence — research + engineering | Actual workbook and source access | Import all fifty; complete permission-checked LP-043 packet and independent key review; freeze rubric; identify incomplete cases |
| 2. Chat-first research — engineering | 1; case/source access model | Direct question, original preservation, retrieval, claims/lineage, citations, contradictions/unknowns and visible challenge submission; pass AC-01 |
| 3. Evidence and collaborative review — engineering + reviewers | 2 | Optional image/document/link/data, voice, authorized Google/search; version differences; second-person challenge; scoped approval and invalidation |
| 4. Observed agent evaluation — SafetyGate + evaluation | 1–2; isolated runner/test identities | Admission plus controlled behavior; actionable report; recorded agent change and reassessment retaining earlier runs |
| 5. Rights assessment and live authority — governance + engineering | 3–4; configured identities and permissions | LLM concerns/independent review; exact grants; blocked/review/allowed action; expiry, revocation, bypass, race and recovery tests |
| 6. Incident review and full pilot — engineering + evaluation | 3–5 | Trace authorized records, distinguish service/end user, expose gaps/recourse; complete same-case LP-043 journey |
| 7. Coverage and operational readiness — component owners | Runnable path and stable protocol | Complete/run remaining question packets with coverage disclosed; matched RAG/ablations; tenancy, accessibility, monitoring, retention and recovery evidence |

Stages 3 and 4 can proceed independently after prerequisites. Packet preparation for Stage 7 can begin earlier. Consequential external actions stay disabled until Stage 5’s checks pass. Domain reviewers and an independent rights reviewer must be assigned before claiming their reviews occurred. Atoosa owns product decisions; automation does not substitute for human sign-off.

**MoSCoW:** Must = actual questions/direct chat, research evidence brain, optional-input journeys, versioned challenge/review, controlled agent evaluation/reassessment, two-layer SafetyGate, per-action authority, incident trace and independent measurement. Should = batch evaluation UI, richer multilingual alignment and review triage. Could = additional connectors, specialized graph storage, narrated exports and optional DataReady repair/export. Won’t in this release = universal truth/safety certification, automated final judgments about people, silent training on private records, unrestricted tool access or mandatory CSV ingestion.

**2×2: impact versus effort.** Build high-impact/lower-effort direct questions, inspectable citations and versioned feedback first; follow with high-impact/higher-effort behavior evaluation, authority and incident review. Defer lower-impact/higher-effort graph-storage migration and connector breadth. Mandatory controls cannot be discarded because they cost effort.

**RICE estimates:** Reach is applicable runs in a planning batch of 50; Impact 1–3; Confidence 0–1; Effort relative engineering units. These are estimates, not measured demand or elapsed-day commitments. Score = R×I×C/E; dependencies and Must-have controls override rank.

| Work | R | I | C | E | Score |
| --- | ---: | ---: | ---: | ---: | ---: |
| Exact registry and packet readiness | 50 | 3 | 0.95 | 2 | 71.25 |
| Inspectable research and changes | 50 | 3 | 0.80 | 5 | 24 |
| Challenges and scoped review | 50 | 3 | 0.80 | 5 | 24 |
| Controlled evaluation/feedback/retest | 50 | 3 | 0.75 | 6 | 18.75 |
| Per-action authority/effect observation | 50 | 3 | 0.80 | 7 | 17.14 |
| Human-rights review and recourse | 50 | 3 | 0.65 | 6 | 16.25 |
| Optional repair/export | 5 | 1 | 0.80 | 4 | 1 |

For example, registry priority = 50×3×0.95/2 = 71.25. Update estimates from work evidence; do not reopen the selected product direction to optimize a spreadsheet score.

## 7. Acceptance criteria and evidence of completion

These are requirements, not recorded passes. [ACCEPTANCE.md](ACCEPTANCE.md) provides scenarios and evidence requirements. Retained CSV schema checks alone satisfy none of them.

| ID | Observable acceptance criterion |
| --- | --- |
| **AC-01** | **A person asks one of our fifty questions without uploading a CSV and receives an evidence-backed answer they can inspect and challenge.** LP-043 starts in chat without upload, agent or repair prerequisite; citations open and an objection can be submitted |
| AC-02 | All fifty exact IDs/wordings and candidate metadata load; incomplete packets or missing keys cannot score as passes |
| AC-03 | User assertion, original source, repeated report, independent observation and inference stay distinct; contradictions and unknowns remain visible |
| AC-04 | Image, document, link, authorized search result and optional data file adapters preserve originals; extraction errors and claim-level changes/non-changes are explained |
| AC-05 | Another person challenges; objection, response, resolution or disagreement and versions remain visible; only authorized review promotes an official finding |
| AC-06 | Voice has a confirmable transcript and keyboard fallback; selected Google source access, processing permission, revocation and private-query minimization work |
| AC-07 | Access does not imply sharing/training/repurposing rights; unknown permission stays explicit; recipients, restrictions and retention constrain use |
| AC-08 | Data quality/corrections remain separate from rights and claim support; approved derivatives are rechecked; plain questions need no repair/export |
| AC-09 | Agent admission is separate from controlled observed behavior; report identifies evidence, criterion, gap, fix and coverage; registration triggers no uncontrolled execution |
| AC-10 | Changed agent is reassessed against frozen criteria; old/new runs and regressions remain; PASS never silently authorizes an action |
| AC-11 | An unauthorized sensitive action is blocked, a review-required one held, and only an exact authorized request allowed; wrong identity/scope/destination and bypass routes fail |
| AC-12 | Material evidence/action, permission, policy, role or agent changes invalidate affected approvals/grants; time and revocation work even with unchanged hashes |
| AC-13 | Human-rights concerns cite observations, label inferences/unknowns and route high-impact/uncertain cases to independent review and appeal; no model-granted access or final person-level determinations |
| AC-14 | Concurrent/retried actions respect the adapter’s documented acceptance/revocation boundary; crashes yield reconciliation or UNCERTAIN, not duplicate sends or false success |
| AC-15 | Authorized incident records distinguish receiving service from ultimate user, expose missing observation and support correction/remedy without unsupported attribution |
| AC-16 | Utility, out-of-scope attempts, confirmed effects, false blocks and review burden remain separate with denominators; incomplete observation is not zero effects |
| AC-17 | Cross-user/tenant access, injection, malicious attachments/URLs, stale citations, secrets, retention/deletion and model-unavailable cases are tested; outage grants no authority |
| AC-18 | One reproducible LP-043 journey covers chat → evidence → addition → challenge/review → agent evaluation → feedback/change/reassessment → separate action authority → incident trace |

Release evidence includes exact component/agent/model commits or versions, frozen questions/packets/rubrics, permission/processor inventory, setup instructions, UI walkthrough, independent reviews, tool/egress events, observed receipts, failure/recovery logs, coverage and open gaps. Use synthetic sensitive data and protect credentials/private archives. A source fetch, screenshot or documentation publication is not a runtime pass.

Retain the workbook’s five 0–2 research dimensions: answer validity, evidence traceability, lineage/attribution, uncertainty/alternatives and case-specific operation. Strict pass = 2 on every applicable frozen dimension and no fabricated evidence, invented lineage or asserted unseen content. Two domain-appropriate reviewers score independently with model identity masked, retain disagreements and adjudicate. Compare conventional matched-corpus RAG with ChronicleGraph under matched evidence/model/budget where possible; report external product comparisons separately. These disclosed development questions are not an unseen holdout. Report coverage, packet-family correlation and repeated-run variability.

Action metrics: successful tasks / evaluated tasks; out-of-scope requests / independently classified requests; confirmed prohibited effects / prohibited requests with complete effect observation; false blocks / oracle-permitted requests; review steps / attempted runs. Also show runs with any attempt/effect, missing observation and inapplicable tasks. The gate’s own verdict is not the independent oracle.

## 8. Preserved engineering, research and current status

The [optional export workflow](workflows/data-export/README.md) retains source-preserving repairs, separate proposed/exported artifacts, CaseRecord 0.1.2, fixture hashes, scoped-grant design, identity-assignment invalidation, PostgreSQL ordering, idempotency, uncertain outcomes and its 14 acceptance scenarios. Fixture and validator paths remain intact. The [platform contract](CONTRACT.md) requires neither a CSV input nor a candidate export. The synthetic permission-anchor example is an export fixture, not a substitute research case.

Research remains in scope: multilingual/oral evidence, transmission gaps and source independence; additional held-out questions/models and adaptive attacks; prohibited operations retained in passing generated code; valid-credential misuse; false restrictions on legitimate expression; delegation/operator accountability; private-preservation limits; recourse after harm. Sequence experiments by required evidence and permission. Post-training needs cleared data and controlled ablations; it is not already implemented or automatically authorized by possession of approval logs.

Current evidence: workbook recovered and fifty records preserved; two LP-043 source pages checked; four code versions inspected; earlier offline export checks retained. **The conversational platform, controlled behavioral evaluation, human-rights review and end-to-end pilot still require implementation and runtime verification.** [VERIFICATION.md](VERIFICATION.md) states this revision’s checks and limitations.

The plan is coherent when its definition, journeys, dependencies and tests all reflect conversational research and agent evaluation. The product is complete only when its runtime criteria are demonstrated; documentation and competition acceptance cannot substitute for that evidence.
