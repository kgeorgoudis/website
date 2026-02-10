# Implementation Tasks: Blacklines.gr Portfolio Website

**Generated**: 2026-02-10  
**Status**: In Progress  
**Feature**: main (Portfolio website with Pelican, pelican-alchemy sketchy theme, port 8100, Render.com deployment)

## Task List

### Phase 1: Foundation & Dependencies (P1)

#### Task 1.1: Install pelican-alchemy theme and configure dependencies
**Status**: TODO  
**Priority**: P1  
**Dependencies**: None  
**Estimate**: 15 min  
**Description**: Add pelican-alchemy theme to pyproject.toml dependencies and sync with uv.
**Acceptance**: 
- pelican-alchemy added to dependencies in pyproject.toml
- `uv sync` completes without errors
- Theme files accessible in Python environment

**Implementation Notes**:
```bash
uv add pelican-alchemy
```

---

#### Task 1.2: Configure pelicanconf.py for local development
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.1  
**Estimate**: 20 min  
**Description**: Update pelicanconf.py with theme configuration, port 8100, content paths, markdown extensions, and proper settings for local development.
**Acceptance**:
- THEME = 'alchemy' with THEME_STYLE = 'sketchy'
- Port set to 8100
- ARTICLE_PATHS configured for devops/sketchnotes/diy folders
- PAGE_PATHS configured for pages
- Markdown extensions include codehilite, fenced_code, tables
- STATIC_PATHS includes images
- Author info and social links properly configured

**Implementation Notes**:
- Keep existing AUTHOR, SITENAME, TIMEZONE settings
- Add THEME configuration
- Configure paths for content organization
- Enable syntax highlighting with Pygments

---

#### Task 1.3: Create publishconf.py for production deployment
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.2  
**Estimate**: 15 min  
**Description**: Create publishconf.py that imports pelicanconf.py and overrides settings for production (SITEURL, feeds, etc.).
**Acceptance**:
- publishconf.py imports from pelicanconf
- SITEURL set to production URL (to be determined or use Render subdomain)
- Feed generation enabled (FEED_ALL_ATOM, CATEGORY_FEED_ATOM)
- DELETE_OUTPUT_DIRECTORY = True for clean builds
- RELATIVE_URLS = False for production

**Implementation Notes**:
- Use Pelican standard publishconf pattern
- Enable caching and optimization settings

---

#### Task 1.4: Create content directory structure
**Status**: TODO  
**Priority**: P1  
**Dependencies**: None  
**Estimate**: 5 min  
**Description**: Create organized content directories under src/content/ for different content types.
**Acceptance**:
- Directories created: src/content/pages/, src/content/devops/, src/content/sketchnotes/, src/content/diy/
- Each section has images/ subdirectory where needed
- .gitkeep files added to preserve empty directories

**Implementation Notes**:
```bash
mkdir -p src/content/{pages,devops,sketchnotes,diy}
mkdir -p src/content/{devops,sketchnotes,diy}/images
```

---

### Phase 2: Core Content Pages (P1)

#### Task 2.1: Create homepage/about page with bio
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.4  
**Estimate**: 30 min  
**Description**: Create src/content/pages/about.md with site description, bio section, author picture reference, and contact information.
**Acceptance**:
- about.md contains frontmatter (title, slug)
- Bio text with 2-3 paragraphs about the author
- Reference to author photo (to be added later)
- Contact methods: email, LinkedIn, GitHub, Instagram
- Clear description of website purpose and content areas
- Markdown renders correctly in Pelican

**Implementation Notes**:
- Use Pelican page frontmatter
- Template: title: About, slug: about, save_as: index.html for homepage

---

#### Task 2.2: Create contact page
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.4  
**Estimate**: 15 min  
**Description**: Create src/content/pages/contact.md with structured contact information.
**Acceptance**:
- contact.md with proper frontmatter
- Email address
- Social media links (LinkedIn, GitHub, Instagram)
- Brief text inviting visitors to reach out

**Implementation Notes**:
- Keep it simple and static
- No contact form (maintaining static site principle)

---

