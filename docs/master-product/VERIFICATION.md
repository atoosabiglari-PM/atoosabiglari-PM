# Design package verification

Checked November 15, 2026.

## Passed

- JSON Schema Draft 2020-12 metaschema validation.
- Synthetic case structural validation with date-time and URI format checks.
- Real SHA-256 checks against all referenced synthetic fixture bytes.
- RFC 8785 precondition digest recomputation.
- ChronicleGraph source fingerprint and JSON Pointer resolution.
- Thirteen negative mutations rejected: untrusted auth_verified field, missing executor, missing identity assignment, changed identity assignment, malformed digest, changed target, changed artifact, changed policy, approval without proof fields, synthetic execution claim, negative count, case-ID mismatch and duplicate domain component.

Reproduce with the pinned validation requirements and validate_contract.py.

## Not established by these checks

Real authentication, signature validation, live permission expiry/revocation, runtime action enforcement, storage race handling, independent effect observation and an end-to-end six-component workflow. Those require the implementation tests in ACCEPTANCE.md.

The component interface audit is a read-only source inspection at the commits recorded in INTERFACE_AUDIT.md. Their full test suites and hosted services were not rerun for this planning package. The original Gemma experiment was not rerun or expanded.
