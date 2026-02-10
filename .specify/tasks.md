# Tasks: Blacklines.gr Portfolio Website

**Input**: Design documents from `.specify/`  
**Prerequisites**: plan.md, spec.md, data-model.md, research.md, quickstart.md  
**Status**: Ready for implementation  
**Date**: 2026-02-10

## Format: `- [ ] [TaskID] [P?] [Story?] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies on incomplete tasks)
- **[Story]**: User story label (US1, US2, US3, etc.) - ONLY for user story phase tasks
- Include exact file paths and actionable details

---

## Phase 1: Setup (Project Initialization)

**Purpose**: Initialize project structure, dependencies, and configuration for Pelican development

**⚠️ Note**: Setup must complete before foundational work

- [ ] T001 Update pyproject.toml with all required dependencies in `/Users/A200014545/code/Personal/www.blacklines.gr/website/pyproject.toml`
  - Add: `pelican[markdown]>=4.11.0`, `pelican-alchemy>=1.0.0`, `typogrify>=2.0.7`, `pygments>=2.11`, `markdown>=3.3.6`
  - Ensure `requires-python=">=3.12"` is set

- [ ] T002 [P] Run `uv sync` to install all dependencies and update `uv.lock` file

- [ ] T003 Create content directory structure under `src/content/`:
  - Create `src/content/pages/` for static pages (home, bio, contact)
  - Create `src/content/devops/` for DevOps articles
  - Create `src/content/devops/images/` for DevOps images
  - Create `src/content/sketchnotes/` for sketchnote posts
  - Create `src/content/sketchnotes/images/` for sketch images
  - Create `src/content/diy/` for DIY projects
  - Create `src/content/diy/images/` for DIY project photos

- [ ] T004 Create theme subdirectory structure:
  - Create `src/themes/` directory for theme installation
  - Ensure pelican-alchemy is available (via uv dependency)

- [ ] T005 [P] Configure .gitignore to exclude build artifacts and virtual environments:
  - Ensure `src/output/` is ignored
  - Ensure `.venv/` and virtual environment directories are ignored
  - Ensure Python cache files (`__pycache__/`, `*.pyc`) are ignored
  - Add `.DS_Store` and OS-specific files

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core Pelican configuration and infrastructure that blocks all user stories  
**⚠️ CRITICAL**: No user story work can begin until this phase completes

### Pelican Configuration

- [ ] T006 Update `src/pelicanconf.py` for development server configuration:
  - Set `THEME = 'pelican-alchemy'` and theme variant to 'sketchy'
  - Set `SITEURL = 'http://localhost:8100'` for development
  - Set `TIMEZONE = 'Europe/Athens'`
  - Set `DEFAULT_LANG = 'en'`
  - Configure `PATH = 'content'`
  - Set `ARTICLE_PATHS = ['devops', 'sketchnotes', 'diy']`
  - Set `PAGE_PATHS = ['pages']`
  - Set `STATIC_PATHS = ['images', 'extra']`
  - Configure markdown extensions for syntax highlighting: `MARKDOWN = {'extension_configs': {'markdown.extensions.codehilite': {'css_class': 'highlight'}, 'markdown.extensions.extra': {}, 'markdown.extensions.toc': {}}}`
  - Set `AUTHOR = 'Konstantinos Georgoudis'`
  - Set `SITENAME = 'Blacklines.gr'`
  - Enable category feeds: `CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'`
  - Set `DEFAULT_PAGINATION = 10`
  - Set `DISPLAY_PAGES_ON_MENU = False` (custom nav needed)
  - Disable inline feeds in dev: `FEED_ALL_ATOM = None` (for dev only)

- [ ] T007 Update `src/publishconf.py` for production Render.com deployment:
  - Set `SITEURL = 'https://www.blacklines.gr'` (or Render default URL during setup)
  - Set `RELATIVE_URLS = False`
  - Set `FEED_ALL_ATOM = 'feeds/all.atom.xml'`
  - Maintain `CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'`
  - Set `DELETE_OUTPUT_DIRECTORY = True` for clean builds
  - Import all base settings from pelicanconf.py

### Theme and Template Structure

- [ ] T008 [P] Create custom theme override in `src/themes/pelican-alchemy-custom/`:
  - Create `templates/` subdirectory
  - Create `static/css/` subdirectory for custom CSS
  - Create `templates/base.html` to override pelican-alchemy base (extend pelican-alchemy, customize nav structure)
  - Add custom navigation structure for Home, DevOps, Sketchnotes, DIY, Bio/Contact

- [ ] T009 [P] Create `src/themes/pelican-alchemy-custom/static/css/custom.css`:
  - Override theme colors minimally to match branding if needed
  - Ensure responsive image styling with `max-width: 100%` and `height: auto`
  - Add lazy loading styles: `.lazy { opacity: 0.8; }`, `.lazy.loaded { opacity: 1; transition: opacity 0.3s; }`
  - Ensure typography is readable on mobile (minimum 16px body text)
  - Ensure touch targets are minimum 44x44px
  - Add print styles to exclude nav/footer
  - Implement CSS-only gallery grid for sketchnotes/DIY: `display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;`

- [ ] T010 [P] Create `src/themes/pelican-alchemy-custom/static/css/responsive-images.css`:
  - Add styles for responsive image handling with `picture` elements
  - Configure `img { max-width: 100%; height: auto; display: block; }`
  - Add mobile-specific image width constraints
  - Ensure images don't cause layout shift (use aspect-ratio or reserved space)

### Performance & Security Headers

- [ ] T011 Create `static.json` in repository root for Render.com deployment headers:
  - Configure `Content-Security-Policy` header: `default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self';`
  - Configure `Strict-Transport-Security`: `max-age=31536000; includeSubDomains; preload`
  - Configure `X-Content-Type-Options`: `nosniff`
  - Configure `Referrer-Policy`: `strict-origin-when-cross-origin`
  - Configure `X-Frame-Options`: `SAMEORIGIN`

- [ ] T012 Create `.cache-control.json` or header rules in `static.json` for caching strategy:
  - CSS/JavaScript: `public, max-age=31536000, immutable` (1 year, cache-bust on filename)
  - Images: `public, max-age=2592000` (30 days)
  - HTML: `public, max-age=3600` (1 hour)
  - Fonts: `public, max-age=31536000, immutable`

### Markup and Accessibility

- [ ] T013 Create base page template `src/themes/pelican-alchemy-custom/templates/page.html`:
  - Ensure semantic HTML5 structure: `<header>`, `<nav>`, `<main>`, `<article>`, `<footer>`
  - Include proper language attribute on `<html>`
  - Add skip-to-main-content link for accessibility
  - Include meta viewport tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
  - Include proper charset declaration: `<meta charset="UTF-8">`
  - Add meta description from Pelican variables

- [ ] T014 Create article template `src/themes/pelican-alchemy-custom/templates/article.html`:
  - Display article metadata: title, date, author, category, tags
  - Render content with proper semantic markup
  - Include article navigation (previous/next)
  - Include breadcrumb navigation for context
  - Ensure code blocks are properly formatted with syntax highlighting

- [ ] T015 Create 404 page template `src/themes/pelican-alchemy-custom/templates/404.html`:
  - Create user-friendly 404 error page
  - Include site branding and navigation back to main sections
  - Suggest browsing sections: DevOps, Sketchnotes, DIY, Home
  - Include search/contact info

### Build and Deployment Configuration

- [ ] T016 Create `render.yaml` in repository root (optional but recommended):
  - Define static site service with Python 3.12 runtime
  - Set build command: `uv run pelican content -s publishconf.py`
  - Set publish directory: `src/output`
  - Configure HTTPS enforcement and custom domain if available

- [ ] T017 Create `Makefile` or update `src/tasks.py` with helpful commands:
  - `make dev` or `uv run invoke dev`: Start development server on port 8100
  - `make build` or `uv run invoke build`: Build for production
  - `make clean`: Clean output directory
  - `make validate`: Run build and basic HTML validation (optional)
  - Ensure all commands use `uv run` for consistency

### Documentation

- [ ] T018 Create comprehensive `README.md` with setup and deployment instructions:
  - Prerequisites: Python 3.12+, uv installed
  - Quick setup: `uv sync && uv run pelican --autoreload --listen --port 8100`
  - File structure overview: explain content organization
  - Adding content: examples for each section (DevOps, Sketchnotes, DIY)
  - Building for production: `uv run pelican content -s publishconf.py`
  - Deployment to Render.com: configuration steps
  - Development workflow: editing, preview, commit, push
  - Performance targets: Lighthouse scores, FCP, TTI
  - Constitution principles reference