#### Task 2.3: Create sample DevOps article
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.4  
**Estimate**: 20 min  
**Description**: Create src/content/devops/sample-devops-article.md with proper frontmatter and sample content including code blocks.
**Acceptance**:
- Markdown file with complete frontmatter (title, date, category: devops, tags, author)
- Sample article content with multiple paragraphs
- At least one code block with syntax highlighting (Python or Bash)
- Excerpt/summary for listing pages
- File builds without errors

**Implementation Notes**:
- Use Date format: YYYY-MM-DD HH:MM
- Category must be lowercase: devops
- Include tags for demonstration

---

#### Task 2.4: Create sample Sketchnote post
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.4  
**Estimate**: 20 min  
**Description**: Create src/content/sketchnotes/sample-sketch.md with image references and descriptive content.
**Acceptance**:
- Markdown file with frontmatter (title, date, category: sketchnotes, tags, author)
- Text describing the sketchnote
- Image reference (placeholder image acceptable)
- Proper markdown for responsive images

**Implementation Notes**:
- Category: sketchnotes
- Use proper image markdown syntax
- Include alt text for accessibility

---

#### Task 2.5: Create sample DIY project post
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.4  
**Estimate**: 25 min  
**Description**: Create src/content/diy/sample-woodworking-project.md with multiple image references showing build process.
**Acceptance**:
- Markdown file with frontmatter (title, date, category: diy, tags, author)
- Step-by-step description of project
- Multiple image references showing different stages
- Materials and tools sections
- Conclusion with results

**Implementation Notes**:
- Category: diy
- Multiple images demonstrating progression
- Clear structure for future DIY posts

---

### Phase 3: Theme & Styling (P1)

#### Task 3.1: Configure alchemy theme with sketchy variant
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.1, 1.2  
**Estimate**: 20 min  
**Description**: Configure pelicanconf.py theme settings to use alchemy with sketchy style variant.
**Acceptance**:
- THEME = 'alchemy' in pelicanconf.py
- Theme settings configured for sketchy variant
- Navigation properly displays categories
- Site builds with theme applied

**Implementation Notes**:
- Check alchemy theme documentation for sketchy variant configuration
- May need THEME_CSS_OVERRIDES or similar setting
- Verify theme is found by Pelican

---

#### Task 3.2: Configure navigation and menu structure
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 3.1  
**Estimate**: 15 min  
**Description**: Configure MENUITEMS or PAGES/CATEGORIES display in navigation with proper ordering.
**Acceptance**:
- Navigation shows: Home, DevOps, Sketchnotes, DIY/Crafts, Contact
- All links functional
- Active page highlighted in navigation
- Navigation visible on all pages

**Implementation Notes**:
- Use MENUITEMS in pelicanconf.py
- Ensure category pages are generated
- Test navigation flow

---

#### Task 3.3: Add placeholder author image
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 1.4  
**Estimate**: 10 min  
**Description**: Add a placeholder author photo or actual photo to static assets and reference in config/about page.
**Acceptance**:
- Image file added to appropriate static path
- Image optimized (WebP preferred, JPEG fallback)
- Referenced in about page
- Displays correctly with proper sizing

**Implementation Notes**:
- Create src/content/images/ if needed
- Add to STATIC_PATHS
- Use responsive image sizing

---

### Phase 4: Development Workflow (P1)

#### Task 4.1: Update Makefile for uv commands
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.1  
**Estimate**: 20 min  
**Description**: Modify src/Makefile to use uv commands instead of direct Python/pip commands.
**Acceptance**:
- `make devserver` uses uv run pelican with port 8100
- `make publish` uses uv run with publishconf.py
- `make clean` works properly
- All make targets use uv run

**Implementation Notes**:
- Replace pelican commands with `uv run pelican`
- Ensure port 8100 is specified for development
- Test all make targets

---

#### Task 4.2: Update tasks.py for uv compatibility
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 1.1  
**Estimate**: 15 min  
**Description**: If using tasks.py (Invoke), ensure all tasks use uv commands.
**Acceptance**:
- All invoke tasks use uv run
- Development server task sets port 8100
- Build tasks work correctly

**Implementation Notes**:
- Check if tasks.py is being used
- Update only if present
- Otherwise this task can be skipped

---

