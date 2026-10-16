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


