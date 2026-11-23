# VARTA integration and quality roadmap

## Production architecture

- **Canonical source:** GitHub repository `ashubagri/Varta`.
- **Production hosting:** GitHub Pages.
- **Authentication and data:** the existing Supabase project.
- **Secondary backup:** GitLab project `ashubagri/varta`.
- Edit and merge code in GitHub only. Do not deploy the GitLab mirror to production.

## Completed

- [x] GitHub Actions static-site check added for HTML files and local `href`/`src` targets.
- [x] GitLab destination imported from the GitHub repository.
- [x] GitHub Actions mirror workflow configured with the repository secret `GITLAB_MIRROR_TOKEN`.
- [x] GitHub-to-GitLab mirror workflow completed successfully on the `main` branch and on its integration branch.
- [x] Supabase database review confirmed Row Level Security is enabled on all 14 public tables.
- [x] Supabase storage video bucket is private; upload and read policies are scoped to the member's own objects, published objects, or moderators.

## Remaining checks

- [ ] Enable Supabase leaked-password protection in Auth settings and rerun the security advisor. **Plan gate:** the connected Supabase organization is on the Free plan; Supabase documents this feature as Pro and above. Do not mark this complete unless the plan supports it and the advisor warning clears.
- [ ] Test signup, email verification, sign-in, password reset, sign-out, profile save, posts, replies, likes, follows, notifications, reports, and moderator-only pages with real user accounts.
- [ ] Verify video upload, private object access, moderation result handling, and retry behavior with a test account.
- [ ] Connect the Google account with access to the Search Console property in OpenSEO, then submit and inspect the VARTA sitemap in Google Search Console.
- [x] Verify the live sitemap and robots endpoints: `sitemap.xml` returns 50 URLs and `robots.txt` references the project sitemap (2026-11-23).
- [x] Review the static-site check on `main`: workflow run #134 passed (2026-11-18).

## Stack Exchange research integration — design only

Use the Stack Exchange API as a discovery aid, not as an unquestioned source of truth.

Potential areas:
- Physics and acoustics for Sound & NADA.
- Computer Science and Artificial Intelligence for Science & Technology.
- Mathematics for quantitative explainers.
- Philosophy and Hinduism for Indian Knowledge discussions.

Editorial safeguards:
- Independently verify important claims.
- Display original question title, author, Stack Exchange site, date, and link when presenting material.
- Do not copy answers wholesale.
- Follow the applicable Creative Commons licence and Stack Exchange attribution requirements.
- Separate established evidence, traditional interpretation, and personal opinion.

Official references:
- https://api.stackexchange.com/
- https://api.stackexchange.com/docs/search
- https://stackoverflow.com/help/licensing

## Operating rules

- Never put passwords, access tokens, Supabase service-role keys, or other privileged credentials in repository files.
- Keep the GitLab mirror as a backup, not a second development source.
- Do not remove database indexes solely because they are currently unused; collect workload evidence first.
- Do not claim the site is fully production-ready until the real-user checks above are completed.
