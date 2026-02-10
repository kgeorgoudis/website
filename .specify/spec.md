# Feature Specification: Blacklines.gr Portfolio Website

**Feature Branch**: `main`  
**Created**: 2026-02-09  
**Status**: Active Development  
**Input**: User description: "Python Pelican static website builder. Theme: pelican-alchemy (sketchy variant). Local dev port: 8100. Deployment: render.com free tier. Content areas: DevOps notes/articles, sketchnotes/urban sketches with gallery, DIY/woodworking projects with pictures. Easy navigation, bio section with picture and contact info."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Visitor Discovers Website Purpose (Priority: P1)

A first-time visitor lands on the homepage and immediately understands what the website is about, who created it, and how to navigate to different content areas.

**Why this priority**: This is the foundation of the website. Without clear purpose and navigation, visitors will leave immediately. This is the minimum viable product.

**Independent Test**: Can be fully tested by visiting the homepage and verifying all navigation elements are visible, functional, and the site description/bio is clear. Delivers immediate value by introducing the site and creator.

**Acceptance Scenarios**:

1. **Given** a visitor lands on the homepage, **When** they view the page, **Then** they see a clear site title "Blacklines.gr", tagline/description, and visible navigation menu
2. **Given** a visitor is on the homepage, **When** they scroll down, **Then** they see a bio section with the author's picture, brief introduction, and contact information
3. **Given** a visitor wants to explore content, **When** they look at the navigation, **Then** they see clearly labeled sections: DevOps, Sketchnotes, and DIY/Crafts
4. **Given** a visitor clicks on any navigation link, **When** the page loads, **Then** they can easily navigate back to the homepage or to other sections

---

### User Story 2 - Developer Reads DevOps Content (Priority: P1)

A developer or DevOps practitioner visits the site to read technical articles and notes about DevOps topics, practices, and tools.

**Why this priority**: This represents one of the three core content pillars and must be functional for the site to serve its purpose.

**Independent Test**: Can be fully tested by navigating to the DevOps section, viewing article listings, reading an article, and verifying proper formatting, code syntax highlighting, and navigation between articles.

**Acceptance Scenarios**:

1. **Given** a visitor clicks on "DevOps" in the navigation, **When** the DevOps page loads, **Then** they see a list of articles with titles, publication dates, and excerpts
2. **Given** a visitor is viewing the DevOps article list, **When** they click on an article title, **Then** the full article loads with proper formatting, code highlighting, and readability
3. **Given** a visitor is reading a DevOps article, **When** they reach the end, **Then** they see links to related articles or back to the article list
4. **Given** a visitor views a DevOps article with code samples, **When** they scroll through the content, **Then** code blocks are properly syntax-highlighted and easily readable

---

### User Story 3 - Artist Explores Sketchnotes and Urban Sketches (Priority: P1)

An artist, designer, or visual learner visits the site to view sketchnotes and urban sketches, with accompanying descriptions and context.

**Why this priority**: This represents the second core content pillar, showcasing visual creativity and must be functional with proper image display and gallery functionality.

**Independent Test**: Can be fully tested by navigating to the Sketchnotes section, viewing thumbnail galleries, opening individual posts with full images, and verifying image quality, loading performance, and descriptive text.

**Acceptance Scenarios**:

1. **Given** a visitor clicks on "Sketchnotes" in the navigation, **When** the Sketchnotes page loads, **Then** they see a gallery/grid of sketch thumbnails with titles
2. **Given** a visitor is viewing the sketchnote gallery, **When** they click on a thumbnail, **Then** the post opens showing the full-size image(s) with accompanying description
3. **Given** a visitor views a sketchnote post, **When** the images load, **Then** they are optimized for web (lazy loading) and display properly on mobile and desktop
4. **Given** a visitor is viewing a sketchnote, **When** they want to see more, **Then** they can easily navigate to the next/previous sketch or back to the gallery

---

### User Story 4 - Maker Discovers DIY and Woodworking Projects (Priority: P1)

