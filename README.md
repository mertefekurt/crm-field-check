# Crm Field Check

![Crm Field Check cover](assets/readme-cover.svg)

Audit CRM fields for PII, ownership, and stale custom fields.

`Python`

## Start here

```bash
git clone https://github.com/mertefekurt/crm-field-check.git
cd crm-field-check
python -m pip install -e ".[dev]"
crm-field-check examples/sample.txt
```

## Project map

```text
risky: field personal_email pii true owner unknown last_used 2023
clean: field plan_name pii false owner salesops last_used 2026
```

## Repository

[Open the source on GitHub →](https://github.com/mertefekurt/crm-field-check)

[MIT License](LICENSE)
