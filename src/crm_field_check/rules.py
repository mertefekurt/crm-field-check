from __future__ import annotations

from crm_field_check.models import Rule

PROJECT_NAME = 'crm-field-check'
SUMMARY = 'Audit CRM fields for PII, ownership, and stale custom fields.'
SAMPLE_RISK = 'field personal_email pii true owner unknown last_used 2023'
SAMPLE_CLEAN = 'field plan_name pii false owner salesops last_used 2026'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='pii-field',
        severity='high',
        pattern='pii\\s+true',
        message='PII field detected',
        recommendation='review access and retention',
    ),
    Rule(
        code='unknown-owner',
        severity='medium',
        pattern='owner\\s+(unknown|none|missing)',
        message='field owner missing',
        recommendation='assign owner',
    ),
    Rule(
        code='stale-field',
        severity='low',
        pattern='last_used\\s+20(1[0-9]|2[0-4])',
        message='field may be stale',
        recommendation='archive or confirm need',
    ),
)