A DIY enthusiast or woodworker visits the site to explore projects, see photos of the build process, and read about construction techniques and materials.

**Why this priority**: This represents the third core content pillar and must showcase projects with multiple images and detailed descriptions.

**Independent Test**: Can be fully tested by navigating to the DIY section, viewing project listings, opening a project post with multiple images showing the build process, and reading the construction description.

**Acceptance Scenarios**:

1. **Given** a visitor clicks on "DIY & Crafts" in the navigation, **When** the DIY page loads, **Then** they see a list of projects with featured images, titles, and brief descriptions
2. **Given** a visitor is viewing the DIY project list, **When** they click on a project, **Then** the full project post loads with multiple photos showing the build process
3. **Given** a visitor is reading a DIY project post, **When** they scroll through, **Then** they see step-by-step descriptions, materials used, and techniques applied
4. **Given** a visitor views a DIY project, **When** images load, **Then** they are properly sized, captioned, and demonstrate the construction process clearly

---

### User Story 5 - Developer Sets Up Local Environment (Priority: P2)

A developer (or the site owner) wants to set up the local development environment to preview changes, add content, or modify the theme.

**Why this priority**: Essential for ongoing maintenance and content creation, but not needed for end-user experience.

**Independent Test**: Can be fully tested by following README instructions on a fresh machine, installing dependencies with `uv sync`, running the development server on port 8100, and making a test content change that appears in the browser.

**Acceptance Scenarios**:

1. **Given** a developer clones the repository, **When** they run `uv sync`, **Then** all dependencies install without errors
2. **Given** dependencies are installed, **When** they run `uv run pelican --autoreload --listen --port 8100`, **Then** the development server starts and is accessible at http://localhost:8100
3. **Given** the development server is running, **When** they edit a Markdown file in `src/content/`, **Then** the browser automatically reloads with the updated content
4. **Given** a developer wants to build for production, **When** they run `uv run pelican content -s publishconf.py`, **Then** the static site is generated in `src/output/` without errors

---

### User Story 6 - Site Owner Deploys to Render.com (Priority: P2)

The site owner wants to deploy the website to Render.com free tier so it's publicly accessible with automatic deployments on git push.

**Why this priority**: Critical for publishing the site, but comes after local development is working.

**Independent Test**: Can be fully tested by configuring Render.com service, pushing to git, verifying the build completes successfully, and accessing the live site at the Render.com URL.

**Acceptance Scenarios**:

1. **Given** the site owner has a Render.com account, **When** they configure a new Static Site service pointing to the repository, **Then** Render.com detects the build configuration
2. **Given** the Render.com service is configured, **When** the build command runs, **Then** the site builds successfully within the free tier time limits (< 5 minutes)
3. **Given** the build completes, **When** the site owner visits the Render.com URL, **Then** the website loads correctly with all assets and pages
4. **Given** the site is deployed, **When** the owner pushes new commits to the main branch, **Then** Render.com automatically rebuilds and redeploys the site

---

### User Story 7 - Content Creator Adds New Content (Priority: P2)

The site owner or a contributor wants to add a new article, sketch, or DIY project by creating a Markdown file and including images.

**Why this priority**: Essential for keeping the site active and growing, but can be done after initial setup.

**Independent Test**: Can be fully tested by creating a new Markdown file in the appropriate content directory, adding frontmatter (title, date, category), writing content, including images, and verifying it appears correctly on the site.

**Acceptance Scenarios**:

1. **Given** a content creator wants to add a DevOps article, **When** they create a new `.md` file in `src/content/devops/`, **Then** they can use a simple template with frontmatter (title, date, category, tags)
2. **Given** a content creator writes Markdown content, **When** they include code blocks, images, and links, **Then** Pelican processes them correctly with syntax highlighting and proper formatting
3. **Given** a content creator adds images, **When** they place images in an appropriate directory and reference them in Markdown, **Then** images display correctly with responsive sizing
4. **Given** new content is added and committed, **When** they preview locally or deploy, **Then** the new post appears in the appropriate section listing with correct metadata

