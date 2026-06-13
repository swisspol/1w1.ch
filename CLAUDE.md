# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-page static site for `1w1.ch`, deployed via GitHub Pages. The entire site is `docs/index.html` — no build step, no dependencies, no framework.

## Favicon generation

Run `generate_favicons.py` to regenerate all favicons into `docs/`:

```bash
.venv/bin/python generate_favicons.py
```

First run downloads Inter-Black.ttf from GitHub and caches it in `.font_cache/`. Outputs: `favicon.ico` (16/32/48px), `favicon-16x16.png`, `favicon-32x32.png`, `apple-touch-icon.png` (180px), `android-chrome-192x192.png`, `android-chrome-512x512.png`.

Dependencies are in `requirements.txt`. Set up with:

```bash
uv venv && uv pip install -r requirements.txt
```

After adding packages, regenerate `requirements.txt` with:

```bash
uv pip freeze > requirements.txt
```

## Deployment

GitHub Pages serves the `docs/` folder on the `main` branch. Pushing to `main` deploys automatically. The custom domain is set via `docs/CNAME`.

## Design language

The site follows Swiss International Style / SBB (Swiss Federal Railways) aesthetics:
- Red: `#EB0000` (SBB red)
- Font: Inter 900 (Black) from Google Fonts — closest free match to Helvetica Neue Bold
- Text: `1w1` large, `.ch` at 60% size, baseline-aligned, white on red
