# Implementation Plan: Blacklines.gr Portfolio Website

**Branch**: `spec-kit` | **Date**: 2026-02-09 | **Spec**: `.specify/spec.md`
**Input**: Feature specification from `.specify/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Build a uv-managed Pelican 4.11+ static portfolio site using the pelican-alchemy "sketchy" theme, with clearly separated sections for Home/Bio, DevOps articles, Sketchnotes gallery, and DIY projects. Optimize for Lighthouse ≥95/90/95/95, lazy-loaded responsive images, minimal JS, and deployment on Render.com free tier with dev server on port 8100.

## Technical Context

**Language/Version**: Python 3.12 (uv-managed)  
**Primary Dependencies**: Pelican 4.11+, pelican-alchemy (sketchy), Markdown/Jinja2, typogrify/pygments for formatting  
**Storage**: N/A (static content from markdown files and assets)  
**Testing**: Pelican build validation + link/HTML checks; manual Lighthouse runs; optional Playwright viewport smoke for nav  
**Target Platform**: Render.com static site (Linux container) served over HTTPS  
**Project Type**: Static web site (single project)  
**Performance Goals**: Lighthouse ≥95 perf, FCP <1.0s, TTI <2.0s, per-page weight <500KB excluding images, lazy-loaded responsive images  
**Constraints**: Minimal JS, CSP + SRI on external assets, no inline JS, build <5 minutes on free tier, dev server on :8100, works with JS disabled  
**Scale/Scope**: Dozens of posts/pages across 3 content pillars; single author; low traffic but must feel instant on mobile

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Lightweight: Keep dependencies to Pelican + theme; avoid extra JS; target <1MB page weight (excluding images) and optimized assets.
- Fast: Enforce Lighthouse perf ≥95, FCP <1s, TTI <2s; use lazy loading, caching, responsive images, minimal render blockers.
- Secure (non-negotiable): HTTPS, CSP headers, SRI on externals, no inline JS, keep dependencies updated.
- Easy to Maintain: uv commands only, markdown content, clear structure, documented quickstart, no generated artifacts in git.
- Free Tier Compatible: Static build in <5 minutes, deployable on Render.com free tier with static hosting.

Status: PASS (all gates planned; revisit after design to confirm tooling keeps footprint and security intact).

## Project Structure

### Documentation (this feature)

```text
.specify/
├── plan.md              # This file (mirrored from specs/main for tooling)
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
└── spec.md              # Source specification
```

### Source Code (repository root)

```text
src/
├── pelicanconf.py        # Dev config (port 8100, autoreload)
├── publishconf.py        # Prod config for Render.com
├── content/              # Markdown sources (pages/, devops/, sketchnotes/, diy/)
├── output/               # Generated static files (gitignored)
└── tasks.py / Makefile   # Invoke pelican/automation helpers

pyproject.toml            # uv project definition
tasks/Make targets use uv # (see quickstart)
README.md                 # Top-level docs
```

**Structure Decision**: Single static-site project under `src/` with Pelican configs and content folders; documentation and contracts live in `.specify/` (mirrored under `specs/main/` for script compatibility); generated output remains ignored.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| _None_ | N/A | N/A |
