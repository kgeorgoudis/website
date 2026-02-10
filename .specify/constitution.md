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
- Target deployment platforms: Render.com free tier, GitHub Pages, Netlify, Vercel, or Cloudflare Pages
- Keep build time under 5 minutes
- Respect bandwidth and storage limits (typically 100GB/month, 1GB storage)
- No server-side processing required
- All dynamic features must be client-side or use free APIs
- Optimize for free CDN usage
- **Decision Criteria**: Will this work on Render.com free tier and similar restrictive free options?

## Technical Architecture

**Technology Stack:**
- Static Site Generator: Pelican 4.11+
- Language: Python 3.12+
- Package Management: uv (modern Python package manager)
- Content Format: Markdown
- Templating: Jinja2 (included with Pelican)
- Theme: pelican-alchemy (sketchy variant)
- Version Control: Git
- Hosting: Render.com free tier (primary), with fallback options

**Project Structure:**
```
website/
├── src/
│   ├── pelicanconf.py      # Development configuration
│   ├── publishconf.py      # Production configuration
│   ├── content/            # Markdown content
│   │   ├── pages/          # Static pages (About, Contact)
│   │   ├── devops/         # DevOps articles and notes
│   │   ├── sketchnotes/    # Sketchnotes and urban sketches
│   │   └── diy/            # DIY/woodworking projects
│   ├── themes/             # Custom theme(s)
│   └── output/             # Generated static files (git-ignored)
├── pyproject.toml          # uv project configuration
└── README.md               # Development and deployment docs
```

**UV Command Standards:**
- Install dependencies: `uv sync`
- Run Pelican: `uv run pelican`
- Development server: `uv run pelican --autoreload --listen --port 8100`
- Build for production: `uv run pelican content -s publishconf.py`
- Add packages: `uv add [package-name]`

## Quality Standards

**Performance Metrics:**
- Lighthouse Performance: ≥ 95
- Lighthouse Accessibility: ≥ 90
- Lighthouse Best Practices: ≥ 95
- Lighthouse SEO: ≥ 95
- Page Load Time: < 2s on 3G connection

**Browser Support:** 
Last 2 versions of Chrome, Firefox, Safari, Edge; iOS Safari 14+; graceful degradation for older browsers

**Accessibility:** 
WCAG 2.1 AA compliance target; semantic HTML; keyboard navigation; screen reader compatible; 4.5:1 contrast ratio minimum

**Content Quality:**
- Clear, concise writing
- Proper heading hierarchy
- Alt text for all images
- Valid HTML/CSS
- No broken links

## Development Workflow

**Setup:**
1. Clone repository
2. Run `uv sync` to install dependencies
3. Start development server with `uv run pelican --autoreload --listen --port 8100`
4. Visit http://localhost:8100

**Feature Development:**
1. Document significant features in .specify/ directory
2. Test locally with development server
3. Verify performance impact (Lighthouse)
4. Check accessibility compliance
5. Update documentation
6. Commit with clear message

**Content Updates:**
1. Create/edit Markdown files in appropriate src/content/ subdirectory
2. Preview locally
3. Verify formatting, images, and links
4. Commit and push

**Deployment:**
- Automated deployment to Render.com on push to main branch
- Build command: `uv run pelican content -s publishconf.py`
- Output directory: `src/output`
- Environment: Python 3.12+
- Verify production deployment post-merge

## Governance

**Decision-Making Framework:**
When evaluating any change, ask:
1. **Alignment**: Does this align with core principles (lightweight, fast, secure, maintainable, free)?
2. **Necessity**: Is this necessary for the portfolio's purpose?
3. **Cost**: What is the cost in complexity, performance, maintenance?
4. **Alternatives**: Are there simpler alternatives?
5. **Trade-offs**: What are we sacrificing, and is it worth it?

**Decision Rule**: 
If a proposal violates more than one core principle, or significantly compromises one principle without clear benefit, reject it.

**Priority Order (when principles conflict):**
1. Secure (non-negotiable)
2. Fast
3. Lightweight
4. Easy to Maintain
5. Free Tier Compatible

**Constitution Authority**: 
This constitution supersedes all other practices and guides all development decisions. All specifications, plans, and implementations must align with these principles.

**Amendment Process:**
1. Document proposed change with rationale
2. Assess impact on existing features/workflow
3. Update constitution with sync impact report
4. Update affected templates and specifications
5. Document in git history

**Version**: 1.0.0 | **Ratified**: 2026-02-09 | **Last Amended**: 2026-02-09

