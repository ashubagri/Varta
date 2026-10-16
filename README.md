# VARTA — India's Knowledge & Conversation Network

This repository contains a lightweight, mobile-first prototype of VARTA — a public conversation and knowledge-sharing platform for India.

## Included pages
- `index.html`
- `science.html`
- `indian-knowledge.html`
- `sound-nada.html`
- `culture-nature.html`
- `world-affairs.html`
- `posts.html`
- `submit.html`
- `css/style.css`

## How to publish with GitHub Pages
1. Go to repository Settings → Pages.
2. Under "Source", select the `main` branch and the root folder `/` if using a single-page static site.
3. Save.
4. Your site will be available at:
   `https://<your-username>.github.io/varta/`

## Replace the placeholders
- Replace the YouTube sample embed in `index.html` and `sound-nada.html` with a real Hydrogen Awakening video.
- Replace the Google Form placeholder in `submit.html` with your real Google Form embed.

## Next steps
This is a prototype meant to test demand. The next stage would be user accounts, feeds, comments, and messaging.

## License
You own the content and can adapt the project as needed.

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>VARTA — India's Knowledge & Conversation Network</title>
  <meta name="description" content="VARTA — short posts, public discussion and knowledge sharing for science, culture, sound and world affairs." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container">
      <a class="brand" href="index.html">VARTA</a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science & Technology</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture & Nature</a>
        <a href="world-affairs.html">World Affairs</a>
        <a href="posts.html">Posts</a>
      </nav>
    </div>
  </header>

  <main class="container">
    <section class="hero">
      <h1>VARTA</h1>
      <p class="tagline">India's Knowledge & Conversation Network</p>
      <p class="lead">Short posts · Public discussion · Science, sound and culture</p>
    </section>

    <section class="grid">
      <article class="card">
        <h2>About VARTA</h2>
        <p>VARTA is a lightweight, mobile-first prototype for public conversation and knowledge sharing. The purpose is to build a digital community for science, Indian knowledge, sound, culture and public ideas.</p>
      </article>

      <article class="card">
        <h2>Get involved</h2>
        <p>Share ideas, short posts or article proposals using the submission form. We review and publish selected contributions.</p>
        <p><a class="cta" href="submit.html">Submit an idea or post</a></p>
      </article>

      <article class="card wide-card">
        <h2>NADA — Sound & Video</h2>
        <p>Featured content from Hydrogen Awakening. Replace the sample video below with a chosen YouTube link from your channel.</p>
        <div class="video-wrap">
          <iframe width="100%" height="315" src="https://www.youtube.com/embed/VIDEO_ID" title="NADA sample video" frameborder="0" allowfullscreen></iframe>
        </div>
      </article>

      <article class="card">
        <h2>Community</h2>
        <p>We are starting small. Invite friends and early users, test what people want, and learn what features matter most.</p>
      </article>
    </section>

    <section class="latest">
      <h2>Latest posts</h2>
      <ul class="posts-list">
        <li><a href="posts.html#post-1">Why Sound Matters — NADA & Hydrogen Awakening</a><span class="muted">sample</span></li>
        <li><a href="posts.html#post-2">Vedic Ideas and Modern Science</a><span class="muted">sample</span></li>
      </ul>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>VARTA — Prototype</p>
    </div>
  </footer>
</body>
</html>

<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sound & NADA — VARTA</title>
  <meta name="description" content="NADA, sound, vibration and media on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>Sound & NADA</h1>
      <p>Ragas, mantras, music, vibration and the study of resonance — from sound science to spiritual practice.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured audio/video</h2>
      <div class="video-wrap">
        <iframe src="https://www.youtube.com/embed/VIDEO_ID" title="Featured NADA video" allowfullscreen></iframe>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>

<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Culture & Nature — VARTA</title>
  <meta name="description" content="Culture and nature on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>Culture & Nature</h1>
      <p>Local landscapes, artistic traditions, memory, rituals, seasons and a deeper relationship with the natural world.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured story</h2>
      <p>Use this section for visual storytelling, photo essays, and discussion about the living culture of Bharat.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>

<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>World Affairs — VARTA</title>
  <meta name="description" content="World affairs and geopolitics on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>World Affairs</h1>
      <p>Public debate and analysis on geopolitics, energy, power, migration, climate and the global system.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured reading</h2>
      <p>Use this page for geopolitical analysis, cross-country frameworks or summaries of global trends and energy policy.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>

#!/usr/bin/env bash
set -euo pipefail

# Automated deploy script for ashubagri/Varta
# Usage:
#   Copy-paste and run:
#     GITHUB_TOKEN=ghp_xxx bash deploy-varta.sh
# Optional env overrides:
#   VIDEO_ID (default gZvnhESKWBA)
#   GOOGLE_FORM_IFRAME (HTML iframe string; leave empty to keep placeholder)
REPO_OWNER="ashubagri"
REPO_NAME="Varta"
REPO_URL="https://github.com/${REPO_OWNER}/${REPO_NAME}.git"
BRANCH="main"
LOCAL_DIR="varta-deploy-$$"
VIDEO_ID="${VIDEO_ID:-gZvnhESKWBA}"
GOOGLE_FORM_IFRAME="${GOOGLE_FORM_IFRAME:-}"
GITHUB_TOKEN="${GITHUB_TOKEN:-}"

if ! command -v git >/dev/null 2>&1; then
  echo "git is required. Install git and retry." >&2
  exit 1
fi
if ! command -v curl >/dev/null 2>&1; then
  echo "curl is required. Install curl and retry." >&2
  exit 1
fi

echo "Cloning repository ${REPO_URL}..."
rm -rf "$LOCAL_DIR"
git clone "$REPO_URL" "$LOCAL_DIR"
cd "$LOCAL_DIR"

