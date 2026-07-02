# crm-field-check

> Audit CRM fields for PII, ownership, and stale custom fields.

## Workflow Overview

Audit CRM fields for PII, ownership, and stale custom fields. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 28

Accepts CRM field inventory. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 28

```bash
python -m pip install -e ".[dev]"
crm-field-check examples/sample.txt
crm-field-check examples/sample.txt --json --fail-on medium
python -m crm_field_check --help
```

## Rule Surface 28

| Rule | Severity | Meaning |
|---|---:|---|
| `pii-field` | high | PII field detected |
| `unknown-owner` | medium | field owner missing |
| `stale-field` | low | field may be stale |

## Validation Notes 28

```bash
ruff check .
pytest
python -m crm_field_check --help
```

Example risky input:

```text
field personal_email pii true owner unknown last_used 2023
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
