<!--
Sync Impact Report
==================
Version change: N/A → 1.0.0 (Initial creation)
Modified principles: None (initial creation)
Added sections: All (Core Principles, Technical Architecture, Quality Standards, Development Workflow, Governance)
Removed sections: None
Templates requiring updates: N/A (no .specify.specify/ directory present)
Follow-up TODOs: None
-->

# Blacklines.gr Portfolio Website Constitution

## Core Principles

### I. Lightweight
**Minimize resource usage, dependencies, and complexity**
- Keep total page weight under 1MB (excluding images)
- Use minimal JavaScript; prefer CSS and HTML solutions
- Avoid unnecessary dependencies in pyproject.toml
- Optimize all assets (images, CSS, fonts) before deployment
- Use system fonts or only essential web fonts
- No external frameworks unless absolutely necessary
- **Decision Criteria**: "Can this be achieved with vanilla HTML/CSS/JS?" and "Does this meaningfully improve the portfolio experience?"

### II. Fast
**Deliver content to users as quickly as possible**
- Target Lighthouse performance score: 95+
- First Contentful Paint (FCP): < 1.0s
- Time to Interactive (TTI): < 2.0s
- Use lazy loading for images
- Minimize render-blocking resources
- Leverage browser caching
- Compress all assets (gzip/brotli)
- Use responsive images with srcset
- **Decision Criteria**: If a feature degrades Lighthouse score by >5 points, reconsider or optimize

### III. Secure (NON-NEGOTIABLE)
**Protect the site and its visitors from security threats**
- Always serve over HTTPS
- Implement Content Security Policy (CSP) headers
- Use Subresource Integrity (SRI) for external resources
- Keep Pelican and all dependencies updated
- Validate and sanitize all user inputs (if any forms added)
- No inline JavaScript where possible
- Regular security audits of dependencies
- Use secure hosting configurations
- **Decision Criteria**: No feature should compromise security; security updates take priority over feature development

### IV. Easy to Maintain
**Enable quick updates and modifications with minimal friction**
- Clear, consistent file structure
- Well-documented code and configuration
- Simple deployment process (single command preferred)
- Content in Markdown format for easy editing
- Version control all configuration and content
- Automated testing where applicable
- Clear README with setup instructions
- Minimal build steps
- **Decision Criteria**: Can a non-technical user add content? Can the site be rebuilt in < 5 minutes?

### V. Free Tier Compatible
**Operate within the constraints of free hosting services**
- Target deployment platforms: GitHub Pages, Netlify, Vercel, or Cloudflare Pages
- Keep build time under 5 minutes
- Respect bandwidth and storage limits (typically 100GB/month, 1GB storage)
- No server-side processing required
- All dynamic features must be client-side or use free APIs
- Optimize for free CDN usage
- **Decision Criteria**: Will this work on GitHub Pages (the most restrictive free option)?

## Technical Architecture

**Technology Stack:**
- Static Site Generator: Pelican 4.11+
- Language: Python 3.12+
- Content Format: Markdown
- Templating: Jinja2 (included with Pelican)
- Package Management: uv (modern Python package manager)
- Version Control: Git
- Hosting: Free tier static hosting (GitHub Pages/Netlify/Vercel)

**Project Structure:**
```
website/
├── src/
│   ├── pelicanconf.py      # Development configuration
│   ├── publishconf.py      # Production configuration
│   ├── content/            # Markdown content
│   ├── themes/             # Custom theme(s)
│   └── output/             # Generated static files (git-ignored)
```

## Quality Standards

**Performance Metrics:**
- Lighthouse Performance: ≥ 95
- Lighthouse Accessibility: ≥ 90
- Lighthouse Best Practices: ≥ 95
- Lighthouse SEO: ≥ 95
- Page Load Time: < 2s on 3G connection

**Browser Support:** Last 2 versions of Chrome, Firefox, Safari, Edge; iOS Safari 14+; graceful degradation

**Accessibility:** WCAG 2.1 AA compliance target; semantic HTML; keyboard navigation; screen reader compatible; 4.5:1 contrast ratio

## Development Workflow

**Feature Development:**
1. Document new features in .specify/ directory if significant
2. Test locally with `pelican --autoreload --listen`
3. Verify performance impact (Lighthouse)
4. Check accessibility
5. Update documentation
6. Commit with clear message

**Content Updates:**
1. Create/edit Markdown files in src/content/
2. Preview locally
3. Verify formatting and links
4. Commit and push

**Deployment:**
- Automated via GitHub Actions on push to main
- Build using publishconf.py
- Deploy to hosting service
- Verify production deployment

## Governance

**Decision-Making Framework:**
When evaluating any change, ask:
1. **Alignment**: Does this align with core principles (lightweight, fast, secure, maintainable, free)?
2. **Necessity**: Is this necessary for the portfolio's purpose?
3. **Cost**: What is the cost in complexity, performance, maintenance?
4. **Alternatives**: Are there simpler alternatives?
5. **Trade-offs**: What are we sacrificing, and is it worth it?

**Decision Rule**: If a proposal violates more than one core principle, or significantly compromises one principle without clear benefit, reject it.

**Constitution Authority**: This constitution supersedes all other practices and guides all development decisions.

**Version**: 1.0.0 | **Ratified**: 2026-02-09 | **Last Amended**: 2026-02-09

**Full Constitution**: See `/CONSTITUTION.md` for complete details, examples, and references.