---

### User Story 8 - Mobile User Browses the Site (Priority: P2)

A visitor accesses the website from a mobile device and expects fast loading, readable text, properly sized images, and touch-friendly navigation.

**Why this priority**: Mobile traffic is significant, and the site must be responsive and performant on mobile devices.

**Independent Test**: Can be fully tested by accessing the site on a mobile device or using browser developer tools' mobile emulation, verifying touch navigation works, text is readable without zooming, and images are appropriately sized.

**Acceptance Scenarios**:

1. **Given** a mobile user visits the site, **When** the page loads, **Then** the layout adapts to the mobile screen width with readable font sizes (minimum 16px for body text)
2. **Given** a mobile user navigates the site, **When** they tap on navigation elements, **Then** menus expand/collapse smoothly and links are touch-friendly (minimum 44x44px tap targets)
3. **Given** a mobile user views images, **When** images load, **Then** they are appropriately sized for the mobile viewport and use responsive image techniques (srcset)
4. **Given** a mobile user is on a slow 3G connection, **When** they access any page, **Then** the page loads in under 3 seconds with progressive content rendering

---

### Edge Cases

- What happens when a content file has malformed frontmatter (missing title, date, or category)?
  - **Expected**: Pelican build fails with a clear error message indicating which file and what's missing
  
- What happens when an image referenced in Markdown doesn't exist?
  - **Expected**: Pelican build shows a warning, and the broken image is visible in the output for debugging
  
- What happens when someone visits a URL that doesn't exist (404)?
  - **Expected**: Custom 404 page displays with site branding and navigation back to main sections
  
- What happens when a DevOps article contains very long code blocks?
  - **Expected**: Code blocks have horizontal scroll on mobile, syntax highlighting is maintained, and performance isn't degraded
  
- What happens when the Render.com build exceeds the free tier limits?
  - **Expected**: Build fails with clear message; optimization needed (reduce dependencies, simplify build)
  
- What happens when a visitor has JavaScript disabled?
  - **Expected**: Site remains fully functional with CSS-only interactions; no critical features depend on JavaScript
  
- What happens when images are very large (several MB)?
  - **Expected**: Build process or pre-deployment script warns about oversized images; documentation guides optimization
  
- What happens when someone tries to access the site over HTTP instead of HTTPS?
  - **Expected**: Automatic redirect to HTTPS (configured in Render.com or via headers)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST generate a static website using Pelican 4.11+ with Python 3.12+ managed via uv
- **FR-002**: System MUST use the pelican-alchemy theme (sketchy variant) for consistent visual design
- **FR-003**: System MUST provide a development server on port 8100 with auto-reload functionality
- **FR-004**: System MUST organize content into four distinct sections: Home/Bio, DevOps, Sketchnotes, and DIY/Crafts
- **FR-005**: System MUST display a homepage with site description, bio section with author picture, and contact information
- **FR-006**: System MUST support Markdown content files with frontmatter (title, date, category, tags, author)
- **FR-007**: System MUST provide clear navigation between all major sections from any page
- **FR-008**: System MUST support syntax highlighting for code blocks in DevOps articles
- **FR-009**: System MUST display images with lazy loading and responsive sizing for optimal performance
- **FR-010**: System MUST generate article/post listings with titles, dates, and excerpts for each content section
- **FR-011**: System MUST build the complete static site for production using publishconf.py configuration
- **FR-012**: System MUST support deployment to Render.com free tier with automated builds on git push
- **FR-013**: System MUST maintain page weight under 1MB (excluding images) per the Lightweight principle
- **FR-014**: System MUST achieve Lighthouse performance score ≥ 95 per the Fast principle
- **FR-015**: System MUST serve all content over HTTPS per the Secure principle
- **FR-016**: System MUST provide clear README documentation for local setup, development, and deployment
- **FR-017**: System MUST use uv commands for all Python operations (uv sync, uv run, uv add)
- **FR-018**: System MUST generate valid HTML5 with semantic markup for accessibility
- **FR-019**: System MUST support multiple images per DIY project post with captions
- **FR-020**: System MUST provide a 404 error page with navigation back to main sections