if git show-ref --verify --quiet "refs/heads/${BRANCH}"; then
  git checkout "${BRANCH}"
else
  git checkout -b "${BRANCH}"
fi

mkdir -p css assets

cat > index.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>VARTA — India’s Knowledge & Conversation Network</title>
  <meta name="description" content="VARTA is a premium digital platform for science, Indian knowledge, sound, culture and world affairs." />
  <meta property="og:title" content="VARTA — India’s Knowledge & Conversation Network" />
  <meta property="og:description" content="A premium public conversation and knowledge platform for India." />
  <meta property="og:type" content="website" />
  <meta name="theme-color" content="#d97706" />
  <link rel="manifest" href="manifest.json" />
  <link rel="shortcut icon" href="assets/logo.svg" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand" aria-label="VARTA home">
        <img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" />
        <span>VARTA</span>
      </a>
      <nav class="main-nav" aria-label="Main navigation">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
        <a href="posts.html">Posts</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-copy">
          <span class="eyebrow">Bharat Digital Universe</span>
          <h1>VARTA</h1>
          <p class="tagline">India’s Knowledge & Conversation Network</p>
          <p class="lead">A premium platform for public discussion, knowledge sharing, sound, wellness, science, culture and modern ideas rooted in Indian wisdom.</p>
          <div class="cta-row">
            <a href="submit.html" class="button primary">Submit a post</a>
            <a href="posts.html" class="button secondary">Read posts</a>
          </div>
          <ul class="stats">
            <li><strong>Science</strong><span>Research & discourse</span></li>
            <li><strong>NADA</strong><span>Sound & vibration</span></li>
            <li><strong>Culture</strong><span>Art & identity</span></li>
          </ul>
        </div>

        <div class="hero-panel">
          <div class="panel-header">
            <span class="dot dot-one"></span>
            <span class="dot dot-two"></span>
            <span class="dot dot-three"></span>
          </div>
          <div class="panel-card">
            <span class="mini-label">Featured topic</span>
            <h3>Hydrogen Awakening</h3>
            <p>Sound, science, energy, nature and wisdom in conversation.</p>
            <a href="posts.html#post-1">Explore the idea</a>
          </div>
          <div class="panel-list">
            <div><span>Public conversation</span><strong>VARTA</strong></div>
            <div><span>Sound & video</span><strong>NADA</strong></div>
            <div><span>Creative culture</span><strong>Drishti</strong></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section container">
      <div class="section-header">
        <span class="eyebrow dark">What we build</span>
        <h2>Public knowledge for a new digital Bharat</h2>
      </div>
      <div class="grid three-up">
        <article class="card">
          <div class="icon">S</div>
          <h3>Science & technology</h3>
          <p>Discussion, discoveries and critical thinking on modern science, climate, energy and innovation.</p>
          <a href="science.html">Explore</a>
        </article>

        <article class="card">
          <div class="icon">K</div>
          <h3>Indian knowledge</h3>
          <p>Essays, learning and contemporary interpretation of Sanskrit, philosophy, rituals and memory traditions.</p>
          <a href="indian-knowledge.html">Explore</a>
        </article>

        <article class="card">
          <div class="icon">N</div>
          <h3>Sound & NADA</h3>
          <p>Ragas, mantras, vibration, sound healing, meditation and the science of resonance.</p>
          <a href="sound-nada.html">Explore</a>
        </article>
      </div>
    </section>

    <section class="section feature-band">
      <div class="container feature-grid">
        <div>
          <span class="eyebrow dark">Featured content</span>
          <h2>NADA — sound, resonance and media</h2>
          <p>We begin with the idea that sound is a bridge between ancient wisdom and modern science. VARTA offers a space for this conversation, including video, music and essays.</p>
        </div>
        <div class="feature-video">
          <iframe src="https://www.youtube.com/embed/${VIDEO_ID}" title="Featured NADA video" allowfullscreen></iframe>
        </div>
      </div>
    </section>

    <section class="section container">
      <div class="section-header">
        <span class="eyebrow dark">Latest on VARTA</span>
        <h2>Fresh thinking from the community</h2>
      </div>
      <div class="grid two-up">
        <article class="post-card">
          <div class="post-tag">Science</div>
          <h3><a href="posts.html#post-1">Why Sound Matters — NADA & Hydrogen Awakening</a></h3>
          <p>Sound explains more than music. It may reveal a deeper way to understand energy, consciousness and culture.</p>
        </article>

        <article class="post-card">
          <div class="post-tag">Knowledge</div>
          <h3><a href="posts.html#post-2">Vedic Ideas and Modern Science</a></h3>
          <p>When tradition and evidence speak to each other, new forms of understanding can emerge.</p>
        </article>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <a href="index.html" class="brand small-brand">
          <img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" />
          <span>VARTA</span>
        </a>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="science.html">Science</a></li>
          <li><a href="indian-knowledge.html">Indian Knowledge</a></li>
          <li><a href="sound-nada.html">NADA</a></li>
        </ul>
      </div>
      <div>
        <h4>Community</h4>
        <ul>
          <li><a href="posts.html">Posts</a></li>
          <li><a href="submit.html">Submit</a></li>
          <li><a href="mailto:hello@varta.example">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Newsletter</h4>
        <form class="newsletter-form">
          <input type="email" placeholder="Email address" aria-label="Email" />
          <button type="submit">Join</button>
        </form>
      </div>
    </div>
    <div class="container legal-line">
      <span>© 2026 VARTA Prototype</span>
      <span><a href="#">Privacy</a> · <a href="#">Terms</a></span>
    </div>
  </footer>

  <script src="sw.js"></script>
</body>
</html>
EOF

