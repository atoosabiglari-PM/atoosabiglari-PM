# ChronicleGraph fifty-question benchmark registry

## Source and fidelity

Read on November 15, 2026 from **Larry_Page_Project_50_Benchmark_Questions_v0_1.xlsx**, Library source version 0, modified November 10, 2026 at 21:31:47.081773 UTC. All three sheets were read: Questions, Evaluation protocol and Source leads. The [registry](benchmarks/chroniclegraph-50.v0.1.json) preserves the actual 50 rows, all 11 question fields, original sheet/row references, all 32 protocol rules and all 12 institutional source leads. Its extracted-text digest identifies the Questions sheet representation returned during retrieval; it is not a hash of the XLSX bytes.

No raw private archive, credentials or Library sharing permissions are changed. The published registry is a transcription of these research questions and planning metadata, not a publication of the underlying source images, interviews or historical evidence packets. Source-lead inspection notes are the workbook’s original notes, not a claim of fresh inspection of every URL. The two LP-043 Met object pages were separately checked for this plan.

| IDs | Count | Domain |
| --- | ---: | --- |
| LP-001–LP-020 | 20 | Persian history |
| LP-021–LP-035 | 15 | Scientific attribution |
| LP-036–LP-050 | 15 | Material culture |

The workbook’s P1–P6 are its research-pillar codes, not the six product components: layered multilingual preservation; claim lineage; oral evidence/recording context; patterns/competing explanations; documented access gaps; private-preservation limits. Preserve these original meanings.

## First case and readiness

Selected question **LP-043**, Questions row 48:

> Could the Met’s later Safavid cope itself have served as a physical model for Duccio’s painting?

Evidence required: both objects’ independently documented dating ranges and distinction between object and motif age. Expected behavior: test chronological compatibility and keep motif ancestry separate. Failure detected: accepting object-level influence that conflicts with dates. Original source leads: S10, S11, S12. Initial packet uses S10 (cope) and S12 (painting); S11 is a comparator lead, not required evidence that was already inspected for this case.

All 50 original rows remain **Candidate**. The source workbook explicitly says that no complete historical evidence packet, answer key, model output or performance result had been produced. The plan’s preliminary LP-043 source check does not silently change this readiness or constitute expert review. Track evolving packet/review/run readiness separately from the immutable source registry.

## Packet preparation and scoring

1. Preserve question wording/ID; record every versioned scope change and why. Complete LP-043 first; import all 50 without pretending all packets are ready.
2. Select exact source versions, custodians, work/witness/edition, languages/dates, retrieval/access records, hashes, permissions and precise page/folio/region/timecode spans. Inspect needed images/audio. Search leads alone are not answers.
3. Have two domain-appropriate reviewers establish supported propositions, mandatory spans, dependencies, admissible alternatives, unknowns and disallowed inferences. Record disagreements and adjudication. Keep answer keys out of the retrievable evidence corpus used for evaluation.
4. Freeze applicable dimensions and rubric: D1 answer validity, D2 evidence traceability, D3 lineage/attribution, D4 uncertainty/alternatives, D5 case-specific operation; each 0–2. Strict pass requires 2 on each applicable dimension and no critical error. Report component scores and total/applicable maximum, not truth probabilities.
5. Track fabricated evidence, invented lineages and asserted unseen contents independently. Incomplete evidence may justify a bounded insufficient-evidence answer; it never justifies an invented answer key.
6. Record model/configuration, prompt, retrieved evidence, output, tool settings, latency, cost, timestamp and packet/rubric versions. Use three repeated runs for stochastic systems and report variability and packet-family correlation.
7. Compare ChronicleGraph with matched-corpus conventional hybrid retrieval/RAG using the same model, evidence access and budget where feasible. Run lineage/context ablations. Keep external GPT/Claude/Grok/Search product comparisons separate with exact modes/dates/configurations.
8. These 50 disclosed questions are for development and calibration. The workbook proposes 25 additional held-out questions from different claim/episode families/witnesses after the rubric stabilizes. They do not exist in this registry; do not invent them or claim an unseen holdout. Screen overlap and protect keys from development/training exports.

Historical cases need real inspected material. Controlled fixtures may introduce labeled duplicates, corrections, withheld fields or synthetic metadata only for the operation specified by the actual question. Never label a manufactured witness as a historical discovery.

## Storage is not the interface

This JSON is a reproducible interchange artifact. An implementation may load it into relational storage or use another format while retaining exact IDs, versions and provenance. The user sees a conversation and research cases, not an obligation to upload this JSON or any spreadsheet. Agent evaluation attaches to a case; it is optional for ordinary question answering.