#### Task 4.3: Add .gitignore for output and cache
**Status**: TODO  
**Priority**: P1  
**Dependencies**: None  
**Estimate**: 5 min  
**Description**: Ensure .gitignore properly excludes output directories, cache, and Python artifacts.
**Acceptance**:
- src/output/ excluded
- __pycache__/ excluded
- *.pyc excluded
- .uv/ or .venv/ excluded if present
- Cache directories excluded

**Implementation Notes**:
- Check existing .gitignore or create one
- Follow Python and Pelican best practices

---

### Phase 5: Documentation (P1)

#### Task 5.1: Write comprehensive README
**Status**: TODO  
**Priority**: P1  
**Dependencies**: 1.1, 1.2, 1.3, 4.1  
**Estimate**: 45 min  
**Description**: Create detailed README.md with project description, setup instructions, development workflow, and deployment guide.
**Acceptance**:
- README contains:
  - Project description
  - Prerequisites (Python 3.12+, uv)
  - Installation instructions (`uv sync`)
  - Development server instructions (`make devserver` or direct command)
  - Content creation guide
  - Production build instructions
  - Render.com deployment guide
  - Port 8100 documentation
- Clear, step-by-step format
- Code examples for common tasks
- Troubleshooting section

**Implementation Notes**:
- Include uv installation instructions
- Document content structure
- Explain frontmatter requirements
- Add contributing guidelines if applicable

---

### Phase 6: Render.com Deployment (P2)

#### Task 6.1: Create Render.com configuration files
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 1.3  
**Estimate**: 20 min  
**Description**: Create render.yaml or document Render.com dashboard configuration for automatic deployments.
**Acceptance**:
- Configuration specifies:
  - Build command: `uv run pelican content -s publishconf.py`
  - Publish directory: `src/output`
  - Environment: Python 3.12+
  - Branch: main (or appropriate)
- Documentation in README covers Render.com setup

**Implementation Notes**:
- Check if render.yaml is supported or use dashboard
- Ensure uv is available in Render build environment
- May need to add uv installation to build command

---

#### Task 6.2: Add static.json for security headers
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 6.1  
**Estimate**: 15 min  
**Description**: Create static.json in src/output/ (via template or build step) to configure HTTPS redirects and security headers.
**Acceptance**:
- static.json includes:
  - HTTPS redirect
  - Security headers (CSP, HSTS, X-Frame-Options, etc.)
  - Proper caching headers
- File is included in build output

**Implementation Notes**:
- Check Render.com documentation for static.json format
- May need to copy file during build or place in static path
- Test headers after deployment

---

#### Task 6.3: Configure custom domain (optional)
**Status**: TODO  
**Priority**: P3  
**Dependencies**: 6.1  
**Estimate**: 30 min  
**Description**: If blacklines.gr domain is available, configure DNS and Render.com custom domain settings.
**Acceptance**:
- DNS records point to Render
- Render.com configured for custom domain
- HTTPS certificate issued
- Redirects from www to apex or vice versa

**Implementation Notes**:
- This is optional and can be done after initial deployment
- Document in README
- Update SITEURL in publishconf.py

---

### Phase 7: Content & Polish (P2)

#### Task 7.1: Create 404 error page
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 1.4, 3.1  
**Estimate**: 15 min  
**Description**: Create custom 404.html page with site branding and navigation back to main sections.
**Acceptance**:
- 404 page template or static page created
- Includes site navigation
- Friendly error message
- Matches site theme

**Implementation Notes**:
- Check alchemy theme 404 support
- May need custom template or page
- Ensure Render.com serves it for 404 errors

---

#### Task 7.2: Add RSS/Atom feed links to theme
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 1.3, 3.1  
**Estimate**: 10 min  
**Description**: Ensure feed links are visible in theme footer or sidebar.
**Acceptance**:
- Feed links visible on site
- Separate feeds for each category work
- Main site feed works
- Feed URLs are correct

**Implementation Notes**:
- Check alchemy theme feed configuration
- Enable in publishconf.py
- Test feed URLs

---

#### Task 7.3: Optimize sample images
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 2.4, 2.5  
**Estimate**: 20 min  
**Description**: Add sample images and ensure they are optimized (WebP/JPEG, reasonable file size, responsive).
**Acceptance**:
- Sample images added for sketchnotes and DIY posts
- Images under 500KB each
- WebP format with JPEG fallback preferred
- Proper alt text on all images
- Images display correctly on mobile and desktop

