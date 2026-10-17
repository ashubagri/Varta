# Contributing to VARTA

Thank you for helping improve VARTA, India's knowledge and conversation network.

## Ways to contribute

- Report a reproducible bug.
- Suggest a focused feature or accessibility improvement.
- Improve documentation, wording or translations.
- Submit a code change that is small, tested and easy to review.

## Before opening an issue

1. Search existing issues to avoid duplicates.
2. Describe what you expected and what actually happened.
3. Include the page URL, browser/device and clear reproduction steps.
4. Never include passwords, access tokens, private user information or other secrets.

## Before submitting a pull request

1. Keep the change focused and explain why it is useful.
2. Test affected pages at desktop and mobile sizes.
3. Check browser-console errors and verify navigation links.
4. Do not commit secrets, service-role keys, private data or local environment files.
5. Preserve existing functionality and follow the current HTML, CSS and JavaScript conventions.
6. Update documentation when behaviour or setup changes.

## Security and privacy

VARTA uses Supabase for authentication and data. Never put Supabase service-role keys or other privileged credentials in browser code. Client-side publishable keys are not a substitute for database row-level security (RLS). Any database or policy change should be reviewed for access control.

Please report suspected vulnerabilities privately as described in [SECURITY.md](SECURITY.md), not in a public issue.

## Review

Maintainers may request changes, ask for tests, or close contributions that are unsafe, out of scope, duplicative or inconsistent with VARTA's goals. A contribution is not considered accepted until it is merged by a maintainer.
