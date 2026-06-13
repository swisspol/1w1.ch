# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-page static site for `1w1.ch`, deployed via GitHub Pages. The entire site is `docs/index.html` — no build step, no dependencies, no framework.

## Deployment

GitHub Pages serves the `docs/` folder on the `main` branch. Pushing to `main` deploys automatically. The custom domain is set via `docs/CNAME`.

## Design language

The site follows Swiss International Style / SBB (Swiss Federal Railways) aesthetics:
- Red: `#EB0000` (SBB red)
- Font: Inter 900 (Black) from Google Fonts — closest free match to Helvetica Neue Bold
- Text: `1w1` large, `.ch` at 60% size, baseline-aligned, white on red
