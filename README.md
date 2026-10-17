# VARTA — India's Knowledge & Conversation Network

**VARTA** is an early-stage Indian community platform for sharing ideas and having thoughtful conversations about science, Indian knowledge, sound and NADA, culture, nature, and world affairs.

🌐 **Live site:** https://ashubagri.github.io/Varta/  
🔎 **Search:** https://ashubagri.github.io/Varta/search.html  
👥 **Discover members:** https://ashubagri.github.io/Varta/discover.html  
💬 **Community posts:** https://ashubagri.github.io/Varta/posts.html  
🔐 **Join or sign in:** https://ashubagri.github.io/Varta/login.html

## Project goals

- Give people a simple place to publish posts and discuss ideas.
- Help members discover profiles, follow people and find conversations.
- Encourage respectful, useful and evidence-aware public discussion.
- Explore science, Indian knowledge, sound, culture, nature and world affairs in one community.
- Build a foundation that can grow responsibly with member feedback.

## Current features

The repository currently includes a static web frontend hosted with GitHub Pages and uses Supabase for authentication and persistent community data.

- Email registration, sign-in and password-reset request flow.
- Member profiles with display names, usernames and bios.
- Community posts and a following feed.
- Likes, replies and reposts.
- Follow and unfollow controls.
- Member discovery and keyword search across profiles and posts.
- Activity and notification pages.
- Member reporting for posts, replies, and profiles, with private report records and a documented owner review workflow (`MODERATION.md`).
- Responsive page layouts and shared navigation.

This is an evolving project. Feature availability and production readiness should be verified as development continues; this README is not a claim of a completed security or accessibility audit.

## Main pages and files

- `index.html` — public homepage and project introduction.
- `login.html` — registration, sign-in and password-reset request.
- `posts.html` — community feed and post interactions.
- `profile.html` — signed-in member profile editing.
- `member.html` — public member profile.
- `discover.html` — member directory.
- `search.html` — search for posts and profiles.
- `activity.html` — community activity.
- `notifications.html` — member notifications.
- `js/supabase-client.js` — browser-side Supabase client configuration.
- `css/style.css` — shared styles.

## Technology

- HTML, CSS and browser JavaScript.
- GitHub Pages for static hosting.
- Supabase Auth and PostgreSQL-backed data.

## Contributing

Bug reports, focused feature proposals and code contributions are welcome. Please read:

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing Guidelines](CONTRIBUTING.md)
- [Security Policy](SECURITY.md)
- [Accessibility Statement](ACCESSIBILITY.md)

Use the repository's issue templates to report a reproducible bug or propose an improvement. Never include passwords, tokens, private messages or personal information in public issues.

## Security notes

The frontend uses a Supabase publishable key, which is designed for browser use. Access to data must be enforced by Supabase Row Level Security (RLS) and appropriate policies; a publishable key is not a substitute for access control. Never put a Supabase service-role key, password or other privileged secret in client-side code.

## Project status

VARTA is under active development. Before inviting a larger audience, continue testing registration, account recovery, database permissions, abuse reporting, mobile usability and privacy protections.

## License

No open-source license has been selected for this repository yet. Until a license is added, do not assume that others have permission to reuse, distribute or modify this project's code.