- [ ] T019 Create `DEVELOPMENT.md` with detailed development workflow:
  - Step-by-step local setup instructions
  - Explanation of Pelican workflow and directory structure
  - How to add/edit content in each section
  - Theme customization guidelines
  - Image optimization recommendations
  - Testing locally before deployment
  - Troubleshooting common issues

### Testing Infrastructure (Foundation)

- [ ] T020 Create simple HTML validation script (optional, in `scripts/validate.py`):
  - Validate generated HTML files in `src/output/` for basic HTML5 compliance
  - Check for broken internal links within the generated site
  - Report missing images or alt text
  - Output report to console

**Checkpoint**: Foundation complete. All Pelican configuration, theme setup, and build infrastructure ready. Development server can start, production builds work. Ready for user story implementation.

---

## Phase 3: User Story 1 - Visitor Discovers Website Purpose (Priority: P1) 🎯 MVP

**Goal**: Create an engaging homepage with clear site description, author bio with picture, contact information, and visible navigation to all content areas

**Independent Test**: Navigate to homepage locally (`http://localhost:8100`), verify title, tagline, bio section with photo, contact info visible, and all navigation links are present and functional

### Content for User Story 1

- [ ] T021 [P] [US1] Create `src/content/pages/index.md`:
  - Title: "Home"
  - Add site tagline: "DevOps | Sketchnotes | DIY & Crafts"
  - Create welcome section with brief site description (3-4 sentences)
  - Create bio section with author name, professional background, and creative interests
  - Explain the three main content pillars
  - Use front matter: `Title`, `Date`, `Slug: index`, `Template: index`

- [ ] T022 [P] [US1] Create `src/content/pages/about.md`:
  - Title: "About"
  - Create detailed author bio (2-3 paragraphs)
  - Explain background in DevOps
  - Explain passion for visual communication (sketches)
  - Explain DIY/crafting interests
  - Maintain consistent voice and branding

- [ ] T023 [P] [US1] Create `src/content/pages/contact.md`:
  - Title: "Contact"
  - List contact methods: Email (with link), LinkedIn (with profile URL), GitHub (with profile URL)
  - Optionally add Instagram for sketch sharing
  - Add brief message encouraging visitors to reach out
  - Include preferred contact method for different topics if relevant

- [ ] T024 [US1] Create or place author photo in `src/content/pages/images/profile.jpg`:
  - Ensure image is optimized (compressed, reasonable dimensions: ~400x400px)
  - Create responsive version if needed: ~200x200px for sidebar, ~800x800px for detail page
  - Provide alt text: "Konstantinos Georgoudis profile photo"

### Theme Templates for User Story 1

- [ ] T025 [US1] Create `src/themes/pelican-alchemy-custom/templates/index.html`:
  - Display welcome section with site tagline
  - Display author bio with profile photo (responsive, lazy-loaded)
  - Display three content pillars with brief descriptions and links
  - Include calls-to-action: "Read DevOps Articles", "View Sketchnotes", "Explore DIY Projects"
  - Display contact information and social links
  - Responsive grid layout with clear visual hierarchy
  - Ensure touch-friendly links (minimum 44x44px)

- [ ] T026 [US1] Create `src/themes/pelican-alchemy-custom/templates/page.html` (override/enhance):
  - Display page title as page header
  - Include breadcrumb navigation (Home > Current Page)
  - Render page content with semantic HTML
  - Display sidebar navigation with all sections
  - Include footer with copyright and links

### Navigation Component

- [ ] T027 [US1] Create `src/themes/pelican-alchemy-custom/templates/nav.html`:
  - Create main navigation component
  - Include links: Home, DevOps, Sketchnotes, DIY & Crafts, About, Contact
  - Implement mobile hamburger menu (CSS-only, no JavaScript required)
  - Use semantic HTML: `<nav>`, `<ul>`, `<li>`, `<a>`
  - Ensure current page is highlighted
  - Ensure menu is keyboard navigable
  - Ensure touch targets are minimum 44x44px on mobile

### Styling for User Story 1

- [ ] T028 [P] [US1] Update `src/themes/pelican-alchemy-custom/static/css/custom.css`:
  - Style homepage hero section with welcome message and CTA buttons
  - Style bio section with author photo (float left on desktop, block on mobile)
  - Style content pillars as cards or visual sections
  - Ensure responsive layout: 1 column on mobile, 2-3 columns on tablet/desktop
  - Style navigation menu: responsive, mobile-first
  - Add hover states for links and buttons
  - Ensure text contrast meets WCAG AA (4.5:1 for normal text)
  - Ensure minimum 16px body text on mobile
  - Implement smooth transitions and animations (CSS-only, <300ms)

### Testing for User Story 1

- [ ] T029 [US1] Manual testing checklist - Homepage:
  - [ ] Homepage loads at `http://localhost:8100`
  - [ ] Title "Blacklines.gr" is visible
  - [ ] Tagline is visible
  - [ ] Welcome description is clear and compelling
  - [ ] Author bio is visible with profile photo
  - [ ] Contact information (email, LinkedIn, GitHub) is displayed
  - [ ] All navigation links are visible: Home, DevOps, Sketchnotes, DIY, About, Contact
  - [ ] Navigation links are functional (clickable, no 404s)
  - [ ] Mobile view: Text is readable without zooming
  - [ ] Mobile view: Navigation menu is accessible (hamburger or full menu)
  - [ ] Mobile view: Touch targets are adequate (44x44px minimum)
  - [ ] Images load and display correctly
  - [ ] Page scrolls smoothly without layout shift

- [ ] T030 [US1] Lighthouse audit - Homepage:
  - Run Lighthouse audit on homepage
  - Performance score ≥ 95
  - Accessibility score ≥ 90
  - Best Practices score ≥ 95
  - SEO score ≥ 95
  - Document scores and any issues

**Checkpoint**: User Story 1 complete. Homepage is live with clear site purpose, author bio, navigation, and contact info. Site is discoverable and sets up expectations for content areas. Ready to move to user story 2.

---

## Phase 4: User Story 2 - Developer Reads DevOps Content (Priority: P1)

**Goal**: Create a DevOps section with article listings, full articles with syntax highlighting, and easy navigation between articles

**Independent Test**: Navigate to DevOps section, view article list, open an article, verify code syntax highlighting, navigate between articles and back to list

### Content for User Story 2

- [ ] T031 [P] [US2] Create `src/content/devops/getting-started.md`:
  - Title: "Getting Started with DevOps"
  - Date: YYYY-MM-DD format
  - Category: `devops`
  - Author: "Konstantinos Georgoudis"
  - Tags: devops, basics, tools
  - Create initial article content (2-3 paragraphs, 500+ words)
  - Include at least one code block (Python, Bash, or YAML) to demonstrate syntax highlighting
  - Use markdown formatting: headers, lists, emphasis
  - Include links to related topics

- [ ] T032 [P] [US2] Create `src/content/devops/ci-cd-basics.md`:
  - Title: "CI/CD Pipeline Fundamentals"
  - Similar structure to above
  - Include code examples (GitHub Actions, GitLab CI, or Jenkins syntax)
  - Include architecture diagrams or ASCII art if relevant
  - Use backtick code blocks with language specification (e.g., ```yaml, ```python)

- [ ] T033 [P] [US2] Create 1-2 additional sample DevOps articles (e.g., Docker, Kubernetes intro):
  - Ensure variety of topics to showcase category
  - Include code blocks in each
  - Use consistent markdown frontmatter format

### Category Page for User Story 2

- [ ] T034 [US2] Create `src/themes/pelican-alchemy-custom/templates/category.html`:
  - Display category name and description
  - Display list of articles in category (title, date, excerpt)
  - Include pagination if > 10 articles
  - Ensure articles are sorted by date (newest first)
  - Display article metadata: date published, author, tags
  - Include link to each article
  - Display excerpt/summary if available
  - Responsive layout for mobile and desktop

