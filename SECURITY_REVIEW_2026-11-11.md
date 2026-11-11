# VARTA security and operational review

**Review date:** 11 November 2026  
**Scope:** Read-only review of the connected Supabase project, repository configuration, key browser pages, and public GitHub Pages endpoints.  
**Important:** This is a limited technical review, not a penetration test, legal review, or certification.

## Executive result

The basic database access controls are in place, but one Supabase Auth security recommendation remains unresolved. The application should continue to be treated as an early-stage service until real-account and abuse-flow testing is completed.

## Verified positive controls

- Row Level Security is enabled on all 14 tables in the `public` schema.
- The public schema does not grant CREATE to `anon`, `authenticated`, or PUBLIC.
- The video storage bucket `varta-videos` is private and accepts only MP4, WebM, and QuickTime video MIME types, with a 50 MiB object limit.
- Video object policies scope uploads and updates to the authenticated member's own folder. Read access is linked to a published video, its owner, or a moderator.
- Moderator checks are enforced through the database's `moderators` table and RLS policies; a browser-side check alone is not the authorization boundary.
- The video moderation Edge Function validates the caller's session and checks that the submission belongs to that caller before processing it.
- The text moderation Edge Function requires a valid signed-in user and fails closed when moderation cannot complete.
- The browser Supabase client contains a publishable key, not a service-role key. A publishable key is expected to be public; RLS is the critical protection.
- Reviewed browser pages build user-facing text with DOM text nodes / `textContent`; no `innerHTML`, `insertAdjacentHTML`, or `document.write` assignment was found in the sampled pages.
- HTTPS is enabled at the database level.
- Supabase health advisor returned no current findings.
- The live homepage, login, posts, moderation, and editorial pages were reachable during this review. The public sitemap listed 51 URLs, and `robots.txt` referenced it.
- GitHub Actions site validation passed on the merged `main` commit. GitHub-to-GitLab mirror workflow runs also completed successfully.

## Findings requiring attention

### 1. Enable leaked-password protection

Supabase Security Advisor reports `auth_leaked_password_protection` as disabled. Enable leaked-password protection in Supabase Auth password/security settings. This check uses the Have I Been Pwned compromised-password corpus.

Reference: https://supabase.com/docs/guides/auth/password-security#password-strength-and-leaked-password-protection

This setting was not changed during this review because the available project connection does not expose the Auth dashboard setting.

### 2. Complete real-account acceptance tests

The following flows cannot be fully validated without interacting with real user accounts and email inboxes:

- Registration and email confirmation.
- Sign-in, sign-out, and password recovery.
- Profile creation, username uniqueness, and profile edits.
- Creating posts and replies, likes, follows, reposts, and notifications.
- Member reports and moderator-only report handling.
- Knowledge suggestions, moderator review, draft saving, publication, and archive flows.
- Video upload, private object access, moderation success, moderation failure, and retry.

Use at least two ordinary member accounts and one moderator account. Do not use real private user data for test content.

### 3. Review privacy disclosures before inviting a large audience

The product uses Supabase Auth and database storage, Google Translate scripts, and an external translation endpoint for user-requested translations. Review the privacy notice so it accurately explains the data collected, third-party services, retention/deletion contact, and user rights applicable to the service.

### 4. Revisit unused indexes only after real usage

Supabase Performance Advisor currently reports 10 unused indexes. This is informational, not proof that they should be dropped. Keep them until real query patterns and a sufficient observation period establish that removal is safe.

## Scope limitations

- No real account was created, signed in, or modified.
- No email was sent.
- No production database rows, RLS policies, schema, storage objects, or Auth settings were changed.
- No attempt was made to bypass authentication or attack the live service.
- Frontend source review sampled key community and moderation pages; it is not a complete manual audit of every page or dependency.
- The live page fetch confirms that pages respond, not that every interactive control works in a real browser.

## Recommended release gate

Before public promotion, complete the real-account acceptance tests, enable leaked-password protection, review the privacy notice, and repeat the Supabase security advisor scan. Keep GitHub as the canonical source and GitLab as a backup mirror.
