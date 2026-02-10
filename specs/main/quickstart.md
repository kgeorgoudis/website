# Quickstart: Blacklines.gr Portfolio Website

## Prerequisites
- Python 3.12+
- uv installed (`pip install uv`)
- Render.com account (for deployment)

## Setup
```bash
uv sync
```

## Run Dev Server (auto-reload, port 8100)
```bash
uv run pelican --autoreload --listen --port 8100
```
Visit http://localhost:8100

## Add Content
- DevOps article: create `src/content/devops/my-article.md` with frontmatter (`Title`, `Date`, `Category: devops`, `Tags`, `Author`).
- Sketchnote: add images under `src/content/sketchnotes/images/` and markdown under `src/content/sketchnotes/` with captions + alt text.
- DIY project: place step photos under `src/content/diy/images/` and markdown in `src/content/diy/` with step-by-step sections.
- Pages (bio/contact): edit `src/content/pages/`.

## Build for Production
```bash
uv run pelican content -s publishconf.py
```
Output: `src/output/`

## Basic QA
- Run `uv run pelican content` to ensure clean build locally.
- Optional: run HTML/link checks (html5validator/linkchecker) against `src/output/`.
- Manual Lighthouse smoke on Home, DevOps article, Sketchnote detail, DIY detail.

## Deploy to Render.com (Static Site)
- Build command: `uv run pelican content -s publishconf.py`
- Publish directory: `src/output`
- Set environment: Python 3.12
- Add `static.json` for CSP/HSTS headers; enforce HTTPS in Render settings.

## Useful uv commands
```bash
uv add <package>     # add dependency
uv tree               # inspect deps
uv lock               # update lock
```

