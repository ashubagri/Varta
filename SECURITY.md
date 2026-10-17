# VARTA Security Policy

## Reporting a vulnerability

Please do not publish exploitable security details, credentials, personal data or attack instructions in a public issue.

Use GitHub's private vulnerability reporting feature for this repository if it is enabled. If it is not available, contact the repository owner privately through a contact method listed on their GitHub profile and include:

- A concise description of the issue and its potential impact.
- The affected page, endpoint or component.
- Reproduction steps and a safe proof of concept, if available.
- Any suggested mitigation.

Please do not access, modify, download or disclose other people's data while investigating a suspected issue.

## Scope and priorities

Reports involving authentication bypass, unauthorized access to private data, broken access controls, exposed privileged credentials, injection, cross-site scripting or serious privacy leaks are especially important.

## Response

The maintainer will make a reasonable effort to acknowledge a report, investigate it and coordinate a fix. Response and remediation times depend on severity, reproducibility and maintainer availability. Please allow time to investigate before public disclosure.

## Secrets

Never place passwords, session tokens, Supabase service-role keys or other private credentials in source code, issues, pull requests or screenshots. If a secret is exposed, revoke or rotate it immediately.