### Non-Functional Requirements

- **NFR-001**: Build time MUST be under 5 minutes to meet free tier constraints
- **NFR-002**: First Contentful Paint MUST be under 1.0 seconds
- **NFR-003**: Time to Interactive MUST be under 2.0 seconds
- **NFR-004**: Site MUST achieve WCAG 2.1 AA compliance for accessibility
- **NFR-005**: Site MUST work correctly in last 2 versions of Chrome, Firefox, Safari, Edge
- **NFR-006**: Site MUST be fully functional without JavaScript
- **NFR-007**: Mobile viewport text MUST be readable without zooming (minimum 16px)
- **NFR-008**: Touch targets MUST be minimum 44x44px for mobile usability
- **NFR-009**: Images MUST be optimized (WebP preferred, fallback to JPG/PNG)
- **NFR-010**: Code blocks MUST not cause horizontal page scroll on mobile
- **NFR-011**: All external resources MUST use Subresource Integrity (SRI) if applicable
- **NFR-012**: Content Security Policy headers SHOULD be implemented
- **NFR-013**: Site MUST compress assets using gzip/brotli
- **NFR-014**: Dependencies MUST be regularly updated for security
- **NFR-015**: Git repository MUST NOT include generated output or virtual environment files

### Key Entities *(include if feature involves data)*

- **Article/Post**: Represents written content (DevOps articles, sketchnote posts, DIY projects)
  - Attributes: title, date, author, category, tags, slug, content (Markdown), excerpt
  - Relationships: belongs to one category, has many tags, may have many images
  
- **Page**: Represents static pages (Home, About, Contact)
  - Attributes: title, content (Markdown), slug, template
  - Relationships: standalone, referenced in main navigation
  
- **Category**: Organizes posts into major content areas
  - Attributes: name (DevOps, Sketchnotes, DIY), slug, description
  - Relationships: has many posts
  
- **Tag**: Enables cross-category topic organization
  - Attributes: name, slug
  - Relationships: belongs to many posts
  
- **Image**: Visual content for posts
  - Attributes: filename, path, alt text, caption, dimensions
  - Relationships: belongs to a post, may have multiple sizes (thumbnail, full)
  
- **Author**: Content creator information
  - Attributes: name, bio, picture, email, social media links
  - Relationships: has many posts/pages

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Local development environment can be set up in under 10 minutes by following README instructions
- **SC-002**: Development server starts and is accessible at http://localhost:8100 with auto-reload working
- **SC-003**: Production build completes in under 3 minutes
- **SC-004**: Lighthouse performance score ≥ 95, accessibility ≥ 90, best practices ≥ 95, SEO ≥ 95
- **SC-005**: First Contentful Paint ≤ 1.0s, Time to Interactive ≤ 2.0s on 3G connection
- **SC-006**: All pages load successfully without errors on Render.com deployment
- **SC-007**: New content (article, sketch, or project) can be added via Markdown file and appears correctly after build
- **SC-008**: Site is fully navigable from any page to any other section in maximum 2 clicks
- **SC-009**: All images display with proper lazy loading and responsive sizing on mobile and desktop
- **SC-010**: Site functions correctly with JavaScript disabled (all content accessible, navigation works)
- **SC-011**: Code syntax highlighting works for common languages (Python, Bash, JavaScript, YAML, JSON)
- **SC-012**: Mobile viewport on iPhone SE and similar small devices displays readable text and functional navigation
- **SC-013**: Automated deployment from git push to live site completes within 10 minutes
- **SC-014**: Total page weight (excluding images) remains under 500KB per page
- **SC-015**: Bio section on homepage displays author picture, brief bio (2-3 paragraphs), and contact methods (email, social links)

### Definition of Done

