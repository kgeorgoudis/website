# Blacklines.gr - Portfolio Website

A lightweight, fast, and secure static portfolio website built with [Pelican](https://getpelican.com/) and the [pelican-alchemy](https://github.com/nairobilug/pelican-alchemy) theme (sketchy variant). This site showcases DevOps articles, sketchnotes, and DIY/woodworking projects.

## 🚀 Features

- **Static Site Generation**: Built with Pelican for security and performance
- **Beautiful Theme**: pelican-alchemy sketchy variant for a unique aesthetic
- **Content Categories**: 
  - DevOps articles with syntax highlighting
  - Sketchnotes and urban sketches with image galleries
  - DIY and woodworking projects with step-by-step photos
- **Performance Optimized**: Lighthouse scores ≥95, lazy loading, responsive images
- **Deployment Ready**: Configured for Render.com free tier with automatic deployments

## 📋 Prerequisites

- **Python 3.12+**
- **uv** - Fast Python package installer and resolver

### Installing uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv
```

## 🛠️ Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/website.git
cd website
```

### 2. Install dependencies

```bash
uv sync
```

This will install Pelican, the alchemy theme, and all required dependencies.

### 3. Start the development server

```bash
cd src
make devserver
```

Or directly:

```bash
cd src
uv run pelican --autoreload --listen --port 8100
```

The site will be available at **http://localhost:8100**

The development server will automatically reload when you make changes to content or configuration files.

### 4. Stop the development server

Press `Ctrl+C` in the terminal.

## 📝 Creating Content

All content is written in Markdown with YAML frontmatter.

### Content Structure

```
src/content/
├── pages/           # Static pages (About, Contact)
├── devops/          # DevOps articles
├── sketchnotes/     # Sketchnote posts
├── diy/             # DIY project posts
└── images/          # Site-wide images
```

### Creating a New Post

#### DevOps Article

Create a new file in `src/content/devops/`:

```markdown
Title: Your Article Title
Date: 2026-02-10 14:30
Modified: 2026-02-10 14:30
Category: devops
Tags: kubernetes, docker, ci-cd
Slug: your-article-slug
Author: Konstantinos Georgoudis
Summary: Brief summary for listing pages and meta description

# Your Article Title

Your content here...

## Code Examples

\```python
def hello_world():
    print("Hello, World!")
\```
```

#### Sketchnote Post

Create a new file in `src/content/sketchnotes/`:

```markdown
Title: Your Sketchnote Title
Date: 2026-02-10 14:30
Category: sketchnotes
Tags: conference, visual-notes
Slug: your-sketchnote-slug
Author: Konstantinos Georgoudis
Summary: Brief description of the sketchnote

# Your Sketchnote Title

Description of what this sketchnote captures...

![Sketchnote image](/images/sketchnotes/your-image.jpg "Alt text description")
```

#### DIY Project

Create a new file in `src/content/diy/`:

```markdown
Title: Building a Wooden Bookshelf
Date: 2026-02-10 14:30
Category: diy
Tags: woodworking, furniture, beginner
Slug: wooden-bookshelf
Author: Konstantinos Georgoudis
Summary: Step-by-step guide to building a simple bookshelf

# Building a Wooden Bookshelf

## Materials
- Wood list
- Hardware

## Step 1: Cutting
![Cutting wood](/images/diy/bookshelf-step1.jpg "Cutting the pieces")
```

### Adding Images

1. Place images in the appropriate directory:
   - Site-wide images: `src/content/images/`
   - DevOps article images: `src/content/devops/images/`
   - Sketchnotes: `src/content/sketchnotes/images/`
   - DIY projects: `src/content/diy/images/`

2. Reference in Markdown:
   ```markdown
   ![Alt text](/images/your-image.jpg "Optional title")
   ```

3. **Optimize images before adding**:
   - Use WebP format when possible (with JPEG fallback)
   - Keep images under 500KB
   - Use responsive sizing

## 🏗️ Building for Production

### Build the static site

```bash
cd src
make publish
```

Or directly:

```bash
cd src
uv run pelican content -s publishconf.py
```

The generated site will be in `src/output/` directory.

### Test the production build locally

```bash
cd src/output
python -m http.server 8100
```

Visit http://localhost:8100 to preview.

## 🚢 Deployment to Render.com

### Initial Setup

1. **Create a Render account** at https://render.com

2. **Create a new Static Site**:
   - Connect your GitHub repository
   - Set build command: `cd src && uv run pelican content -s publishconf.py`
   - Set publish directory: `src/output`
   - Set environment to Python 3.12+

3. **Configure auto-deploy**:
   - Enable auto-deploy from main branch
   - Render will rebuild on every push

### Update Site URL

After deployment, update `src/publishconf.py` with your Render URL:

```python
SITEURL = "https://your-site-name.onrender.com"
```

### Custom Domain (Optional)

1. In Render dashboard, go to your site settings
2. Add custom domain: `blacklines.gr` or `www.blacklines.gr`
3. Update DNS records with provided values
4. Update `SITEURL` in `publishconf.py` to your custom domain

## 🔧 Configuration

### Main Configuration Files

- **`src/pelicanconf.py`**: Development configuration (port 8100, relative URLs)
- **`src/publishconf.py`**: Production configuration (absolute URLs, feeds enabled)

### Theme Configuration

The site uses the alchemy theme with the sketchy variant. Key settings in `pelicanconf.py`:

```python
THEME = 'alchemy'
SITESUBTITLE = 'DevOps, Sketchnotes, and DIY Creations'
```

### Customizing Navigation

Edit `MENUITEMS` in `src/pelicanconf.py`:

```python
MENUITEMS = (
    ('Home', '/'),
    ('DevOps', '/devops/'),
    ('Sketchnotes', '/sketchnotes/'),
    ('DIY & Crafts', '/diy/'),
    ('Contact', '/contact/'),
)
```

### Social Links

Update `SOCIAL` in `src/pelicanconf.py`:

```python
SOCIAL = (
    ('github', 'https://github.com/yourusername'),
    ('linkedin', 'https://linkedin.com/in/yourusername'),
    ('instagram', 'https://instagram.com/yourusername'),
    ('envelope', 'mailto:your.email@example.com'),
)
```

## 📦 Available Make Commands

From the `src/` directory:

```bash
make html          # Build the site once
make clean         # Remove generated files
make regenerate    # Rebuild on file changes (without server)
make serve         # Serve the site (without auto-rebuild)
make devserver     # Serve and auto-rebuild (recommended for development)
make publish       # Build for production
```

## 🐛 Troubleshooting

### Development server won't start

- Ensure port 8100 is not in use: `lsof -i :8100`
- Check that dependencies are installed: `uv sync`
- Verify you're in the `src/` directory

### Content not appearing

- Check frontmatter is valid YAML
- Ensure `Status: published` (or omit, published is default)
- Verify category matches folder name (lowercase)
- Check date format: `YYYY-MM-DD HH:MM`

### Images not loading

- Verify image path starts with `/images/`
- Check file exists in `src/content/images/` or subdirectory
- Ensure images are added to git (not in .gitignore)
- Check image filenames (no spaces, use hyphens)

### Build errors

Run with debug mode:
```bash
uv run pelican content -s pelicanconf.py -D
```

### Theme not applied

- Verify alchemy theme is installed: `uv run pip list | grep alchemy`
- Check `THEME = 'alchemy'` in pelicanconf.py
- Clear output and rebuild: `make clean && make html`

## 📚 Project Structure

```
.
├── README.md                    # This file
├── CONSTITUTION.md              # Project principles
├── pyproject.toml               # Python dependencies
├── uv.lock                      # Locked dependencies
├── specs/                       # Specifications and planning
│   └── main/
│       ├── spec.md              # Feature specification
│       ├── plan.md              # Implementation plan
│       ├── data-model.md        # Data model
│       ├── research.md          # Research notes
│       └── tasks.md             # Task breakdown
└── src/                         # Pelican source
    ├── pelicanconf.py           # Development config
    ├── publishconf.py           # Production config
    ├── Makefile                 # Build automation
    ├── tasks.py                 # Invoke tasks
    ├── content/                 # Content source files
    │   ├── pages/               # Static pages
    │   ├── devops/              # DevOps articles
    │   ├── sketchnotes/         # Sketchnotes
    │   ├── diy/                 # DIY projects
    │   └── images/              # Image assets
    └── output/                  # Generated site (gitignored)
```

## 🎨 Design Principles

This project follows these core principles:

- **Lightweight**: Minimal dependencies, no JavaScript frameworks, optimized assets
- **Fast**: Static generation, lazy loading, aggressive caching, Lighthouse ≥95
- **Secure**: HTTPS, CSP headers, static site (no server vulnerabilities)
- **Easy to Maintain**: Markdown content, clear structure, uv commands, good docs
- **Free Tier Compatible**: Works on Render.com free tier, <5 minute builds

## 📖 Additional Resources

- [Pelican Documentation](https://docs.getpelican.com/)
- [pelican-alchemy Theme](https://github.com/nairobilug/pelican-alchemy)
- [Markdown Guide](https://www.markdownguide.org/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Render Documentation](https://render.com/docs/static-sites)

## 📄 License

This project is open source. See LICENSE file for details.

## 🤝 Contributing

This is a personal portfolio site, but suggestions and feedback are welcome! Feel free to open an issue or reach out via the contact page.

---

**Built with ❤️ using Pelican and deployed on Render**