cat > sound-nada.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sound & NADA — VARTA</title>
  <meta name="description" content="NADA, sound, vibration and media on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>Sound & NADA</h1>
      <p>Ragas, mantras, music, vibration and the study of resonance — from sound science to spiritual practice.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured audio/video</h2>
      <div class="video-wrap">
        <iframe src="https://www.youtube.com/embed/${VIDEO_ID}" title="Featured NADA video" allowfullscreen></iframe>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

cat > culture-nature.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Culture & Nature — VARTA</title>
  <meta name="description" content="Culture and nature on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>Culture & Nature</h1>
      <p>Local landscapes, artistic traditions, memory, rituals, seasons and a deeper relationship with the natural world.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured story</h2>
      <p>Use this section for visual storytelling, photo essays, and discussion about the living culture of Bharat.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

cat > world-affairs.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>World Affairs — VARTA</title>
  <meta name="description" content="World affairs and geopolitics on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>World Affairs</h1>
      <p>Public debate and analysis on geopolitics, energy, power, migration, climate and the global system.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured reading</h2>
      <p>Use this page for geopolitical analysis, cross-country frameworks or summaries of global trends and energy policy.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

cat > posts.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Posts — VARTA</title>
  <meta name="description" content="Latest posts on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Latest</span>
      <h1>Posts</h1>
    </div>

    <div class="grid two-up">
      <article class="post-card" id="post-1">
        <span class="post-tag">Science</span>
        <h2><a href="#">Why Sound Matters — NADA & Hydrogen Awakening</a></h2>
        <p>Sound is more than music. It links vibration, creativity, consciousness and the deeper structure of reality.</p>
      </article>

      <article class="post-card" id="post-2">
        <span class="post-tag">Knowledge</span>
        <h2><a href="#">Vedic Ideas and Modern Science</a></h2>
        <p>When ancient systems of thought meet scientific inquiry, new meaning opens up.</p>
      </article>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

if [ -n "$GOOGLE_FORM_IFRAME" ]; then
cat > submit.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Submit — VARTA</title>
  <meta name="description" content="Submit an idea or post to VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="posts.html">Posts</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Contribute</span>
      <h1>Submit an idea or post</h1>
      <p>Share a new idea, article proposal, short essay or community note.</p>
    </div>

    <article class="card detail-card">
      <h2>Submission form</h2>
      ${GOOGLE_FORM_IFRAME}
      <p class="submit-links">
        <a href="mailto:hello@varta.example" class="button primary">Email submission</a>
      </p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF
else
cat > submit.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Submit — VARTA</title>
  <meta name="description" content="Submit an idea or post to VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="posts.html">Posts</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Contribute</span>
      <h1>Submit an idea or post</h1>
      <p>Share a new idea, article proposal, short essay or community note.</p>
    </div>

    <article class="card detail-card">
      <h2>Submission form placeholder</h2>
      <p>Paste a Google Form embed or direct link here to collect user submissions.</p>
      <div class="submission-box">
        <p>Example Google Form embed placeholder:</p>
        <!-- Paste Google Form iframe here -->
      </div>
      <p class="submit-links">
        <a href="mailto:hello@varta.example" class="button primary">Email submission</a>
      </p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF
fi

cat > css/style.css <<'EOF'
body {
  margin: 0;
  font-family: Inter, Arial, sans-serif;
  background: #fffaf3;
  color: #1d1d1d;
}

img { max-width: 100%; display: block; }

a { color: inherit; }

.container {
  width: min(1180px, calc(100% - 30px));
  margin: 0 auto;
}

.site-header {
  background: linear-gradient(180deg, #0f172a, #101827);
  position: sticky;
  top: 0;
  z-index: 10;
  box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
}

.header-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 78px;
  gap: 20px;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: white;
  font-weight: 800;
  letter-spacing: 0.08em;
  font-size: 1.2rem;
}

.brand-mark {
  width: 32px;
  height: 32px;
  border-radius: 50%;
}

.main-nav {
  display: flex;
  align-items: center;
  gap: 18px;
  flex-wrap: wrap;
  justify-content: flex-end;
}

.main-nav a {
  text-decoration: none;
  color: #e8edf3;
  font-size: 0.92rem;
}

.hero {
  background: radial-gradient(circle at 20% 20%, rgba(217,119,6,0.18), transparent 24%), #fffaf3;
  padding: 72px 0 40px;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 30px;
  align-items: center;
}

.eyebrow {
  display: inline-block;
  font-size: 0.76rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #a75a00;
  font-weight: 700;
}

.eyebrow.dark {
  color: #b45309;
}

.hero h1, .page-intro h1 {
  margin: 12px 0 10px;
  font-size: clamp(2.7rem, 5vw, 5rem);
  line-height: 0.98;
  letter-spacing: -0.06em;
}

.tagline {
  margin: 0 0 16px;
  font-size: 1.25rem;
  color: #4b5563;
}

.lead {
  font-size: 1.08rem;
  line-height: 1.6;
  color: #374151;
  max-width: 620px;
}

.cta-row {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  margin-top: 24px;
}

.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 18px;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  transition: transform 0.2s ease;
}

.button:hover { transform: translateY(-1px); }