- [ ] T035 [US2] Create category-specific landing page `src/content/devops/_index.md`:
  - Title: "DevOps Articles"
  - Category: devops
  - Add category description: what readers will find here
  - Add category image/header if desired
  - Use template: category (or custom devops-landing)
  - Front matter: `Title: DevOps`, `Date: YYYY-MM-DD`, `Status: draft` (so it doesn't appear in listings)

### Styling for User Story 2

- [ ] T036 [P] [US2] Update `src/themes/pelican-alchemy-custom/static/css/custom.css`:
  - Style article listings: card layout or list with preview
  - Style article metadata: date, author, tags (subtle styling)
  - Style code blocks: background color, border, syntax highlighting colors
  - Style article titles: clear hierarchy, hover effects
  - Ensure code blocks have horizontal scroll on mobile (not wrapping text awkwardly)
  - Style inline code: monospace, subtle background
  - Style blockquotes: left border, italic, lighter color
  - Ensure code text is readable (not too small, good contrast)

- [ ] T037 [P] [US2] Create or ensure `src/themes/pelican-alchemy-custom/static/css/syntax-highlighting.css`:
  - Ensure Pygments color scheme is applied (from Pygments CSS generation)
  - Define colors for: keywords, strings, comments, functions, numbers, etc.
  - Ensure good contrast in code blocks (white text on dark background or similar)
  - Verify syntax highlighting works with Markdown fenced code blocks

### Article Navigation

- [ ] T038 [US2] Update `src/themes/pelican-alchemy-custom/templates/article.html` to include:
  - Previous/next article navigation links
  - "Back to category" link
  - Related articles (by tag) if multiple articles exist
  - Breadcrumb: Home > Category > Article Title

### Testing for User Story 2

- [ ] T039 [US2] Manual testing checklist - DevOps Articles:
  - [ ] Navigate to DevOps section from navigation menu
  - [ ] DevOps listing page loads with article list
  - [ ] Article titles are visible and clickable
  - [ ] Article metadata displayed: date, author, tags
  - [ ] Article excerpts are visible
  - [ ] Click on article title opens full article
  - [ ] Full article loads with proper formatting
  - [ ] Code blocks display with syntax highlighting
  - [ ] Code is readable: text size, contrast, colors
  - [ ] Code blocks don't cause horizontal scroll on mobile (use horizontal scroll on code block, not page)
  - [ ] Previous/next article links work
  - [ ] "Back to DevOps" or category link works
  - [ ] Mobile view: article is readable without zooming
  - [ ] Mobile view: code blocks are scrollable horizontally
  - [ ] Images (if present) load and display correctly

- [ ] T040 [US2] Lighthouse audit - DevOps article:
  - Run Lighthouse on a DevOps article with code blocks
  - Performance score ≥ 95
  - Accessibility score ≥ 90
  - Best Practices score ≥ 95
  - SEO score ≥ 95
  - Verify code blocks don't impact performance

**Checkpoint**: User Story 2 complete. DevOps section fully functional with article listings, syntax-highlighted code blocks, and article navigation. Developers can read and navigate content easily.

---

## Phase 5: User Story 3 - Artist Explores Sketchnotes and Urban Sketches (Priority: P1)

**Goal**: Create a Sketchnotes gallery section with thumbnails, full-size images, descriptions, and optimized performance for image-heavy content

**Independent Test**: Navigate to Sketchnotes, view thumbnail gallery, click on thumbnail, view full-size image with description, navigate between sketches, verify images load efficiently (lazy loading works)

### Content for User Story 3

- [ ] T041 [P] [US3] Create sample sketchnote posts `src/content/sketchnotes/sketch-001.md`:
  - Title: "Understanding Kubernetes" (example)
  - Date: YYYY-MM-DD
  - Category: `sketchnotes`
  - Author: "Konstantinos Georgoudis"
  - Tags: kubernetes, architecture, visual-learning, sketches
  - Create description (1-2 paragraphs explaining the sketch)
  - Reference image: `![Kubernetes Architecture Sketch](images/sketch-001.jpg)`
  - Include alt text and captions
  - Use frontmatter: `Featured_image: images/sketch-001-thumb.jpg` or similar

- [ ] T042 [P] [US3] Create 3-4 additional sketchnote posts with varied topics:
  - Ensure images are placed in `src/content/sketchnotes/images/`
  - Include diverse topics to showcase gallery
  - Use consistent format for all posts
  - Ensure each post has clear description

- [ ] T043 [P] [US3] Prepare sketchnote images:
  - Optimize images: resize to web-appropriate dimensions
  - Create thumbnails (~300x300px or appropriate aspect ratio)
  - Create full-size versions (~1200px width for detail)
  - Save as WebP with JPEG fallback for broad compatibility
  - Ensure alt text is descriptive
  - Place in `src/content/sketchnotes/images/` directory

### Gallery Template for User Story 3

- [ ] T044 [US3] Create `src/themes/pelican-alchemy-custom/templates/gallery.html` or category-specific gallery:
  - Display CSS grid layout of thumbnails
  - Show thumbnail images with lazy loading (`loading="lazy"`)
  - Include image title/caption below thumbnail
  - Thumbnail images click through to full post
  - Responsive grid: 1 column on mobile, 2-3 columns on tablet, 3-4 on desktop
  - Use CSS Grid with `repeat(auto-fit, minmax(250px, 1fr))`
  - Ensure aspect ratio is consistent (e.g., 1:1 square thumbnails)

- [ ] T045 [US3] Update article template for sketchnote posts `src/themes/pelican-alchemy-custom/templates/article-sketchnote.html`:
  - Display article title and metadata
  - Display full-size image(s) with lazy loading and responsive sizing
  - Use `<picture>` element with `srcset` for responsive images
  - Display image captions and alt text
  - Include description text
  - Include navigation: previous/next sketch
  - Include category navigation
  - Ensure images are centered and readable at all sizes

### Image Optimization for User Story 3

- [ ] T046 [P] [US3] Create image optimization guidelines document:
  - Document in DEVELOPMENT.md or separate IMAGES.md
  - Explain image format recommendations: WebP primary, JPEG fallback
  - Explain sizing: thumbnail (~300x300px), detail (~1200px)
  - Explain compression: quality 80-85% for photos, higher for graphics
  - Provide commands or tools for optimization (ImageMagick, ffmpeg, online tools)
  - Explain lazy loading best practices
  - Explain responsive image syntax (srcset, sizes)

- [ ] T047 [P] [US3] Update custom CSS for responsive images in `src/themes/pelican-alchemy-custom/static/css/custom.css`:
  - Style gallery grid
  - Style individual gallery items with aspect ratio preservation
  - Ensure images in articles: `max-width: 100%`, `height: auto`
  - Add shadow or border styling for image prominence
  - Ensure images on mobile fit within viewport
  - Add caption styling below images

- [ ] T048 [P] [US3] Update `src/themes/pelican-alchemy-custom/static/css/responsive-images.css`:
  - Ensure `picture` element styling works correctly
  - Add fallback styles for unsupported browsers
  - Ensure images use aspect-ratio CSS property to prevent layout shift
  - Test with inspector to verify lazy loading behavior

### Testing for User Story 3

- [ ] T049 [US3] Manual testing checklist - Sketchnotes Gallery:
  - [ ] Navigate to Sketchnotes section from navigation
  - [ ] Gallery page loads with thumbnail grid
  - [ ] Thumbnails are visible and laid out in grid
  - [ ] Gallery is responsive: 1 column on mobile, multiple columns on desktop
  - [ ] Click on thumbnail opens full sketchnote post
  - [ ] Full-size image loads correctly
  - [ ] Image is readable and centered
  - [ ] Image captions are visible (if present)
  - [ ] Description text is visible and readable
  - [ ] Previous/next navigation links work
  - [ ] "Back to Sketchnotes" link works
  - [ ] Images have alt text (verify in inspector)
  - [ ] Mobile view: no horizontal scroll
  - [ ] Mobile view: images are appropriately sized
  - [ ] Desktop view: images are prominent and well-formatted

- [ ] T050 [US3] Lighthouse audit - Sketchnotes gallery and detail page:
  - Run Lighthouse on gallery (listing) page
  - Run Lighthouse on sketchnote detail page with full-size image
  - Performance score ≥ 95 (verify lazy loading is working)
  - Accessibility score ≥ 90 (verify alt text and contrast)
  - Best Practices score ≥ 95
  - SEO score ≥ 95
  - Test on 3G throttle to verify image optimization

- [ ] T051 [US3] Performance testing - Image loading:
  - Test lazy loading: images below fold load only when scrolled
  - Verify no layout shift when images load (aspect ratio preservation)
  - Test on slow 3G connection: page should load text first, images progressively
  - Verify image sizes: check DevTools network tab for actual file sizes
  - Document image file sizes and load times

**Checkpoint**: User Story 3 complete. Sketchnotes gallery fully functional with optimized responsive images, lazy loading, and clean gallery layout. Visitors can explore sketches efficiently on mobile and desktop.

---

## Phase 6: User Story 4 - Maker Discovers DIY and Woodworking Projects (Priority: P1)

**Goal**: Create a DIY/Crafts section showcasing projects with multiple images (step-by-step process), detailed descriptions, materials, and techniques

**Independent Test**: Navigate to DIY section, view project listing with featured images, open a project, view multiple step images with captions, read description with materials/techniques, navigate between projects

### Content for User Story 4

- [ ] T052 [P] [US4] Create sample DIY project post `src/content/diy/project-001.md`:
  - Title: "Building a [Project Name]" (e.g., bookshelf, workbench)
  - Date: YYYY-MM-DD
  - Category: `diy`
  - Author: "Konstantinos Georgoudis"
  - Tags: diy, woodworking, crafts, projects
  - Create structured content with sections: Materials, Tools, Process, Results
  - Include multiple images: material overview, step-by-step process (3-5 photos), finished product
  - Provide detailed descriptions for each step
  - Include tips or lessons learned
  - Reference images: `![Step 1: Cutting wood](images/project-001-step1.jpg)`, etc.

- [ ] T053 [P] [US4] Create 2-3 additional DIY project posts:
  - Ensure variety of projects to showcase category
  - Include different types: woodworking, DIY tech project, upcycling, etc.
  - Each project should have 3-5 process images
  - Use consistent format for all posts

- [ ] T054 [P] [US4] Prepare DIY project images:
  - Organize images in `src/content/diy/images/` by project
  - Create featured/hero images (~1200x800px, landscape recommended)
  - Create process step images (~1000x750px or landscape)
  - Create thumbnail versions for listing (~400x300px)
  - Optimize all images: WebP primary, JPEG fallback
  - Ensure high quality for detailed craftsmanship (quality 85%+)
  - Provide descriptive alt text for accessibility

### Project Listing Template for User Story 4

- [ ] T055 [US4] Create or update `src/themes/pelican-alchemy-custom/templates/diy-listing.html`:
  - Display DIY section title and description
  - List projects with featured images (hero images)
  - Show project title, date, brief excerpt
  - Responsive layout: 1 column on mobile, 2 columns on tablet, 2-3 on desktop
  - Use CSS grid for layout
  - Include featured image with lazy loading
  - Make entire project card clickable or only image/title
  - Include category/tags display

- [ ] T056 [US4] Update article template for DIY projects `src/themes/pelican-alchemy-custom/templates/article-diy.html`:
  - Display project title and metadata (date, author, tags)
  - Include breadcrumb navigation
  - Display full-size featured/hero image
  - Display materials section (list or table)
  - Display tools section (list)
  - Display process section with multiple images and descriptions
  - Use responsive image sizing for all images
  - Display finished product image prominently
  - Include project details/dimensions if applicable
  - Include next/previous project navigation

### Styling for User Story 4

- [ ] T057 [P] [US4] Update custom CSS for DIY project styling:
  - Style project listing cards with featured images
  - Ensure project cards are equal height and responsive
  - Style materials and tools sections (lists or tables)
  - Style process images in article: centered, full-width on mobile, constrained width on desktop
  - Add captions styling for process images
  - Ensure images don't cause layout shift (aspect ratio reservation)
  - Add visual separation between process steps
  - Ensure adequate spacing for readability

- [ ] T058 [P] [US4] Create project-specific CSS if needed for multi-image layout:
  - Support image galleries within articles (2-3 images side-by-side on desktop)
  - Maintain single column on mobile
  - Ensure images scale responsively
  - Add gallery navigation if multiple related images

### Testing for User Story 4

- [ ] T059 [US4] Manual testing checklist - DIY Projects:
  - [ ] Navigate to DIY & Crafts section from navigation
  - [ ] DIY listing page loads with project cards
  - [ ] Project cards display featured images
  - [ ] Project titles and dates are visible
  - [ ] Projects are laid out in responsive grid
  - [ ] Click on project card/title opens full project post
  - [ ] Full project page loads with all images
  - [ ] Materials section is readable (list or table format)
  - [ ] Tools section is visible
  - [ ] Process images load with captions/descriptions
  - [ ] Images are well-sized and don't cause awkward layout
  - [ ] Finished product image is prominent
  - [ ] Text descriptions are clear and detailed
  - [ ] Previous/next project navigation works
  - [ ] "Back to DIY" link works
  - [ ] Mobile view: cards are single column, readable
  - [ ] Mobile view: images are appropriately sized, no horizontal scroll
  - [ ] Desktop view: cards show good detail, images prominent

- [ ] T060 [US4] Lighthouse audit - DIY listing and detail page:
  - Run Lighthouse on DIY listing (project overview) page
  - Run Lighthouse on DIY detail page with multiple images
  - Performance score ≥ 95
  - Accessibility score ≥ 90 (verify images have alt text)
  - Best Practices score ≥ 95
  - SEO score ≥ 95
  - Test on 3G to verify image optimization impact

**Checkpoint**: User Story 4 complete. DIY section fully functional with project listings, multi-image process documentation, materials/tools details, and optimized responsive images. Makers can explore and learn from projects efficiently.

---

## Phase 7: User Story 5 - Developer Sets Up Local Environment (Priority: P2)

**Goal**: Enable developers and site owners to set up, preview, and modify the site locally with minimal friction

**Independent Test**: Clone repository, run `uv sync`, start dev server on port 8100, make a test Markdown change, verify hot-reload works, build for production, verify no errors

### Documentation for User Story 5

- [ ] T061 [US5] Ensure comprehensive README.md with setup instructions:
  - Prerequisites section: Python 3.12+, uv installation
  - Quick start: 3 simple steps (clone, uv sync, uv run dev)
  - Project structure explanation: directories and key files
  - Adding content: detailed examples for DevOps, Sketchnotes, DIY
  - Running locally: command to start dev server, expected output
  - Building for production: build command, output directory
  - Deployment: link to DEPLOYMENT.md
  - Troubleshooting section for common issues
  - Constitution principles summary at end

- [ ] T062 [US5] Ensure DEVELOPMENT.md with detailed dev workflow:
  - Setup verification: confirm `uv sync` works, list installed packages
  - Development server: explain autoreload feature, how to stop server
  - Content structure: explain frontmatter fields, naming conventions
  - Adding articles: step-by-step for each category
  - Theme customization: where to find theme files, what's safe to modify
  - Image optimization: tools and process
  - Testing content locally: running Lighthouse, checking links
  - Committing changes: commit message conventions
  - Troubleshooting: common errors and solutions

- [ ] T063 [US5] Create DEPLOYMENT.md with Render.com setup:
  - Prerequisites: Render.com account, GitHub repository
  - Step-by-step Render.com configuration:
    - Create Static Site service
    - Connect GitHub repository
    - Set build command: `uv run pelican content -s publishconf.py`
    - Set publish directory: `src/output`
    - Set environment: Python 3.12
  - Custom domain setup (if applicable)
  - HTTPS configuration verification
  - Environment variables (if any)
  - Monitoring build logs
  - Troubleshooting failed builds
  - Rollback procedures

- [ ] T064 [US5] Create QUICKSTART.md (summary of .specify/quickstart.md for root repo):
  - Copy/adapt quickstart.md to repository root or link to it
  - Ensure it's the first thing developers see after cloning

### Development Tools Configuration for User Story 5

- [ ] T065 [P] [US5] Ensure Makefile or invoke tasks are set up:
  - `make dev` or `uv run invoke dev`: Start development server
  - `make build` or `uv run invoke build`: Build for production
  - `make clean`: Clean output directory
  - `make validate`: Run build and basic validation (optional)
  - Ensure all commands use `uv run` and are documented

- [ ] T066 [P] [US5] Create `.python-version` file (already present, verify):
  - Ensure it specifies Python 3.12 or higher
  - Helps with local development environment consistency

### Environment and Configuration for User Story 5

- [ ] T067 [US5] Ensure pyproject.toml is properly configured:
  - All dependencies listed and pinned to compatible versions
  - Python version requirement clear: `requires-python=">=3.12"`
  - Project metadata complete: name, version, description
  - Optional: add development dependencies (html5validator, etc.)

- [ ] T068 [US5] Ensure uv.lock is committed to repository:
  - Ensures reproducible builds across environments
  - Document: `uv lock` command to update if dependencies change

### Testing Setup for User Story 5

- [ ] T069 [P] [US5] Create optional validation script in `scripts/validate-setup.sh`:
  - Check Python version is 3.12+
  - Check uv is installed
  - Check uv sync succeeds
  - Check all key files exist
  - Output success message with next steps

- [ ] T070 [US5] Create optional quick build test:
  - Document command to run local build: `uv run pelican content`
  - Document where to check for output: `src/output/index.html`
  - Document how to verify: open in browser, check for homepage

### Testing for User Story 5

- [ ] T071 [US5] Manual testing checklist - Local Setup:
  - [ ] Clone repository to new directory
  - [ ] Run `uv sync` - all dependencies install without errors
  - [ ] Check installed packages: `uv pip list` or inspect venv
  - [ ] Run `uv run pelican --help` - verify Pelican is available
  - [ ] Start dev server: `uv run pelican --autoreload --listen --port 8100`
  - [ ] Verify server starts and shows output
  - [ ] Open browser to http://localhost:8100
  - [ ] Homepage loads without errors
  - [ ] Edit a Markdown file in `src/content/pages/index.md`
  - [ ] Save the file
  - [ ] Verify browser automatically reloads (check for Pelican output message)
  - [ ] Verify changes are visible in browser
  - [ ] Stop server (Ctrl+C)
  - [ ] Run `uv run pelican content -s src/publishconf.py`
  - [ ] Verify build completes without errors
  - [ ] Check `src/output/` directory has generated files
  - [ ] Open `src/output/index.html` in browser - should match dev server
  - [ ] Verify no errors in console or build output

- [ ] T072 [US5] Cross-platform testing (if possible):
  - [ ] Test setup on macOS (primary platform)
  - [ ] Verify commands work in zsh shell
  - [ ] Document any platform-specific considerations

**Checkpoint**: User Story 5 complete. Developer can set up local environment in < 10 minutes, preview changes with hot-reload, and build for production without errors. Documentation is clear and comprehensive.

---

## Phase 8: User Story 6 - Site Owner Deploys to Render.com (Priority: P2)

**Goal**: Enable automated deployment to Render.com free tier with builds completing in < 5 minutes and HTTPS enforced

**Independent Test**: Configure Render.com service, push to GitHub, verify build completes in < 5 minutes, access site at Render.com URL, verify HTTPS, verify all content loads correctly

### Render.com Configuration for User Story 6

- [ ] T073 [US6] Create `render.yaml` configuration file:
  - Define static site service type
  - Set Python runtime to 3.12
  - Set build command: `uv run pelican content -s publishconf.py`
  - Set publish directory: `src/output`
  - Configure auto-deploy on main branch push
  - Set deploy hook for automatic rebuilds (if using Render's features)

- [ ] T074 [US6] Ensure `static.json` is properly configured (from Phase 2):
  - CSP headers set
  - HSTS header set for HTTPS enforcement
  - Cache control headers set
  - Verify Render recognizes and applies these headers

- [ ] T075 [US6] Configure HTTPS in Render.com:
  - Enable HTTPS enforcement (Render default)
  - Configure custom domain if applicable (blacklines.gr)
  - Set up DNS records if using custom domain
  - Verify HTTPS certificate is valid and auto-renewed

### Documentation for User Story 6

- [ ] T076 [US6] Document deployment procedure in DEPLOYMENT.md:
  - Step-by-step Render.com account setup
  - Repository connection walkthrough
  - Build configuration explanation
  - Custom domain setup (if applicable)
  - Testing deployed site
  - Monitoring build logs
  - Troubleshooting common deployment issues

- [ ] T077 [P] [US6] Update README.md with deployment link:
  - Add section "Deployment" with link to DEPLOYMENT.md
  - Add status badge if Render supports (optional)

### Git Configuration for User Story 6

- [ ] T078 [P] [US6] Verify `.gitignore` excludes unnecessary files:
  - Exclude `src/output/` (generated files)
  - Exclude `.venv/`, virtual environment directories
  - Exclude `__pycache__/`, Python cache
  - Exclude `.DS_Store` and OS files
  - Exclude IDE-specific files (.idea, .vscode, etc.)
  - Include `pyproject.toml` and `uv.lock` (needed for reproducible builds)

- [ ] T079 [P] [US6] Ensure all documentation files are committed:
  - Commit README.md, DEVELOPMENT.md, DEPLOYMENT.md
  - Commit render.yaml, static.json
  - Commit .specify/tasks.md (this file)
  - Commit pelicanconf.py, publishconf.py

### Testing for User Story 6

- [ ] T080 [US6] Manual testing checklist - Render.com Deployment:
  - [ ] Create Render.com account (if not already done)
  - [ ] Connect GitHub repository to Render.com
  - [ ] Create new Static Site service
  - [ ] Configure build command: `uv run pelican content -s publishconf.py`
  - [ ] Configure publish directory: `src/output`
  - [ ] Set environment: Python 3.12
  - [ ] Save and trigger initial build
  - [ ] Monitor build logs - verify build completes
  - [ ] Check build time - should be < 5 minutes (target 3 minutes)
  - [ ] Build succeeds without errors
  - [ ] Access deployed site at Render URL
  - [ ] Verify homepage loads without errors
  - [ ] Verify all assets load (CSS, images, etc.)
  - [ ] Verify navigation works on deployed site
  - [ ] Verify HTTPS - check URL is https://, not http://
  - [ ] Verify SSL certificate is valid (check browser lock icon)
  - [ ] Make a test commit to main branch
  - [ ] Verify Render auto-deploys the change
  - [ ] Verify deployed change is visible on live site
  - [ ] Test navigation across all sections on deployed site
  - [ ] Test on mobile device - verify responsive design works

- [ ] T081 [US6] Performance audit - Deployed site:
  - Run Lighthouse on deployed site (different from local due to CDN/caching)
  - Performance score ≥ 95
  - Accessibility score ≥ 90
  - Best Practices score ≥ 95
  - SEO score ≥ 95
  - Document scores

- [ ] T082 [US6] Security verification - Deployed site:
  - Verify HTTPS enforcement (HTTP redirects to HTTPS)
  - Verify security headers using online header checker (securityheaders.com)
  - Check CSP policy (should be restrictive)
  - Check HSTS header (should enforce HTTPS)
  - Verify no mixed content (images over HTTP, etc.)

**Checkpoint**: User Story 6 complete. Site is deployed to Render.com, builds automatically on push, HTTPS is enforced, and all content loads correctly. Public site is live and ready for visitors.

---

## Phase 9: User Story 7 - Content Creator Adds New Content (Priority: P2)

**Goal**: Enable easy content creation for new articles, sketches, and DIY projects with simple markdown templates and straightforward workflow

**Independent Test**: Create new article/sketch/project in markdown, preview locally, verify it appears in appropriate section and listing, deploy, verify it appears on live site

### Content Templates for User Story 7

- [ ] T083 [P] [US7] Create template `docs/CONTENT-TEMPLATES.md`:
  - DevOps article template with frontmatter example
  - Sketchnote post template with frontmatter
  - DIY project template with frontmatter and sections
  - Example of proper markdown formatting
  - Code block syntax highlighting examples
  - Image reference syntax with alt text
  - Instructions for each content type

- [ ] T084 [P] [US7] Create `src/content/devops/TEMPLATE.md`:
  - Template file content creators can copy
  - Include example frontmatter with all required fields
  - Include example structure: introduction, main content, conclusion
  - Include example code block
  - Include example image reference
  - Include tips for writing

- [ ] T085 [P] [US7] Create `src/content/sketchnotes/TEMPLATE.md`:
  - Template for sketchnote posts
  - Include frontmatter: Title, Date, Category, Author, Tags, Featured_image
  - Include example content structure: context, sketch description, key takeaways
  - Include image reference syntax
  - Include alt text example

- [ ] T086 [P] [US7] Create `src/content/diy/TEMPLATE.md`:
  - Template for DIY projects
  - Include section structure: Overview, Materials, Tools, Process, Results, Lessons
  - Include frontmatter with required fields
  - Include image reference syntax for multiple images
  - Include tips for step-by-step documentation

### Documentation for User Story 7

- [ ] T087 [US7] Create detailed content guidelines in DEVELOPMENT.md:
  - How to add a DevOps article: steps, frontmatter requirements, formatting tips
  - How to add a sketchnote: image preparation, markdown structure, alt text
  - How to add a DIY project: image organization, multi-image layout, section structure
  - Frontmatter field reference: which fields are required, optional
  - Image handling: where to place files, naming conventions, optimization
  - Markdown formatting reference: headers, lists, code, links, images
  - Category and tag guidelines: which categories exist, recommended tags
  - Publishing workflow: draft vs published status, testing before publish

- [ ] T088 [US7] Create quick-reference checklist for new content:
  - Filename: follow kebab-case naming convention
  - Frontmatter: Title, Date, Category, Author, Tags required
  - Slug: derive from filename or specify explicitly
  - Featured image: include for project/sketch listings
  - Images: place in `images/` subdirectory, use relative paths
  - Alt text: required for all images
  - Code blocks: specify language (python, bash, etc.) for syntax highlighting
  - Test locally: run dev server and verify in browser before committing
  - Proofread: check formatting, spelling, broken links

### Workflow Documentation for User Story 7

- [ ] T089 [US7] Document step-by-step content creation workflow:
  - 1. Clone and setup (or pull latest)
  - 2. Run `uv run pelican --autoreload --listen --port 8100`
  - 3. Choose content type (DevOps/Sketchnote/DIY)
  - 4. Copy template to new markdown file with appropriate naming
  - 5. Fill in frontmatter (title, date, category, tags)
  - 6. Write content in markdown
  - 7. Add images (for sketches/DIY)
  - 8. Save and preview in browser at localhost:8100
  - 9. Iterate on content until satisfied
  - 10. Commit: `git add -A && git commit -m "Add: [content title]"`
  - 11. Push: `git push origin main`
  - 12. Monitor build on Render.com
  - 13. Verify content on live site

### Image Optimization for Content Creators for User Story 7

- [ ] T090 [P] [US7] Create image optimization script or document:
  - Tool recommendations: ImageMagick, ffmpeg, or online tools
  - Sizing guidelines: thumbnails, detail sizes
  - Format guidelines: WebP preferred, JPEG fallback
  - Quality settings: 80-85% for photos, higher for graphics
  - File size targets: < 500KB per image (after optimization)
  - Batch processing examples (if complex)
  - Checklist before committing images

### Testing for User Story 7

- [ ] T091 [US7] Manual testing checklist - Content Creation:
  - [ ] Create new DevOps article by copying template
  - [ ] Fill in frontmatter: Title, Date, Category, Author, Tags
  - [ ] Write simple content (2-3 paragraphs)
  - [ ] Include a code block with ```python syntax
  - [ ] Save file locally
  - [ ] Run dev server: `uv run pelican --autoreload --listen --port 8100`
  - [ ] Refresh browser - verify article appears in DevOps listing
  - [ ] Click on article title - verify full article loads
  - [ ] Verify code syntax highlighting works
  - [ ] Edit the article markdown, save
  - [ ] Verify dev server reloads and changes appear in browser
  - [ ] Commit changes
  - [ ] Create new sketchnote post with image
  - [ ] Place image in `src/content/sketchnotes/images/`
  - [ ] Reference image in markdown with alt text
  - [ ] Save and preview - verify image appears with lazy loading
  - [ ] Create new DIY project with multiple images
  - [ ] Verify all images appear in correct order
  - [ ] Verify next/previous navigation includes new content
  - [ ] Push to repository
  - [ ] Monitor Render.com build
  - [ ] Verify new content appears on live site

- [ ] T092 [US7] Test edge cases:
  - [ ] Create article with missing required frontmatter - verify build error message
  - [ ] Create article with broken image reference - verify build warning
  - [ ] Create article with very long code block - verify no horizontal scroll on mobile
  - [ ] Create article with special characters in title - verify slug is generated correctly

**Checkpoint**: User Story 7 complete. Content creation workflow is straightforward, templates guide creators, documentation explains process clearly, and new content integrates seamlessly with the site.

---

## Phase 10: User Story 8 - Mobile User Browses the Site (Priority: P2)

**Goal**: Ensure the site is fast, responsive, and fully functional on mobile devices with proper touch targets, readable text, and optimized images

**Independent Test**: Access site on mobile device or mobile emulator, verify layout is responsive, text is readable without zooming, navigation is touch-friendly, images load properly, test on 3G connection to verify performance

### Responsive Design Configuration for User Story 8

- [ ] T093 [US8] Ensure responsive meta viewport tag in base template:
  - Verify in `src/themes/pelican-alchemy-custom/templates/base.html`
  - Must include: `<meta name="viewport" content="width=device-width, initial-scale=1">`
  - Ensure no user-scalable=no (allow user zoom)

- [ ] T094 [P] [US8] Review and update CSS for mobile-first responsive design:
  - Base styles target mobile (small screens)
  - Media queries add complexity for larger screens
  - Breakpoints: 480px, 768px, 1024px, 1280px (adjust as needed)
  - Test common device sizes: iPhone SE (375px), iPhone 12 (390px), iPad (768px), Desktop (1280px)

- [ ] T095 [P] [US8] Update custom.css to ensure proper mobile spacing:
  - Text: minimum 16px on mobile
  - Line-height: minimum 1.4-1.5 for readability
  - Padding/margin: sufficient for touch targets
  - Navigation: easily accessible on mobile
  - Images: responsive sizing, don't exceed viewport width
  - Code blocks: horizontal scroll on mobile, not page scroll

### Touch Target Sizing for User Story 8

- [ ] T096 [US8] Audit and update all interactive elements:
  - Navigation links: minimum 44x44px tap target
  - Buttons: minimum 44x44px
  - Article links: wrap in generous padding
  - Footer links: ensure adequate spacing
  - Form inputs (if any): minimum 44x44px
  - Document in custom.css with comments

### Typography for Mobile for User Story 8

- [ ] T097 [P] [US8] Verify typography settings for mobile readability:
  - Body text: 16px minimum on mobile
  - Headings: scale appropriately (h1 > h2 > h3 etc.)
  - Line-height: 1.4-1.6 for body text
  - Letter-spacing: not too tight
  - Paragraph spacing: clear separation of sections
  - Mobile-specific font adjustments in media queries if needed

### Image Sizing for Mobile for User Story 8

- [ ] T098 [P] [US8] Verify responsive image implementation:
  - `<picture>` elements with `<source>` for different formats (WebP, JPEG)
  - `srcset` on `<img>` for different densities/sizes
  - `sizes` attribute to match CSS layout
  - Fallback to JPEG for unsupported browsers
  - All images use `loading="lazy"`
  - Images scale to viewport on mobile: `max-width: 100%`

- [ ] T099 [P] [US8] Document image srcset strategy:
  - Thumbnail sizes for mobile and desktop
  - Detail image sizes for mobile and desktop
  - DPI considerations (1x, 2x for retina displays)
  - Example srcset values in DEVELOPMENT.md

### Navigation for Mobile for User Story 8

- [ ] T100 [US8] Ensure mobile navigation is functional without JavaScript:
  - CSS-only hamburger menu implementation (checkbox hack or similar)
  - Menu toggles visibility with CSS
  - Menu items are clearly visible when expanded
  - Touch-friendly menu item sizes
  - Menu closes when clicking outside or on a link
  - Breadcrumb navigation scales to mobile (might be stacked)

- [ ] T101 [P] [US8] Test keyboard navigation on mobile:
  - Tab through links with mobile keyboard
  - All interactive elements are keyboard accessible
  - Focus states are visible
  - Skip-to-main-content link works on mobile

### Performance Testing for Mobile for User Story 8

- [ ] T102 [US8] Perform Lighthouse audit on mobile:
  - Run Lighthouse with mobile profile
  - Performance score ≥ 95
  - Accessibility score ≥ 90
  - Best Practices score ≥ 95
  - SEO score ≥ 95
  - Test on slow 3G throttle

- [ ] T103 [US8] Test on real mobile devices (if possible):
  - iPhone (iOS) - various sizes
  - Android device - various sizes
  - Test navigation, scrolling, image loading, form interaction (if any)
  - Document any issues found

- [ ] T104 [US8] Test on mobile browser emulation:
  - Use Chrome DevTools mobile emulation
  - Test common devices: iPhone SE (375), iPhone 12 (390), iPad (768), etc.
  - Test portrait and landscape orientations
  - Verify layout adapts correctly

### Text Readability on Mobile for User Story 8

- [ ] T105 [P] [US8] Verify no text requires zoom to read:
  - Navigate to each page on emulated mobile device
  - Check that body text is readable at 100% zoom
  - Check that headings and links are clearly visible
  - Check that code blocks are readable (with horizontal scroll if needed)
  - Check that images have captions that are readable

### Testing for User Story 8

- [ ] T106 [US8] Manual testing checklist - Mobile Responsive:
  - [ ] Homepage on mobile (375px width)
  - [ ] Homepage on tablet (768px width)
  - [ ] Homepage on mobile landscape (667px width)
  - [ ] All sections on mobile (DevOps, Sketchnotes, DIY)
  - [ ] Article/post on mobile with code block (ensure no horizontal page scroll)
  - [ ] Article/post on mobile with images (ensure images scale properly)
  - [ ] Navigation menu on mobile (verify hamburger/responsive menu works)
  - [ ] Touch tap targets are large enough (test with finger if on real device)
  - [ ] Text is readable at 100% zoom (no pinch-to-zoom needed)
  - [ ] Images load and display properly on mobile
  - [ ] No horizontal page scroll on any page

- [ ] T107 [US8] Performance testing on slow connection:
  - Use Chrome DevTools throttle to 3G
  - Measure page load time: target < 3 seconds
  - Verify images load progressively (text first)
  - Verify no layout shift as images load
  - Verify no jank during scrolling
  - Document metrics

- [ ] T108 [US8] Accessibility testing on mobile:
  - Use screen reader (VoiceOver on iOS, TalkBack on Android if available)
  - Verify all content is accessible via screen reader
  - Verify alt text on images is present and descriptive
  - Verify heading structure is logical
  - Verify form inputs (if any) are labeled

**Checkpoint**: User Story 8 complete. Site is fully responsive, mobile-friendly, and performs well on slow connections. Visitors on mobile devices have excellent experience with readable text, proper touch targets, and optimized images.

---

## Phase 11: Polish & Cross-Cutting Concerns

**Purpose**: Final optimizations, documentation, testing, and deployment readiness

### Documentation Finalization

- [ ] T109 [P] Documentation completeness check:
  - [ ] README.md is comprehensive and up-to-date
  - [ ] DEVELOPMENT.md covers all dev workflows
  - [ ] DEPLOYMENT.md covers Render.com setup
  - [ ] CONSTITUTION.md principles are visible throughout project
  - [ ] Code comments explain non-obvious logic
  - [ ] All configuration files have comments explaining key settings

- [ ] T110 [P] Code cleanup and consistency:
  - [ ] All Python files (pelicanconf.py, publishconf.py) are well-commented
  - [ ] CSS files are organized and well-commented
  - [ ] No debug code or commented-out sections
  - [ ] Consistent indentation and formatting (4 spaces for Python, 2 spaces for CSS)
  - [ ] File naming is consistent (kebab-case for content, snake_case for Python)

### Security Hardening

- [ ] T111 [P] Verify security best practices:
  - [ ] All dependencies are up-to-date (check for CVEs)
  - [ ] No hardcoded secrets or sensitive data in repository
  - [ ] HTTPS is enforced on deployed site
  - [ ] Security headers (CSP, HSTS, etc.) are properly configured
  - [ ] No inline JavaScript in templates
  - [ ] No third-party trackers or analytics (unless explicitly needed)
  - [ ] SRI is used for any external resources

- [ ] T112 Dependency audit and updates:
  - Run `uv tree` to check dependency tree
  - Identify any outdated or vulnerable dependencies
  - Update to latest compatible versions
  - Update `pyproject.toml` and `uv.lock`
  - Verify all updates don't break build

### Performance Optimization

- [ ] T113 [P] Final performance review:
  - [ ] All images are optimized (run ImageMagick audit if possible)
  - [ ] CSS is minified in production build (verify in src/output/)
  - [ ] JavaScript (if any) is minified
  - [ ] Fonts are optimized (web fonts only if necessary)
  - [ ] Caching headers are properly configured
  - [ ] Lazy loading is implemented for all images
  - [ ] No render-blocking resources

- [ ] T114 Final Lighthouse audit - all key pages:
  - [ ] Homepage: Performance ≥ 95, Accessibility ≥ 90, Best Practices ≥ 95, SEO ≥ 95
  - [ ] DevOps article page: Same scores
  - [ ] Sketchnote detail page: Same scores
  - [ ] DIY project detail page: Same scores
  - [ ] Mobile profiles for all above
  - [ ] Document all scores and any improvements made

### Accessibility Validation

- [ ] T115 [P] WCAG 2.1 AA compliance check:
  - [ ] Use WAVE browser extension or similar
  - [ ] Check contrast ratios: 4.5:1 for normal text, 3:1 for large text
  - [ ] Verify all images have alt text
  - [ ] Verify heading structure is logical (no skipped levels)
  - [ ] Verify form inputs (if any) are properly labeled
  - [ ] Verify color is not the only indicator of information
  - [ ] Verify focus states are visible on all interactive elements

- [ ] T116 Keyboard navigation audit:
  - [ ] Tab through site - all interactive elements are reachable
  - [ ] Focus order is logical
  - [ ] No keyboard traps
  - [ ] Enter/Space activates buttons
  - [ ] Escape closes modals/menus (if any)

### Cross-Browser Testing

- [ ] T117 [P] Test on recent browser versions:
  - [ ] Chrome 90+ (latest)
  - [ ] Firefox 88+ (latest)
  - [ ] Safari 14+ (latest)
  - [ ] Edge 90+ (latest)
  - [ ] Verify layout and functionality on all
  - [ ] Check for console errors
  - [ ] Verify images display correctly
  - [ ] Verify CSS loads correctly

### Content Quality Final Review

- [ ] T118 Content review and proofreading:
  - [ ] All articles are well-written and error-free
  - [ ] All images have descriptive captions and alt text
  - [ ] All links (internal and external) work correctly
  - [ ] Metadata (dates, authors, tags, categories) is accurate
  - [ ] No placeholder text or Lorem Ipsum remaining
  - [ ] Content reflects personal branding and voice

- [ ] T119 Link verification (internal and external):
  - [ ] All internal links point to correct pages/articles
  - [ ] All external links are valid and relevant
  - [ ] No broken links in generated site (can use linkchecker tool)
  - [ ] Social links point to correct profiles

### Git and Repository Cleanup

- [ ] T120 [P] Git history and cleanup:
  - [ ] Verify .gitignore excludes all necessary files
  - [ ] No large files or secrets in repository history
  - [ ] Commits are well-organized and have clear messages
  - [ ] No unnecessary branches

- [ ] T121 [P] Create GitHub documentation files:
  - [ ] .github/CONTRIBUTING.md (if accepting contributions)
  - [ ] .github/ISSUE_TEMPLATE/ (if using GitHub Issues)

### Deployment Final Verification

- [ ] T122 [P] Final deployment checklist:
  - [ ] Render.com build succeeds consistently
  - [ ] Render.com build completes in < 5 minutes (target 3 minutes)
  - [ ] All pages accessible on deployed site
  - [ ] HTTPS is enforced
  - [ ] Custom domain resolves correctly (if applicable)
  - [ ] Auto-deploy on push works
  - [ ] Site is responsive on deployed version
  - [ ] Images load properly on deployed version
  - [ ] No 404s or missing resources on deployed version

### Monitoring and Maintenance Setup

- [ ] T123 [P] Create maintenance runbook:
  - [ ] How to check Render.com build logs
  - [ ] How to rollback failed deployment
  - [ ] How to monitor site performance
  - [ ] How to update dependencies
  - [ ] How to handle broken content (missing images, etc.)

- [ ] T124 Create update schedule and checklist:
  - [ ] Monthly: Check for Pelican and dependency updates
  - [ ] Quarterly: Run Lighthouse audits and address any regressions
  - [ ] Quarterly: Check external links for validity
  - [ ] As-needed: Add new content, update bio/contact info

### Final Testing and Validation

- [ ] T125 Comprehensive final test suite:
  - [ ] All user stories individually testable and working
  - [ ] All user stories can be tested in sequence
  - [ ] All user stories can be tested in parallel
  - [ ] No race conditions or conflicts between stories
  - [ ] Site works with JavaScript disabled
  - [ ] Site works on slow connections (3G throttle)
  - [ ] Site works on older devices (if scope permits)

- [ ] T126 Full regression test:
  - [ ] Verify all user stories still work after Phase 11 changes
  - [ ] Run through each story's acceptance scenarios
  - [ ] Verify no new bugs introduced
  - [ ] Verify no performance regressions

- [ ] T127 Project closure and handoff:
  - [ ] Update README.md with final deployment URL
  - [ ] Create release/v1.0.0 tag in Git
  - [ ] Document any known issues or future improvements
  - [ ] Update CONSTITUTION.md with final verification of principles
  - [ ] Create issues for any future enhancements
  - [ ] Celebrate launch! 🎉

**Checkpoint**: Phase 11 complete. Site is fully optimized, documented, tested, and deployed. All constitution principles are upheld. Project is ready for public launch and ongoing maintenance.

---

## Dependencies & Execution Order

### Phase Dependencies

```
Phase 1 (Setup)
    ↓
Phase 2 (Foundational) ← BLOCKING: No user story work begins until this completes
    ↓
    ├─→ Phase 3 (US1: Homepage) ←→ Phase 4 (US2: DevOps)
    ├─→ Phase 3 (US1: Homepage) ←→ Phase 5 (US3: Sketchnotes)
    ├─→ Phase 3 (US1: Homepage) ←→ Phase 6 (US4: DIY)
    ├─→ Phase 7 (US5: Local Setup)
    ├─→ Phase 8 (US6: Deployment)
    └─→ Phase 9 (US7: Content Workflow)
    └─→ Phase 10 (US8: Mobile)
    ↓
Phase 11 (Polish)
```

### Critical Path for MVP (User Story 1 Only)

1. **Phase 1**: Setup (T001-T005) - 30 minutes
2. **Phase 2**: Foundational (T006-T020) - 2-3 hours
   - Pelican configuration
   - Theme setup
   - Security headers
   - Build infrastructure
3. **Phase 3**: User Story 1 (T021-T030) - 2-3 hours
   - Homepage content
   - Navigation
   - Bio section
   - Testing

**MVP Ready**: After Phase 3, site has clear purpose, navigation, and can be deployed. Estimated total: 5-6 hours.

### Minimum Viable Product (MVP) Scope

Complete these tasks for MVP:
- ✅ All of Phase 1 (Setup)
- ✅ All of Phase 2 (Foundational - Pelican, theme, security)
- ✅ Phase 3 (User Story 1 - Homepage with purpose and bio)
- ✅ Phase 8 (User Story 6 - Deployment to Render.com)

**Optional for MVP**: Phases 4-7, Phase 10 can be done after MVP if needed

### Full Feature Delivery

Complete all tasks:
- Phase 1: Setup
- Phase 2: Foundational
- Phase 3-6: All user stories (US1-US4) - Content pillars
- Phase 7: Local development setup
- Phase 8: Render.com deployment
- Phase 9: Content creation workflow
- Phase 10: Mobile optimization
- Phase 11: Polish & cross-cutting concerns

**Estimated total**: 4-5 full development days or 2-3 weeks with part-time work

### Parallel Execution Opportunities

**Phase 2 Foundational Tasks** (can run in parallel):
- T006 Pelican config + T007 Production config (sequential, related)
- T008 Theme override + T009 Custom CSS + T010 Responsive images (parallel)
- T011 Security headers + T012 Caching strategy (parallel)
- T013 Base template + T014 Article template + T015 404 page (parallel)
- T018 README + T019 DEVELOPMENT docs (parallel)

**Phase 3+ User Stories** (can all run in parallel if team capacity allows):
- Once Phase 2 is complete, start all user stories in parallel
- Developer A: Phase 3 (US1: Homepage)
- Developer B: Phase 4 (US2: DevOps)
- Developer C: Phase 5 (US3: Sketchnotes)
- Developer D: Phase 6 (US4: DIY)

**Within Each User Story** (can run in parallel):
- Content creation (markdown files)
- Image optimization and preparation
- Template creation
- Styling updates
- Testing

### Example: Parallel Development Sprint

```
Developer A: Homepage (US1)
├── T021 Index markdown
├── T022 About markdown
├── T023 Contact markdown
├── T024 Profile photo
├── T025 Index template
├── T026 Page template
├── T027 Navigation component
└── T028 Homepage styling

Developer B: DevOps (US2)
├── T031-T033 DevOps articles
├── T034 Category page template
├── T035 Category landing
├── T036 Article list styling
├── T037-T038 Syntax highlighting + Article navigation
└── T039-T040 Testing

Developer C: Sketchnotes (US3)
├── T041-T043 Sketchnote posts
├── T043 Prepare and optimize images
├── T044-T045 Gallery templates
├── T046-T048 Image CSS
└── T049-T051 Testing

Developer D: DIY (US4)
├── T052-T054 DIY projects
├── T055-T056 Project listing templates
├── T057-T058 DIY styling
└── T059-T060 Testing
```

All developers work in parallel → Faster completion, better visibility

---

## Implementation Notes

### Constitution Alignment

Every task is aligned with Blacklines.gr Constitution principles:

- **Lightweight**: No unnecessary dependencies, minimal CSS/JS, clean structure (T001-T005, T008-T010, T028, T036-T037, T047-T048)
- **Fast**: Pelican static generation, image optimization, lazy loading, caching (T011-T012, T046-T048, T099, T113-T114)
- **Secure**: HTTPS, CSP headers, SRI, no inline JS, regular updates (T011, T111-T112)
- **Easy to Maintain**: Clear structure, markdown content, uv commands, comprehensive docs (T001-T005, T018-T019, T061-T092)
- **Free Tier Compatible**: Render.com support, <5 minute builds, static generation (T016-T017, T073-T082)

### File Structure Alignment

All tasks reference explicit file paths:
- Configuration: `src/pelicanconf.py`, `src/publishconf.py`
- Content: `src/content/{pages,devops,sketchnotes,diy}/`
- Themes: `src/themes/pelican-alchemy-custom/`
- Docs: `README.md`, `DEVELOPMENT.md`, `DEPLOYMENT.md`
- Build: `src/output/` (gitignored)

### Testing Strategy

- **No automated tests required** (static site generator, minimal code)
- **Manual testing per user story**: Each story has dedicated testing tasks
- **Lighthouse audits**: Performance, accessibility, best practices, SEO
- **Mobile testing**: Chrome DevTools emulation + manual if possible
- **Content quality**: Proofreading, link checking, image optimization

### Deployment Strategy

- **Dev server**: `uv run pelican --autoreload --listen --port 8100` (port 8100 per requirement)
- **Production build**: `uv run pelican content -s publishconf.py`
- **Deployment**: Render.com static site with auto-deploy on push
- **Build time**: Target < 3 minutes on Render.com free tier

### Git Workflow

Each task should ideally be a commit or logical group of commits:
```bash
git commit -m "Setup: Configure Pelican development environment"
git commit -m "Feature: Add homepage with bio section (US1)"
git commit -m "Feature: Add DevOps articles and syntax highlighting (US2)"
git commit -m "Feature: Add sketchnotes gallery with optimized images (US3)"
git commit -m "Feature: Add DIY projects with step-by-step documentation (US4)"
git commit -m "Deploy: Configure Render.com deployment"
git commit -m "Docs: Add content creation templates and guidelines"
git commit -m "Polish: Final optimization and lighthouse audits"
```

### Success Metrics

- Homepage loads in < 1 second (FCP < 1.0s)
- Any article/page loads in < 2 seconds (TTI < 2.0s)
- Lighthouse scores: 95+ Performance, 90+ Accessibility, 95+ Best Practices, 95+ SEO
- Site fully responsive and usable on mobile
- Render.com build completes in < 5 minutes (target 3 minutes)
- All links work (internal and external)
- All content displays correctly (text, images, code)
- Site fully functional without JavaScript

---

## Task Summary

| Phase | Name | Task Count | Completion Criteria |
|-------|------|-----------|---------------------|
| 1 | Setup | T001-T005 (5 tasks) | Project structure created, dependencies installed, git configured |
| 2 | Foundational | T006-T020 (15 tasks) | Pelican configured, theme set up, security headers, 404 page |
| 3 | US1: Homepage | T021-T030 (10 tasks) | Homepage with bio, navigation, contact info; Lighthouse ≥95 |
| 4 | US2: DevOps | T031-T040 (10 tasks) | Articles with syntax highlighting, listings, navigation |
| 5 | US3: Sketchnotes | T041-T051 (11 tasks) | Gallery with optimized images, lazy loading, responsive layout |
| 6 | US4: DIY Projects | T052-T060 (9 tasks) | Project listings, multi-image docs, materials/tools sections |
| 7 | US5: Local Dev | T061-T072 (12 tasks) | Setup docs, dev tools, templates, validation |
| 8 | US6: Deployment | T073-T082 (10 tasks) | Render.com config, HTTPS, auto-deploy, monitoring |
| 9 | US7: Content Workflow | T083-T092 (10 tasks) | Templates, guidelines, image optimization, workflow docs |
| 10 | US8: Mobile | T093-T108 (16 tasks) | Responsive design, touch targets, mobile testing |
| 11 | Polish | T109-T127 (19 tasks) | Optimization, security, accessibility, final testing |
| | | **Total: 127 tasks** | |

---

## Notes

- **[P] tasks**: Can run in parallel; different files or no dependencies
- **[Story] labels**: Map tasks to specific user story (US1-US8)
- **Setup/Foundational**: NO story labels (pre-story work)
- **Polish**: NO story labels (post-story work)
- **Execution**: Sequential by phase, but parallel within phase where [P] marked
- **MVP scope**: Phases 1-3, 8 (estimated 5-6 hours)
- **Full delivery**: All phases (estimated 4-5 full development days)
- **Constitution**: Every task upholds Lightweight, Fast, Secure, Easy to Maintain, Free Tier Compatible principles

---

**Last Updated**: 2026-02-10  
**Ready for Implementation**: ✅ Yes