**Implementation Notes**:
- Use placeholder images if needed
- Document image optimization process in README
- Consider responsive image plugin or manual srcset

---

### Phase 8: Testing & Validation (P1)

#### Task 8.1: Test local development server
**Status**: TODO  
**Priority**: P1  
**Dependencies**: All previous P1 tasks  
**Estimate**: 15 min  
**Description**: Verify development server runs on port 8100, auto-reload works, and all pages are accessible.
**Acceptance**:
- Server starts with `uv run pelican --autoreload --listen --port 8100`
- Site accessible at http://localhost:8100
- Navigation works between all sections
- Sample content displays correctly
- Auto-reload works when editing content
- No console errors

**Implementation Notes**:
- Test on clean environment if possible
- Verify all content renders
- Check navigation flow

---

#### Task 8.2: Test production build
**Status**: TODO  
**Priority**: P1  
**Dependencies**: All previous P1 tasks  
**Estimate**: 15 min  
**Description**: Run production build and verify output is correct and complete.
**Acceptance**:
- Build completes: `uv run pelican content -s publishconf.py`
- No errors during build
- src/output/ contains complete site
- All pages generated
- Assets copied correctly
- Links are absolute for production

**Implementation Notes**:
- Check build time (should be under 3 minutes)
- Verify all files present in output
- Can test locally by serving output directory

---

#### Task 8.3: Validate HTML and check links
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 8.2  
**Estimate**: 20 min  
**Description**: Use HTML validator and link checker to ensure markup is valid and links work.
**Acceptance**:
- HTML5 validation passes
- No broken internal links
- External links are valid
- Images load correctly

**Implementation Notes**:
- Can use online validator or local tools
- Document any known issues
- Fix critical errors

---

#### Task 8.4: Run Lighthouse audit
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 8.2  
**Estimate**: 20 min  
**Description**: Run Lighthouse on built site to verify performance, accessibility, best practices, and SEO scores meet targets.
**Acceptance**:
- Performance ≥ 95
- Accessibility ≥ 90
- Best Practices ≥ 95
- SEO ≥ 95
- Document any issues to address

**Implementation Notes**:
- Test both mobile and desktop
- Can test locally or after deployment
- Focus on critical issues first

---

#### Task 8.5: Test mobile responsiveness
**Status**: TODO  
**Priority**: P2  
**Dependencies**: 8.1  
**Estimate**: 15 min  
**Description**: Test site on mobile devices or browser dev tools to ensure proper responsive behavior.
**Acceptance**:
- Site works on iPhone SE and similar small screens
- Text readable without zooming (≥16px)
- Navigation usable on mobile
- Images properly sized
- Touch targets ≥44px
- No horizontal scroll

**Implementation Notes**:
- Use browser dev tools mobile emulation
- Test actual device if available
- Check both portrait and landscape

---

## Summary

**Total Tasks**: 29  
**P1 Tasks**: 19  
**P2 Tasks**: 9  
**P3 Tasks**: 1  

**Estimated Total Time**: ~7.5 hours

**Critical Path**:
1. Install dependencies and configure Pelican (Tasks 1.1-1.3)
2. Create content structure and sample content (Tasks 1.4, 2.1-2.5)
3. Configure theme and navigation (Tasks 3.1-3.2)
4. Set up development workflow (Task 4.1, 4.3)
5. Write documentation (Task 5.1)
6. Test everything (Tasks 8.1-8.2)

**Next Steps**:
1. Begin with Phase 1 tasks to establish foundation
2. Move to Phase 2 and 3 for content and theme
3. Complete Phase 4 and 5 for workflow and documentation
4. Test thoroughly in Phase 8
5. Deploy to Render.com in Phase 6 when ready
6. Polish and optimize in Phase 7

---

**Notes**:
- All tasks respect the uv workflow
- Port 8100 consistently used for development
- pelican-alchemy sketchy theme as specified
- Render.com deployment configured
- Constitution principles (Lightweight, Fast, Secure, Easy to Maintain, Free Tier Compatible) followed throughout