.button.primary {
  background: linear-gradient(135deg, #d97706, #efb44a);
  color: white;
}

.button.secondary {
  background: white;
  border: 1px solid rgba(15, 23, 42, 0.08);
  color: #111827;
}

.stats {
  list-style: none;
  display: flex;
  gap: 18px;
  padding: 0;
  margin: 30px 0 0;
  flex-wrap: wrap;
}

.stats li {
  background: rgba(255,255,255,0.8);
  border: 1px solid rgba(15,23,42,0.06);
  border-radius: 14px;
  padding: 16px 18px;
  min-width: 130px;
  display: flex;
  flex-direction: column;
  box-shadow: 0 12px 24px rgba(15, 23, 42, 0.04);
}

.stats strong {
  font-size: 1.1rem;
  margin-bottom: 4px;
}

.stats span {
  font-size: 0.8rem;
  color: #6b7280;
}

.hero-panel {
  background: rgba(255,255,255,0.7);
  border: 1px solid rgba(15,23,42,0.06);
  border-radius: 22px;
  box-shadow: 0 20px 48px rgba(17, 24, 39, 0.08);
  padding: 16px;
}

.panel-header {
  display: flex;
  gap: 8px;
  margin-bottom: 18px;
}

.dot {
  display: inline-block;
  width: 12px;
  height: 12px;
  border-radius: 50%;
}

.dot-one { background: #ff5959; }
.dot-two { background: #fbbf24; }
.dot-three { background: #34d399; }

.panel-card {
  background: linear-gradient(180deg, #ffffff, #fff8ef);
  border-radius: 18px;
  border: 1px solid rgba(15,23,42,0.06);
  padding: 20px;
}

.mini-label {
  color: #a75a00;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 700;
}

.panel-card h3, .card h3, .post-card h2 {
  margin-top: 12px;
  margin-bottom: 10px;
}

.panel-card a {
  color: #b45309;
  font-weight: 700;
  text-decoration: none;
}

.panel-list {
  display: grid;
  gap: 12px;
  margin-top: 18px;
}

.panel-list div {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #fff;
  border: 1px solid rgba(15,23,42,0.06);
  border-radius: 12px;
  padding: 12px 14px;
}

.panel-list span { color: #374151; }

.section {
  padding: 58px 0 28px;
}

.section-header {
  margin-bottom: 24px;
}

.section-header h2 {
  margin: 8px 0 0;
  font-size: clamp(1.7rem, 3vw, 2.5rem);
}

.grid {
  display: grid;
  gap: 20px;
}

.three-up { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.two-up { grid-template-columns: repeat(2, minmax(0, 1fr)); }

.card, .post-card, .detail-card {
  background: white;
  border: 1px solid rgba(15,23,42,0.06);
  border-radius: 18px;
  padding: 22px;
  box-shadow: 0 14px 32px rgba(17, 24, 39, 0.04);
}

.card .icon {
  width: 46px;
  height: 46px;
  border-radius: 14px;
  background: linear-gradient(135deg, #fef3c7, #fed7aa);
  color: #7c2d12;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  margin-bottom: 14px;
}

.card a, .post-card a {
  color: #b45309;
  text-decoration: none;
  font-weight: 700;
}

.feature-band {
  background: linear-gradient(180deg, rgba(255,245,230,0.8), rgba(255,255,255,0.9));
  border-top: 1px solid rgba(15,23,42,0.06);
  border-bottom: 1px solid rgba(15,23,42,0.06);
}

.feature-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
  align-items: center;
}

.feature-video iframe {
  width: 100%;
  min-height: 300px;
  border: 0;
  border-radius: 18px;
}

.post-tag {
  display: inline-block;
  background: #fff7ed;
  border: 1px solid rgba(217,119,6,0.18);
  color: #9a4b00;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 7px 10px;
  border-radius: 999px;
  margin-bottom: 10px;
}

.page-wrap {
  padding: 42px 0 36px;
}

.page-intro {
  padding: 18px 0 12px;
}

.page-intro h1 {
  font-size: clamp(2.3rem, 4vw, 3.8rem);
}

.detail-card {
  margin-top: 14px;
}

.video-wrap {
  margin-top: 12px;
}

.video-wrap iframe {
  width: 100%;
  min-height: 320px;
  border: 0;
  border-radius: 16px;
}

.submission-box {
  margin-top: 18px;
  border: 1px dashed rgba(15,23,42,0.2);
  border-radius: 12px;
  min-height: 180px;
  background: #fffaf3;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  color: #5b6470;
}

.submit-links {
  margin-top: 18px;
}

.site-footer {
  background: #0f172a;
  color: rgba(255,255,255,0.82);
  padding: 32px 0 18px;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.2fr 1fr 1fr 1.4fr;
  gap: 24px;
}

.site-footer h4 {
  color: white;
  margin: 0 0 12px;
}

.site-footer ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 8px;
}

.site-footer a {
  text-decoration: none;
  color: rgba(255,255,255,0.8);
}

.newsletter-form {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.newsletter-form input {
  flex: 1 1 160px;
  min-height: 42px;
  border-radius: 999px;
  border: 1px solid rgba(255,255,255,0.15);
  background: rgba(255,255,255,0.05);
  color: white;
  padding: 0 14px;
}

.newsletter-form button {
  min-height: 42px;
  border: 0;
  border-radius: 999px;
  background: linear-gradient(135deg, #f59e0b, #f97316);
  color: white;
  font-weight: 700;
  padding: 0 16px;
}

.legal-line {
  margin-top: 22px;
  padding-top: 18px;
  border-top: 1px solid rgba(255,255,255,0.08);
  display: flex;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.small-brand {
  font-size: 1.1rem;
}

@media (max-width: 900px) {
  .hero-grid,
  .feature-grid,
  .footer-grid,
  .three-up,
  .two-up {
    grid-template-columns: 1fr;
  }

  .header-wrap {
    flex-direction: column;
    justify-content: center;
    padding: 14px 0;
  }

  .main-nav {
    justify-content: center;
  }
}
EOF

cat > assets/logo.svg <<'EOF'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" role="img" aria-label="VARTA logo">
  <defs>
    <linearGradient id="g1" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
  </defs>
  <rect width="200" height="200" rx="44" fill="#0f172a"/>
  <circle cx="100" cy="100" r="68" fill="none" stroke="url(#g1)" stroke-width="20" opacity="0.95"/>
  <path d="M78 93c0-9 7-16 16-16h26c13 0 22 9 22 22 0 14-10 23-25 26l-19 4c-7 2-13 9-13 16v8h26v12H75v-14c0-13 9-22 19-26l22-7c7-2 11-7 11-13 0-7-5-12-13-12H94c-7 0-13 5-13 12v7h-13v-7z" fill="#fff"/>
</svg>
EOF

cat > manifest.json <<'EOF'
{
  "name": "VARTA",
  "short_name": "VARTA",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#fffaf3",
  "theme_color": "#d97706",
  "description": "VARTA — India's Knowledge & Conversation Network",
  "icons": [
    { "src": "assets/logo.svg", "sizes": "any", "type": "image/svg+xml" }
  ]
}
EOF

cat > sw.js <<'EOF'
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('varta-cache-v1').then((cache) => cache.addAll([
      './',
      './index.html',
      './css/style.css',
      './assets/logo.svg'
    ]))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => response || fetch(event.request))
  );
});
EOF

git add -A
git commit -m "Add site pages, assets, and embed featured video (ID: ${VIDEO_ID})" || true
git push origin "${BRANCH}"

if [ -z "$GITHUB_TOKEN" ]; then
  echo "Warning: GITHUB_TOKEN is empty. To enable Pages automatically, re-run with GITHUB_TOKEN set to a PAT with repo scope:"
  echo "  GITHUB_TOKEN=ghp_xxx bash deploy-varta.sh"
  echo "Files have been pushed. Enable Pages manually: Settings → Pages → Deploy from a branch → Branch: main, Folder: /"
  echo "Expected site URL: https://${REPO_OWNER}.github.io/${REPO_NAME}/"
  exit 0
fi

echo "Enabling GitHub Pages via API..."
API_URL="https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/pages"
RESP=$(curl -sS -X PUT -H "Authorization: token ${GITHUB_TOKEN}" -H "Accept: application/vnd.github+json" "${API_URL}" -d '{"source":{"branch":"main","path":"\/"}}')
if echo "$RESP" | grep -q '"message"'; then
  echo "Pages API response:"
  echo "$RESP"
fi

echo "Deployment complete. Check Settings → Pages for the published URL or visit:"
echo "https://${REPO_OWNER}.github.io/${REPO_NAME}/"

#!/usr/bin/env bash
set -euo pipefail

REPO_OWNER="ashubagri"
REPO_NAME="Varta"
REPO_URL="https://github.com/${REPO_OWNER}/${REPO_NAME}.git"
BRANCH="main"
LOCAL_DIR="varta-deploy-$$"
VIDEO_ID="${VIDEO_ID:-gZvnhESKWBA}"
GOOGLE_FORM_IFRAME="${GOOGLE_FORM_IFRAME:-}"
GITHUB_TOKEN="${GITHUB_TOKEN:-}"

if ! command -v git >/dev/null 2>&1; then echo "git not found"; exit 1; fi
if ! command -v curl >/dev/null 2>&1; then echo "curl not found"; exit 1; fi

rm -rf "$LOCAL_DIR"
git clone "$REPO_URL" "$LOCAL_DIR"
cd "$LOCAL_DIR"

if git show-ref --verify --quiet "refs/heads/${BRANCH}"; then
  git checkout "${BRANCH}"
else
  git checkout -b "${BRANCH}"
fi

mkdir -p css assets

cat > index.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>VARTA — India’s Knowledge & Conversation Network</title>
  <meta name="description" content="VARTA is a premium digital platform for science, Indian knowledge, sound, culture and world affairs." />
  <meta name="theme-color" content="#d97706" />
  <link rel="manifest" href="manifest.json" />
  <link rel="shortcut icon" href="assets/logo.svg" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand" aria-label="VARTA home">
        <img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" />
        <span>VARTA</span>
      </a>
      <nav class="main-nav" aria-label="Main navigation">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
        <a href="posts.html">Posts</a>
      </nav>
    </div>
  </header>

  <main>
    <section class="hero">
      <div class="container hero-grid">
        <div class="hero-copy">
          <span class="eyebrow">Bharat Digital Universe</span>
          <h1>VARTA</h1>
          <p class="tagline">India’s Knowledge & Conversation Network</p>
          <p class="lead">A premium platform for public discussion, knowledge sharing, sound, wellness, science, culture and modern ideas rooted in Indian wisdom.</p>
          <div class="cta-row">
            <a href="submit.html" class="button primary">Submit a post</a>
            <a href="posts.html" class="button secondary">Read posts</a>
          </div>
          <ul class="stats">
            <li><strong>Science</strong><span>Research & discourse</span></li>
            <li><strong>NADA</strong><span>Sound & vibration</span></li>
            <li><strong>Culture</strong><span>Art & identity</span></li>
          </ul>
        </div>

        <div class="hero-panel">
          <div class="panel-header">
            <span class="dot dot-one"></span>
            <span class="dot dot-two"></span>
            <span class="dot dot-three"></span>
          </div>
          <div class="panel-card">
            <span class="mini-label">Featured topic</span>
            <h3>Hydrogen Awakening</h3>
            <p>Sound, science, energy, nature and wisdom in conversation.</p>
            <a href="posts.html#post-1">Explore the idea</a>
          </div>
          <div class="panel-list">
            <div><span>Public conversation</span><strong>VARTA</strong></div>
            <div><span>Sound & video</span><strong>NADA</strong></div>
            <div><span>Creative culture</span><strong>Drishti</strong></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section container">
      <div class="section-header">
        <span class="eyebrow dark">What we build</span>
        <h2>Public knowledge for a new digital Bharat</h2>
      </div>
      <div class="grid three-up">
        <article class="card">
          <div class="icon">S</div>
          <h3>Science & technology</h3>
          <p>Discussion, discoveries and critical thinking on modern science, climate, energy and innovation.</p>
          <a href="science.html">Explore</a>
        </article>

        <article class="card">
          <div class="icon">K</div>
          <h3>Indian knowledge</h3>
          <p>Essays, learning and contemporary interpretation of Sanskrit, philosophy, rituals and memory traditions.</p>
          <a href="indian-knowledge.html">Explore</a>
        </article>

        <article class="card">
          <div class="icon">N</div>
          <h3>Sound & NADA</h3>
          <p>Ragas, mantras, vibration, sound healing, meditation and the science of resonance.</p>
          <a href="sound-nada.html">Explore</a>
        </article>
      </div>
    </section>

    <section class="section feature-band">
      <div class="container feature-grid">
        <div>
          <span class="eyebrow dark">Featured content</span>
          <h2>NADA — sound, resonance and media</h2>
          <p>We begin with the idea that sound is a bridge between ancient wisdom and modern science. VARTA offers a space for this conversation, including video, music and essays.</p>
        </div>
        <div class="feature-video">
          <iframe src="https://www.youtube.com/embed/${VIDEO_ID}" title="Featured NADA video" allowfullscreen></iframe>
        </div>
      </div>
    </section>

    <section class="section container">
      <div class="section-header">
        <span class="eyebrow dark">Latest on VARTA</span>
        <h2>Fresh thinking from the community</h2>
      </div>
      <div class="grid two-up">
        <article class="post-card">
          <div class="post-tag">Science</div>
          <h3><a href="posts.html#post-1">Why Sound Matters — NADA & Hydrogen Awakening</a></h3>
          <p>Sound explains more than music. It may reveal a deeper way to understand energy, consciousness and culture.</p>
        </article>

        <article class="post-card">
          <div class="post-tag">Knowledge</div>
          <h3><a href="posts.html#post-2">Vedic Ideas and Modern Science</a></h3>
          <p>When tradition and evidence speak to each other, new forms of understanding can emerge.</p>
        </article>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <a href="index.html" class="brand small-brand">
          <img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" />
          <span>VARTA</span>
        </a>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="science.html">Science</a></li>
          <li><a href="indian-knowledge.html">Indian Knowledge</a></li>
          <li><a href="sound-nada.html">NADA</a></li>
        </ul>
      </div>
      <div>
        <h4>Community</h4>
        <ul>
          <li><a href="posts.html">Posts</a></li>
          <li><a href="submit.html">Submit</a></li>
          <li><a href="mailto:hello@varta.example">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Newsletter</h4>
        <form class="newsletter-form">
          <input type="email" placeholder="Email address" aria-label="Email" />
          <button type="submit">Join</button>
        </form>
      </div>
    </div>
    <div class="container legal-line">
      <span>© 2026 VARTA Prototype</span>
      <span><a href="#">Privacy</a> · <a href="#">Terms</a></span>
    </div>
  </footer>

  <script src="sw.js"></script>
</body>
</html>
EOF

cat > science.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Science — VARTA</title>
  <meta name="description" content="Scientific discourse and exploration on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>Science</h1>
      <p>Research, technology, systems and critical thinking for the modern world.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured story</h2>
      <p>Use this page for essays, experiments, climate ideas, technology commentary and evidence-driven discourse.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

cat > indian-knowledge.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Indian Knowledge — VARTA</title>
  <meta name="description" content="Indian knowledge traditions on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>Indian Knowledge</h1>
      <p>Philosophy, memory, Sanskrit, rituals, systems of thought and meaningful interpretation.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured reading</h2>
      <p>Use this page for scholarship, learning notes, and modern commentary on Indian intellectual traditions.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

cat > sound-nada.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sound & NADA — VARTA</title>
  <meta name="description" content="NADA, sound, vibration and media on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>Sound & NADA</h1>
      <p>Ragas, mantras, music, vibration and the study of resonance — from sound science to spiritual practice.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured audio/video</h2>
      <div class="video-wrap">
        <iframe src="https://www.youtube.com/embed/${VIDEO_ID}" title="Featured NADA video" allowfullscreen></iframe>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

cat > culture-nature.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Culture & Nature — VARTA</title>
  <meta name="description" content="Culture and nature on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>Culture & Nature</h1>
      <p>Local landscapes, artistic traditions, memory, rituals, seasons and a deeper relationship with the natural world.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured story</h2>
      <p>Use this section for visual storytelling, photo essays, and discussion about the living culture of Bharat.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

cat > world-affairs.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>World Affairs — VARTA</title>
  <meta name="description" content="World affairs and geopolitics on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Section</span>
      <h1>World Affairs</h1>
      <p>Public debate and analysis on geopolitics, energy, power, migration, climate and the global system.</p>
    </div>

    <article class="card detail-card">
      <h2>Featured reading</h2>
      <p>Use this page for geopolitical analysis, cross-country frameworks or summaries of global trends and energy policy.</p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

cat > posts.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Posts — VARTA</title>
  <meta name="description" content="Latest posts on VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="science.html">Science</a>
        <a href="indian-knowledge.html">Indian Knowledge</a>
        <a href="sound-nada.html">Sound & NADA</a>
        <a href="culture-nature.html">Culture</a>
        <a href="world-affairs.html">World Affairs</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Latest</span>
      <h1>Posts</h1>
    </div>

    <div class="grid two-up">
      <article class="post-card" id="post-1">
        <span class="post-tag">Science</span>
        <h2><a href="#">Why Sound Matters — NADA & Hydrogen Awakening</a></h2>
        <p>Sound is more than music. It links vibration, creativity, consciousness and the deeper structure of reality.</p>
      </article>

      <article class="post-card" id="post-2">
        <span class="post-tag">Knowledge</span>
        <h2><a href="#">Vedic Ideas and Modern Science</a></h2>
        <p>When ancient systems of thought meet scientific inquiry, new meaning opens up.</p>
      </article>
    </div>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF

if [ -n "$GOOGLE_FORM_IFRAME" ]; then
cat > submit.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Submit — VARTA</title>
  <meta name="description" content="Submit an idea or post to VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="posts.html">Posts</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Contribute</span>
      <h1>Submit an idea or post</h1>
      <p>Share a new idea, article proposal, short essay or community note.</p>
    </div>

    <article class="card detail-card">
      <h2>Submission form</h2>
      ${GOOGLE_FORM_IFRAME}
      <p class="submit-links">
        <a href="mailto:hello@varta.example" class="button primary">Email submission</a>
      </p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF
else
cat > submit.html <<EOF
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Submit — VARTA</title>
  <meta name="description" content="Submit an idea or post to VARTA." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container header-wrap">
      <a href="index.html" class="brand"><img src="assets/logo.svg" alt="VARTA logo" class="brand-mark" /><span>VARTA</span></a>
      <nav class="main-nav">
        <a href="index.html">Home</a>
        <a href="posts.html">Posts</a>
      </nav>
    </div>
  </header>

  <main class="container page-wrap">
    <div class="page-intro">
      <span class="eyebrow dark">Contribute</span>
      <h1>Submit an idea or post</h1>
      <p>Share a new idea, article proposal, short essay or community note.</p>
    </div>

    <article class="card detail-card">
      <h2>Submission form placeholder</h2>
      <p>Paste a Google Form embed or direct link here to collect user submissions.</p>
      <div class="submission-box">
        <p>Example Google Form embed placeholder:</p>
        <!-- Paste Google Form iframe here -->
      </div>
      <p class="submit-links">
        <a href="mailto:hello@varta.example" class="button primary">Email submission</a>
      </p>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container legal-line"><span>© 2026 VARTA Prototype</span></div>
  </footer>
</body>
</html>
EOF
fi

cat > css/style.css <<'EOF'
body {
  margin: 0;
  font-family: Inter, Arial, sans-serif;
  background: #fffaf3;
  color: #1d1d1d;
}
img { max-width: 100%; display: block; }
a { color: inherit; }
.container { width: min(1180px, calc(100% - 30px)); margin: 0 auto; }
.site-header { background: linear-gradient(180deg, #0f172a, #101827); position: sticky; top: 0; z-index: 10; box-shadow: 0 10px 25px rgba(15,23,42,.08); }
.header-wrap { display: flex; align-items: center; justify-content: space-between; min-height: 78px; gap: 20px; }
.brand { display: inline-flex; align-items: center; gap: 12px; text-decoration: none; color: white; font-weight: 800; letter-spacing: .08em; font-size: 1.2rem; }
.brand-mark { width: 32px; height: 32px; border-radius: 50%; }
.main-nav { display: flex; align-items: center; gap: 18px; flex-wrap: wrap; justify-content: flex-end; }
.main-nav a { text-decoration: none; color: #e8edf3; font-size: .92rem; }
.hero { background: radial-gradient(circle at 20% 20%, rgba(217,119,6,.18), transparent 24%), #fffaf3; padding: 72px 0 40px; }
.hero-grid { display: grid; grid-template-columns: 1.2fr .8fr; gap: 30px; align-items: center; }
.eyebrow { display: inline-block; font-size: .76rem; letter-spacing: .12em; text-transform: uppercase; color: #a75a00; font-weight: 700; }
.eyebrow.dark { color: #b45309; }
.hero h1, .page-intro h1 { margin: 12px 0 10px; font-size: clamp(2.7rem, 5vw, 5rem); line-height: .98; letter-spacing: -.06em; }
.tagline { margin: 0 0 16px; font-size: 1.25rem; color: #4b5563; }
.lead { font-size: 1.08rem; line-height: 1.6; color: #374151; max-width: 620px; }
.cta-row { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 24px; }
.button { display: inline-flex; align-items: center; justify-content: center; padding: 12px 18px; border-radius: 999px; text-decoration: none; font-weight: 600; transition: transform .2s ease; }
.button:hover { transform: translateY(-1px); }
.button.primary { background: linear-gradient(135deg, #d97706, #efb44a); color: white; }
.button.secondary { background: white; border: 1px solid rgba(15,23,42,.08); color: #111827; }
.stats { list-style: none; display: flex; gap: 18px; padding: 0; margin: 30px 0 0; flex-wrap: wrap; }
.stats li { background: rgba(255,255,255,.8); border: 1px solid rgba(15,23,42,.06); border-radius: 14px; padding: 16px 18px; min-width: 130px; display: flex; flex-direction: column; box-shadow: 0 12px 24px rgba(15,23,42,.04); }
.stats strong { font-size: 1.1rem; margin-bottom: 4px; }
.stats span { font-size: .8rem; color: #6b7280; }
.hero-panel { background: rgba(255,255,255,.7); border: 1px solid rgba(15,23,42,.06); border-radius: 22px; box-shadow: 0 20px 48px rgba(17,24,39,.08); padding: 16px; }
.panel-header { display: flex; gap: 8px; margin-bottom: 18px; }
.dot { display: inline-block; width: 12px; height: 12px; border-radius: 50%; }
.dot-one { background: #ff5959; }
.dot-two { background: #fbbf24; }
.dot-three { background: #34d399; }
.panel-card { background: linear-gradient(180deg, #ffffff, #fff8ef); border-radius: 18px; border: 1px solid rgba(15,23,42,.06); padding: 20px; }
.mini-label { color: #a75a00; font-size: .7rem; letter-spacing: .1em; text-transform: uppercase; font-weight: 700; }
.panel-card h3, .card h3, .post-card h2 { margin-top: 12px; margin-bottom: 10px; }
.panel-card a { color: #b45309; font-weight: 700; text-decoration: none; }
.panel-list { display: grid; gap: 12px; margin-top: 18px; }
.panel-list div { display: flex; justify-content: space-between; align-items: center; background: #fff; border: 1px solid rgba(15,23,42,.06); border-radius: 12px; padding: 12px 14px; }
.panel-list span { color: #374151; }
.section { padding: 58px 0 28px; }
.section-header { margin-bottom: 24px; }
.section-header h2 { margin: 8px 0 0; font-size: clamp(1.7rem, 3vw, 2.5rem); }
.grid { display: grid; gap: 20px; }
.three-up { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.two-up { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.card, .post-card, .detail-card { background: white; border: 1px solid rgba(15,23,42,.06); border-radius: 18px; padding: 22px; box-shadow: 0 14px 32px rgba(17,24,39,.04); }
.card .icon { width: 46px; height: 46px; border-radius: 14px; background: linear-gradient(135deg, #fef3c7, #fed7aa); color: #7c2d12; display: flex; align-items: center; justify-content: center; font-weight: 800; margin-bottom: 14px; }
.card a, .post-card a { color: #b45309; text-decoration: none; font-weight: 700; }
.feature-band { background: linear-gradient(180deg, rgba(255,245,230,.8), rgba(255,255,255,.9)); border-top: 1px solid rgba(15,23,42,.06); border-bottom: 1px solid rgba(15,23,42,.06); }
.feature-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; align-items: center; }
.feature-video iframe { width: 100%; min-height: 300px; border: 0; border-radius: 18px; }
.post-tag { display: inline-block; background: #fff7ed; border: 1px solid rgba(217,119,6,.18); color: #9a4b00; font-size: .72rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; padding: 7px 10px; border-radius: 999px; margin-bottom: 10px; }
.page-wrap { padding: 42px 0 36px; }
.page-intro { padding: 18px 0 12px; }
.page-intro h1 { font-size: clamp(2.3rem, 4vw, 3.8rem); }
.detail-card { margin-top: 14px; }
.video-wrap { margin-top: 12px; }
.video-wrap iframe { width: 100%; min-height: 320px; border: 0; border-radius: 16px; }
.submission-box { margin-top: 18px; border: 1px dashed rgba(15,23,42,.2); border-radius: 12px; min-height: 180px; background: #fffaf3; display: flex; align-items: center; justify-content: center; padding: 20px; color: #5b6470; }
.submit-links { margin-top: 18px; }
.site-footer { background: #0f172a; color: rgba(255,255,255,.82); padding: 32px 0 18px; }
.footer-grid { display: grid; grid-template-columns: 1.2fr 1fr 1fr 1.4fr; gap: 24px; }
.site-footer h4 { color: white; margin: 0 0 12px; }
.site-footer ul { list-style: none; padding: 0; margin: 0; display: grid; gap: 8px; }
.site-footer a { text-decoration: none; color: rgba(255,255,255,.8); }
.newsletter-form { display: flex; gap: 10px; flex-wrap: wrap; }
.newsletter-form input { flex: 1 1 160px; min-height: 42px; border-radius: 999px; border: 1px solid rgba(255,255,255,.15); background: rgba(255,255,255,.05); color: white; padding: 0 14px; }
.newsletter-form button { min-height: 42px; border: 0; border-radius: 999px; background: linear-gradient(135deg, #f59e0b, #f97316); color: white; font-weight: 700; padding: 0 16px; }
.legal-line { margin-top: 22px; padding-top: 18px; border-top: 1px solid rgba(255,255,255,.08); display: flex; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
.small-brand { font-size: 1.1rem; }
@media (max-width: 900px) { .hero-grid, .feature-grid, .footer-grid, .three-up, .two-up { grid-template-columns: 1fr; } .header-wrap { flex-direction: column; justify-content: center; padding: 14px 0; } .main-nav { justify-content: center; } }
EOF

cat > assets/logo.svg <<'EOF'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" role="img" aria-label="VARTA logo">
  <defs>
    <linearGradient id="g1" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#fbbf24"/>
      <stop offset="100%" stop-color="#f97316"/>
    </linearGradient>
  </defs>
  <rect width="200" height="200" rx="44" fill="#0f172a"/>
  <circle cx="100" cy="100" r="68" fill="none" stroke="url(#g1)" stroke-width="20" opacity="0.95"/>
  <path d="M78 93c0-9 7-16 16-16h26c13 0 22 9 22 22 0 14-10 23-25 26l-19 4c-7 2-13 9-13 16v8h26v12H75v-14c0-13 9-22 19-26l22-7c7-2 11-7 11-13 0-7-5-12-13-12H94c-7 0-13 5-13 12v7h-13v-7z" fill="#fff"/>
</svg>
EOF

cat > manifest.json <<'EOF'
{
  "name": "VARTA",
  "short_name": "VARTA",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#fffaf3",
  "theme_color": "#d97706",
  "description": "VARTA — India's Knowledge & Conversation Network",
  "icons": [
    { "src": "assets/logo.svg", "sizes": "any", "type": "image/svg+xml" }
  ]
}
EOF

cat > sw.js <<'EOF'
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('varta-cache-v1').then((cache) => cache.addAll([
      './',
      './index.html',
      './css/style.css',
      './assets/logo.svg'
    ]))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => response || fetch(event.request))
  );
});
EOF

git add -A
git commit -m "Add VARTA static site and embeds" || true
git push origin "${BRANCH}"

if [ -z "$GITHUB_TOKEN" ]; then
  echo "Files pushed. To enable Pages automatically, run with GITHUB_TOKEN set, or do this in the UI:"
  echo "Settings -> Pages -> Deploy from a branch -> Branch: main, Folder: /"
  echo "Site URL: https://${REPO_OWNER}.github.io/${REPO_NAME}/"
  exit 0
fi

curl -sS -X PUT \
  -H "Authorization: token ${GITHUB_TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/pages" \
  -d '{"source":{"branch":"main","path":"/"}}' | head

echo
echo "Check: https://${REPO_OWNER}.github.io/${REPO_NAME}/"


