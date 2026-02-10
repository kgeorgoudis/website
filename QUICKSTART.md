# Quick Start Guide - Blacklines.gr

## Prerequisites

- Python 3.12+
- uv package manager

## 5-Minute Setup

### 1. Install uv (if not already installed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Clone and setup

```bash
git clone https://github.com/yourusername/website.git
cd website
uv sync
```

### 3. Start development server

```bash
cd src
uv run pelican --autoreload --listen --port 8100
```

Visit: **http://localhost:8100**

## Creating New Content

### New DevOps Article

```bash
cd src/content/devops
# Create new file: my-article.md
```

Template:
```markdown
Title: Your Article Title
Date: 2026-02-10 14:30
Category: devops
Tags: kubernetes, docker
Slug: your-article-slug
Author: Konstantinos Georgoudis
Summary: Brief summary

# Your Article Title

Your content here...
```

### New Sketchnote

```bash
cd src/content/sketchnotes
# Create: my-sketch.md and add image to images/
```

### New DIY Project

```bash
cd src/content/diy
# Create: my-project.md and add images to images/
```

## Common Commands

```bash
# Development server with auto-reload
cd src && make devserver

# Build for production
cd src && make publish

# Clean output
cd src && make clean

# Just build (no server)
cd src && make html
```

## Deployment

### Render.com Setup

1. Create account at https://render.com
2. New Static Site
3. Connect GitHub repo
4. Configure:
   - **Build**: `cd src && uv run pelican content -s publishconf.py`
   - **Publish**: `src/output`
   - **Auto-deploy**: Enable on main branch

## Troubleshooting

**Port 8100 in use?**
```bash
lsof -i :8100
# Kill the process or use different port
make devserver PORT=8200
```

**Content not showing?**
- Check frontmatter has required fields (Title, Date, Category)
- Ensure Status: published (or omit, defaults to published)
- Verify category matches folder name (lowercase)

**Theme not loading?**
```bash
uv sync  # Reinstall dependencies
cd src && make clean && make html
```

## File Structure

```
src/
├── content/
│   ├── pages/          # About, Contact
│   ├── devops/         # DevOps articles
│   ├── sketchnotes/    # Sketchnote posts
│   ├── diy/            # DIY projects
│   └── images/         # Site images
├── pelicanconf.py      # Dev config
├── publishconf.py      # Production config
└── output/             # Generated site (gitignored)
```

## Next Steps

1. Update social links in `src/pelicanconf.py`
2. Add your profile photo to `src/content/images/profile.jpg`
3. Customize the About page in `src/content/pages/about.md`
4. Start creating content!

---

**Full documentation**: See [README.md](../README.md)

