# Next Steps - Blacklines.gr

## Immediate Actions (Before Deployment)

### 1. Update Personal Information

**File: `src/pelicanconf.py`**

Replace placeholder social links:
```python
SOCIAL = (
    ('github', 'https://github.com/YOUR_ACTUAL_USERNAME'),
    ('linkedin', 'https://linkedin.com/in/YOUR_ACTUAL_USERNAME'),
    ('instagram', 'https://instagram.com/YOUR_ACTUAL_USERNAME'),
    ('envelope', 'mailto:YOUR_ACTUAL_EMAIL@example.com'),
)
```

### 2. Customize About Page

**File: `src/content/pages/about.md`**

- Update bio with your actual information
- Customize the description of your interests
- Update contact information

### 3. Update Contact Page

**File: `src/content/pages/contact.md`**

- Replace placeholder email and social media links
- Customize the topics you want to discuss

### 4. Add Profile Photo (Optional)

Add your profile photo:
```bash
# Place your photo here:
src/content/images/profile.jpg

# Optimize it first:
# - Recommended size: 400x400px
# - Format: JPEG or WebP
# - File size: < 100KB
```

Update reference in `src/pelicanconf.py`:
```python
SITEIMAGE = '/images/profile.jpg width=200 height=200'
```

### 5. Review Sample Content

The site includes 3 sample posts:
- DevOps: `src/content/devops/getting-started-containers.md`
- Sketchnote: `src/content/sketchnotes/power-of-sketchnotes.md`
- DIY: `src/content/diy/simple-wooden-desk-organizer.md`

**Options:**
- Keep them as examples
- Modify them with your actual content
- Delete and replace with your own posts

## Local Testing

Before deploying, test everything locally:

```bash
cd src

# Start dev server
make devserver

# Visit http://localhost:8100
# Check:
# - All navigation links work
# - Pages load correctly
# - No broken links
# - Content displays properly
```

## Deployment to Render.com

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Initial website setup"
git push origin main
```

### Step 2: Configure Render.com

1. Go to https://render.com and sign in
2. Click "New" → "Static Site"
3. Connect your GitHub repository
4. Configure settings:
   - **Name**: blacklines (or your choice)
   - **Branch**: main
   - **Build Command**: `cd src && uv run pelican content -s publishconf.py`
   - **Publish Directory**: `src/output`
5. Click "Create Static Site"

### Step 3: Update Site URL

After deployment, Render will give you a URL like:
`https://blacklines.onrender.com`

Update `src/publishconf.py`:
```python
SITEURL = "https://blacklines.onrender.com"  # Use your actual URL
```

Commit and push:
```bash
git add src/publishconf.py
git commit -m "Update site URL for production"
git push origin main
```

Render will automatically rebuild.

### Step 4: Custom Domain (Optional)

If you own `blacklines.gr`:

1. In Render dashboard, go to your site → Settings
2. Click "Custom Domains"
3. Add domain: `blacklines.gr` or `www.blacklines.gr`
4. Follow DNS configuration instructions
5. Update `src/publishconf.py` with custom domain
6. Push changes

## Adding Content

### Create a New DevOps Article

```bash
cd src/content/devops
# Create: my-new-article.md
```

Template:
```markdown
Title: My New Article
Date: 2026-02-10 14:00
Category: devops
Tags: kubernetes, automation
Slug: my-new-article
Author: Konstantinos Georgoudis
Summary: Brief summary of the article

# My New Article

Content here...
```

### Add Images

```bash
# Place images in appropriate directory:
src/content/devops/images/my-image.jpg

# Reference in markdown:
![Description](/images/devops/my-image.jpg "Caption")
```

### Test Locally

```bash
cd src
make devserver
# Check http://localhost:8100
```

### Deploy

```bash
git add .
git commit -m "Add new article"
git push origin main
# Render auto-deploys
```

## Performance Optimization (Later)

After adding real content:

1. **Optimize Images**:
   - Convert to WebP
   - Compress to < 500KB each
   - Use responsive sizes

2. **Run Lighthouse**:
   ```bash
   # Open site in Chrome
   # DevTools → Lighthouse → Run audit
   # Target: Performance ≥95
   ```

3. **Check Mobile**:
   - Test on actual devices
   - Use Chrome DevTools mobile emulation
   - Verify readable text and touch targets

## Ongoing Maintenance

### Regular Updates

```bash
# Update dependencies periodically
uv sync --upgrade

# Test locally
cd src && make devserver

# If all good, commit and push
git add pyproject.toml uv.lock
git commit -m "Update dependencies"
git push
```

### Content Workflow

1. Write locally in markdown
2. Test with `make devserver`
3. Commit and push
4. Render auto-deploys

### Monitor Site

- Check Render dashboard for build status
- Test live site after deployments
- Monitor for broken links periodically

## Getting Help

- **Build Issues**: Check Render build logs
- **Theme Issues**: See [pelican-alchemy docs](https://github.com/nairobilug/pelican-alchemy)
- **Pelican Issues**: See [Pelican docs](https://docs.getpelican.com/)
- **Questions**: Open GitHub issue or contact via website

## Checklist Before Going Live

- [ ] Update all personal information (bio, contact, social links)
- [ ] Add or replace sample content with real articles
- [ ] Add profile photo (optional)
- [ ] Test all navigation links
- [ ] Test on mobile device or emulator
- [ ] Review 404 page
- [ ] Check that feeds work (/feeds/all.atom.xml)
- [ ] Push to GitHub
- [ ] Configure Render.com
- [ ] Test live deployment
- [ ] Configure custom domain (if applicable)
- [ ] Run Lighthouse audit
- [ ] Share with others! 🎉

---

**You're all set!** The website is ready to deploy and use. Good luck with your portfolio! 🚀

