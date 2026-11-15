# Platform case and evaluation contract — design version 2.0

This is the contract for the [conversational master product](README.md). It is a proposed integration contract, not a deployed API or a claim that existing components already accept these records. The retained [CaseRecord 0.1.2 JSON schema](case-record.schema.json) is **export-specific**; its semantics are preserved under the [optional export workflow](workflows/data-export/CONTRACT.md). It must not be used to require files or candidate exports for research questions.

## Case root and separate state dimensions

Required on case creation: `case_id`, `case_revision`, `tenant/workspace`, access policy reference, original submission ID, created time and attributable actor reference. `benchmark_question_id` is optional; when supplied, bind the registry and question version. A typed question is a complete valid input. Attachments, connected agents, quality findings, action requests and execution grants are optional collections, initially empty.

Do not force one state enum to represent everything. Maintain case review state, claim evidential status, source access state, permission/use status, agent evaluation status and action execution status independently. A case can contain contested claims, accessible sources, unknown sharing permissions and a completed read-only research run at the same time.

## Owned records

| Record / owner | Minimum fields and behavior |
| --- | --- |
| Submission / workspace | Exact original text or permitted original asset; immutable version/hash; submitter; timestamp; input modality; corrected transcript/derived version reference; access/retention. Hash is integrity evidence, not truth or ownership |
| Source / resolver + ChronicleGraph | Source ID, work/witness/edition/representation, custodian/author, URI, version/hash, retrieval/access state, relevant dates/language, rights reference, inspected scope. Never invent a missing source’s content |
| Evidence anchor / ChronicleGraph | Claim ID, source version, exact locator (passage/page/region/timecode/field), attributed wording, SUPPORTS/CONTRADICTS/CONTEXT, assessor, review and uncertainty. Authorize retrieval of excerpt and underlying source separately |
| Claim and relation / ChronicleGraph | Attributed statement, scope/date, assertion versus inference, support/counterevidence, dependency edge and evidence for that edge, alternatives/unknowns, predecessor/supersession. Unknown independence is explicit |
| Use permission / RightsReady | Relevant source/version, accessor, purpose, processor, recipients/destinations, operations, restrictions, retention, validity/revocation, permission basis and known gaps; per-use status. No blanket access-equals-sharing decision |
| Quality finding / DataReady | Applicability, input version, missing/duplicate/inconsistent findings, proposed correction, independent check, approval reference, derived version and reassessment. Never overwrite input or substitute quality for evidence support |
| Objection / DecisionReady | Contributor, targeted claim/finding version, statement/evidence, requested reconsideration, response, unresolved/resolved state, resolution reason, reviewer and appeal relation |
| Review / DecisionReady | Exact case/finding/evidence scope, readiness, reviewer issuer/subject and role assignment, conflicts/independence, approval/rejection/revision request, rationale/time, affected objections, validity and supersession |
| Agent version / SafetyGate | Owner/connection authority, stable agent/version/configuration hash, model/prompt/tool/memory versions where available, declared permissions/purpose, endpoint/package provenance and observability limits |
| Evaluation run / SafetyGate + evaluation | Case/question/packet/rubric versions, agent config, admission result, behavioral results per criterion, observed outputs/tool events, independent effects, resource budgets, uncertainty/coverage, actionable feedback, predecessor/reassessment reference. Admission PASS and behavior PASS are distinct |
| Human-rights assessment / SafetyGate | Model/version and permitted context, concern category, observations with spans/events, separate inferences, uncertainty/missing facts, affected interests, criterion, suggested remedy, independent-review assignment and disposition/appeal. Never an access credential or final person-level determination |
| Action request/grant / gateway | Exact principal/agent version, data/field scope, purpose, action, recipient/account/destination, case/finding/evidence versions, permission/policy/role bindings, reviewer, audience, validity/revocation and protected proof reference |
| Execution/effect / gateway + observer | Request digest, scoped idempotency key, authorization decision time, acceptance/commit time when known, attempted action, observed receiver/output, receipt, observer coverage, SUCCESS/FAILED/UNCERTAIN and reconciliation history |
| Incident / authorized investigator | Scope/authority, record interval, observed transfers and identifiers, inferred correlations labeled, receiving service/account versus proven ultimate user, missing intervals, corrections/remedies and reviewer |

Every component writes its own authenticated finding. A coordinator or model cannot set an `authoritative=true` field and thereby acquire authority. API responses validate producer identity, version and integrity; per-tenant access applies to references and content, including indexes and logs. Return explicit NOT_APPLICABLE/UNKNOWN/UNAVAILABLE states instead of fabricated favorable results.

## Version changes, reviews and authority

Append changes and link predecessors. A source or extraction correction creates a new version. Compute a dependency-aware difference identifying which claims and approvals rely on the changed evidence. Material changes to evidence, proposed action, permission, policy, identity/role assignment, agent configuration or approved scope invalidate the affected approval/grant and trigger reevaluation. Preserve unrelated valid decisions and record why.

Use a signed scoped action grant, with human approver and executing agent/service separately authenticated. Bind the exact action and current authoritative preconditions using canonical serialization and a digest. Verify issuer, key/algorithm, audience, executor, scope, current roles, time and revocation at the enforcement boundary. Hash equality does not detect expiry or newly revoked authority. Missing mandatory checks cannot return ALLOW. An evaluation result is not a grant.

Official-finding promotion must compare-and-set the reviewed revision and write the decision/receipt transactionally. Each external-action adapter must document when acceptance becomes non-retractable, how revocation races resolve, and how receipts/idempotency/reconciliation work. Never promise a database transaction controls an unrelated external service. Unknown outcomes remain UNCERTAIN; an empty receipt list is not evidence of zero effects if observation is incomplete.

## Data and human-rights boundaries

Access, processing, onward disclosure, training and retention require distinct applicable permission checks. This includes speech/model/search processors before sending them context. Unknown permission is explicit and blocks the affected use or routes it to review; it need not block permitted parts of a research question. Restricted original evidence may be inspectable only by authorized users; public readers get an accurate access explanation rather than leaked excerpts.

The rights-assessment LLM emits advisory evidence-linked concerns only. Deterministic policy routes high-impact/uncertain cases to an independent reviewer and holds required actions pending disposition. Reviewers cannot override non-overridable prohibitions or grant authority beyond their role. Retain objections, dissent, notice/appeal where appropriate, and correction/remedy history. Do not create automated person-level guilt, eligibility or credibility scores from such assessments.

## Measurement and limits

Every run records utility, attempted out-of-scope actions, confirmed effects, false blocks and review burden separately, including unknown/inapplicable values. Aggregate only against explicit eligible denominators and report excluded/incomplete observations. Research scoring uses the actual workbook’s rubric and reviewed reference packets; disclosure of all fifty makes them development cases, not an unseen holdout. Keep Gemma prototype evidence in a separate namespace from platform runs. Synthetic fixtures stay labeled synthetic.
