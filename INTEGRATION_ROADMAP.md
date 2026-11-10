# VARTA external integrations

## Source of truth and safety rules

- GitHub repository `ashubagri/Varta` remains the canonical source of code.
- GitHub Pages remains the production host.
- Supabase remains the production authentication and database service.
- Never deploy a GitLab mirror directly to the live site.
- Test changes on a branch and merge to `main` only after the checks pass.
- Do not store passwords, Supabase service-role keys, or personal access tokens in repository files.

## GitLab mirror

GitLab.com supports push mirrors on its Free tier. GitLab pull mirroring from GitHub is a paid-tier feature, so it is not the right free route for a GitHub-first project.

Recommended free-tier design:

1. Create an empty GitLab project named `Varta`.
2. Keep GitHub as the only place where code is edited and merged.
3. Add a GitLab project access token with the minimum required repository-write permission as a GitHub Actions repository secret named `GITLAB_MIRROR_TOKEN`.
4. Add a GitHub Actions repository variable named `GITLAB_PROJECT_PATH`, with the GitLab namespace/project path (for example, `namespace/Varta`).
5. Add a guarded GitHub Actions job that mirrors only the `main` branch to GitLab after the validation job succeeds.
6. Never make changes directly in the GitLab mirror. It is a secondary copy, not the source of truth.

The mirror job should remain disabled until the destination project and secret/variable are configured. Do not place tokens in this file or in workflow YAML.

Official documentation: https://docs.gitlab.com/user/project/repository/mirror/

## Stack Exchange knowledge discovery

Use the Stack Exchange API as a discovery aid, not as an unquestioned source of truth.

Potential VARTA areas:
- Physics and acoustics for Sound & NADA.
- Computer Science and Artificial Intelligence for Science & Technology.
- Mathematics for quantitative explainers.
- Philosophy and Hinduism for Indian Knowledge discussions.

Editorial rules:
- Retrieve only questions relevant to a specific VARTA topic.
- Prefer well-scored, well-supported answers, but independently verify important claims.
- Show the original question title, author, Stack Exchange site, date, and link when displaying material.
- Do not copy answers wholesale into VARTA.
- Respect the applicable Creative Commons Attribution-ShareAlike licence and the Stack Exchange attribution requirements.
- Clearly separate established evidence, interpretation, and personal opinion.

Useful official references:
- API documentation: https://api.stackexchange.com/
- Question search: https://api.stackexchange.com/docs/search
- Content licensing: https://stackoverflow.com/help/licensing

## Current implementation status

- [x] Isolated development branch created: `integration/quality-checks`.
- [x] Static-site validation script added at `tools/check_site.py`.
- [x] GitHub Actions workflow added at `.github/workflows/site-checks.yml`.
- [x] First workflow run passed on the development branch.
- [ ] Review and merge the quality-check branch into `main`.
- [ ] Create the GitLab destination project and configure the protected mirror secret/variable.
- [ ] Add and test the optional GitHub-to-GitLab mirror job.
- [ ] Design a small Stack Exchange topic-discovery prototype; keep it separate from production content until editorial review.
