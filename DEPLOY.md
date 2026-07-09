# Deployment Guide

## GitHub Pages (recommended)

```bash
# 1. Push to a repo
git remote add origin https://github.com/YOUR_USER/composio-research-submission.git

# 2. Create and push the gh-pages branch
git checkout -b gh-pages
git push origin gh-pages

# 3. In repo Settings → Pages → Source: Deploy from branch → gh-pages / (root)
#    Your dashboard will be live at:
#    https://YOUR_USER.github.io/composio-research-submission/
```

### Alternate: use the `/docs` folder

If you prefer to keep everything on `main`:

1. Copy `index.html` and `data/` into a `docs/` folder.
2. In repo Settings → Pages → Source: Deploy from branch → main → /docs.

## Vercel (one-click)

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy (static file server, no build step)
vercel --prod
```

The CLI will auto-detect this as a static project. Approve the defaults.

## Docker

```bash
# Build the image
docker build -t composio-research .

# Run
docker run -d -p 8080:80 composio-research
```

Open http://localhost:8080.

## Comparison

| Platform | Setup Time | Cost | Custom Domain |
|----------|-----------|------|---------------|
| GitHub Pages | ~2 min | Free | Yes (via CNAME) |
| Vercel | ~1 min | Free tier | Yes |
| Docker | ~3 min | Server cost | Yes |

## Environment Variables (for live MCP mode)

Set these on your deployment platform if running the pipeline server-side:

- `COMPOSIO_API_KEY` — your Composio API key
- `COMPOSIO_MOCK_MODE` — set to `1` to force mock mode

For static dashboard hosting (GitHub Pages / Vercel), no env vars are needed.
