# Optional governed data repair and export workflow

This is an optional DataReady-led workflow within the conversational platform. It is no longer the first integrated pilot or a prerequisite for asking questions, supplying evidence, or evaluating an agent.

Retained assets: source-preserving repair proposals, independent checks, approval bindings, the CaseRecord 0.1.2 export schema, synthetic fixtures, offline validator, idempotency, revocation ordering and uncertain-outcome handling. None establishes a working integrated platform.

- [Current master plan](../../README.md)
- [Export contract](CONTRACT.md)
- [Export acceptance scenarios](ACCEPTANCE.md)
- [Retained export JSON schema](../../case-record.schema.json)
- [Synthetic example](../../examples/case-awaiting-approval.json)
- [Offline validator](../../validate_contract.py)
- [Original version 1.1 plan, preserved in Git history](https://github.com/atoosabiglari-PM/atoosabiglari-PM/blob/d41ee7f453ca9b1b6a39983e009751d14a239d5d/docs/master-product/README.md)

The files remain in their existing paths so the offline validator and fixture references keep working. This export-specific schema does not model the research workspace. Production credentials, real personal data and external exports require their own authorization and deployment tests.

## Preserved runtime protocol

The following design was selected for the optional export workflow. Its 2 MiB CSV artifact limit applies only here. Neither this destination nor a same-database transaction is required to ask a research question. The graph writer/reader described here is a reusable primitive, not the complete ChronicleGraph research brain.


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

