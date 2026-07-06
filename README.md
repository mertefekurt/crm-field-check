# Crm Field Check

Audit CRM fields for PII, ownership, and stale custom fields. This repo keeps the work close to the terminal: clear input, predictable output, and no service to babysit.

<img src="assets/readme-cover.svg" alt="Crm Field Check cover" width="100%" />

## Review checklist

- [ ] PII field detected (`pii-field`, high)
- [ ] field owner missing (`unknown-owner`, medium)
- [ ] field may be stale (`stale-field`, low)

## Command path

```bash
git clone https://github.com/mertefekurt/crm-field-check.git
cd crm-field-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
crm-field-check examples/sample.txt
crm-field-check examples/sample.txt --json
```

## Fixture worth keeping

```text
field personal_email pii true owner unknown last_used 2023
```

## Files I look at first

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
