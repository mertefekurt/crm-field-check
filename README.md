<img src="assets/readme-cover.svg" alt="Crm Field Check cover" width="100%" />

# Crm Field Check

Audit CRM fields for PII, ownership, and stale custom fields.

![stack](https://img.shields.io/badge/stack-Python-dc2626?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-7c3aed?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-0891b2?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-b45309?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `crm-field-check` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `pii-field` | high | PII field detected |
| `unknown-owner` | medium | field owner missing |
| `stale-field` | low | field may be stale |

## Command line

```bash
python -m pip install -e ".[dev]"
crm-field-check examples/sample.txt
crm-field-check examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
field personal_email pii true owner unknown last_used 2023
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