A user story is considered done when:
1. All acceptance scenarios pass
2. Code is committed to version control
3. README documentation is updated if needed
4. Lighthouse scores meet targets
5. Manual testing on mobile and desktop passes
6. Site builds without errors locally and on Render.com
7. Changes are deployed to production

## Technical Notes

### Theme Configuration
- Use pelican-alchemy theme, specifically the "sketchy" variant
- Theme should be installed via uv or git submodule
- Customize theme colors/styles minimally to maintain Lightweight principle

### Content Organization
```
src/content/
├── pages/
│   ├── about.md (bio page)
│   └── contact.md (contact info)
├── devops/
│   ├── article-1.md
│   └── article-2.md
├── sketchnotes/
│   ├── sketch-1.md
│   └── images/
│       ├── sketch-1.jpg
│       └── sketch-2.jpg
└── diy/
    ├── project-1.md
    └── images/
        ├── project-1-step1.jpg
        └── project-1-step2.jpg
```

### Pelican Configuration Highlights
- `SITEURL`: Different for pelicanconf.py (http://localhost:8100) and publishconf.py (Render.com URL)
- `TIMEZONE`: Set appropriately
- `DEFAULT_LANG`: 'en'
- `THEME`: 'pelican-alchemy' (sketchy)
- `PLUGIN_PATHS`: If using plugins for galleries or code highlighting
- `MARKDOWN` extensions: codehilite, fenced_code, tables
- `STATIC_PATHS`: ['images', 'extra']
- `ARTICLE_PATHS`: ['devops', 'sketchnotes', 'diy']
- `PAGE_PATHS`: ['pages']

### Render.com Configuration
- Build command: `uv run pelican content -s publishconf.py`
- Publish directory: `src/output`
- Environment: Python 3.12+
- Auto-deploy: Enabled on main branch

### uv Commands Reference
```bash
# Install dependencies
uv sync

# Run development server
uv run pelican --autoreload --listen --port 8100

# Build for production
uv run pelican content -s publishconf.py

# Add a new dependency
uv add pelican-alchemy

# Run any Pelican command
uv run pelican --help
```

## Open Questions / Needs Clarification

- **Q1**: Should the site have RSS/Atom feeds for each content category?
  - **Recommendation**: Yes, Pelican generates these by default and they're useful for DevOps readers
  
- **Q2**: Should there be a search functionality?
  - **Recommendation**: Start without it (Lightweight principle), consider static search (lunr.js) only if needed later
  
- **Q3**: Should sketchnote and DIY posts support actual gallery functionality (lightbox, thumbnails)?
  - **Recommendation**: Use a lightweight Pelican plugin or simple CSS-only solution for image galleries
  
- **Q4**: What information should be in the contact section?
  - **Recommendation**: Email, LinkedIn, GitHub, and optionally Instagram for sketches
  
- **Q5**: Should comments be enabled on posts?
  - **Recommendation**: No, maintains static nature and Lightweight principle. Could add "Email me" link if discussion needed
  
- **Q6**: Custom domain or Render.com subdomain?
  - **Current**: Using blacklines.gr domain (implied from project name)

## Alignment with Constitution

This specification aligns with the project constitution:

- ✅ **Lightweight**: Minimal dependencies (Pelican + theme), no JavaScript frameworks, Markdown content
- ✅ **Fast**: Static site generation, lazy loading images, aggressive caching, Lighthouse score targets
- ✅ **Secure**: HTTPS enforced, static site (no server vulnerabilities), CSP headers
- ✅ **Easy to Maintain**: Markdown content, clear structure, uv commands, comprehensive README
- ✅ **Free Tier Compatible**: Static site works on Render.com free tier, under 5-minute builds, minimal resources

All requirements respect the decision-making framework and prioritize the core principles.

---

**Next Steps**: 
1. Review and approve this specification
2. Generate implementation plan (plan.md) using speckit.plan
3. Generate task breakdown (tasks.md) using speckit.tasks
4. Begin implementation following tasks.md

