# github-pi-sandbox

Test playground for the **github-pi** automation system.

This repo is intentionally simple — it exists so the github-pi agent can:
- Be triaged on issue open (auto-label)
- Auto-fix issues when labeled `gp:auto-fix`
- Receive automated PR review when labeled `gp:review`
- Be auto-merged when configured in the allowlist

**Do not put real code here.** Everything is disposable.

## Files

- `src/calculator.py` — small intentionally-buggy module for issue-fix tests
- `src/__init__.py` — package marker

## Trigger labels

| Label | Effect |
|---|---|
| `gp:auto-fix` | Agent attempts to fix the issue and opens a PR |
| `gp:review` | Agent reviews an open PR and posts comments |
| `gp:declined` | Issue is closed |
