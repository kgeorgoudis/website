# 🚀 Deployment Checklist - Blacklines.gr

## Pre-Deployment (Do This First)

### ✅ Already Complete
- [x] Dependencies installed
- [x] Theme configured
- [x] Content structure created
- [x] Sample content added
- [x] Social links updated in pelicanconf.py
- [x] Contact information updated in pages
- [x] Navigation configured
- [x] Security headers configured
- [x] Local build tested
- [x] Development server tested

### 🎯 Optional Before Deploying
- [ ] Add profile photo: `src/content/images/profile.jpg`
- [ ] Customize About page bio
- [ ] Replace or keep sample articles
- [ ] Add your own articles (optional)

## Deployment Steps

### Step 1: Push to GitHub

```bash
cd /Users/A200014545/code/Personal/www.blacklines.gr/website

# Check status
git status

# Add all files
git add .

# Commit
git commit -m "Complete website implementation with personal info"

# Push to main
git push origin main
```

### Step 2: Configure Render.com

1. Go to https://render.com
2. Sign in or create account
3. Click "New +" → "Static Site"
4. Click "Connect account" for GitHub
5. Select repository: `website` (or your repo name)
6. Configure:

**Settings to Enter:**
```
Name: blacklines
Branch: main
Build Command: cd src && uv run pelican content -s publishconf.py
Publish Directory: src/output
Auto-Deploy: Yes
```

7. Click "Create Static Site"
8. Wait 2-3 minutes for build

### Step 3: Update Site URL

After deployment, Render gives you a URL like:
`https://blacklines.onrender.com`

Update this in your code:

**File: `src/publishconf.py`**
```python
SITEURL = "https://blacklines.onrender.com"  # Replace with your actual URL
```

Then:
```bash
git add src/publishconf.py
git commit -m "Update production site URL"
git push origin main
```

Render will auto-rebuild (takes ~2 min).

### Step 4: Test Live Site

Visit your Render URL and check:
- [ ] Homepage loads
- [ ] Navigation works
- [ ] All pages accessible
- [ ] Social links work
- [ ] About page displays correctly
- [ ] Contact page displays correctly
- [ ] Sample articles render
- [ ] Images display (if any)
- [ ] 404 page works (visit /nonexistent)
- [ ] Mobile view looks good

### Step 5: Custom Domain (Optional)

If you want to use `blacklines.gr`:

1. **In Render Dashboard**:
   - Go to your static site
   - Settings → Custom Domains
   - Click "Add Custom Domain"
   - Enter: `blacklines.gr` or `www.blacklines.gr`
   - Note the DNS instructions

2. **In Your DNS Provider**:
   - Add CNAME or A record as instructed
   - Wait for DNS propagation (can take 24-48 hours)

3. **Update Site URL**:
   ```python
   # src/publishconf.py
   SITEURL = "https://blacklines.gr"
   ```
   
   Commit and push.

4. **Enable HTTPS** (automatic on Render)

## Post-Deployment

### Verify Everything Works
- [ ] Visit live site
- [ ] Test all links
- [ ] Check mobile view
- [ ] Test social media links
- [ ] Share with a friend for feedback

### Run Performance Check
1. Open site in Chrome
2. Open DevTools (F12)
3. Go to Lighthouse tab
4. Click "Generate report"
5. Target scores:
   - Performance: ≥95
   - Accessibility: ≥90
   - Best Practices: ≥95
   - SEO: ≥95

### Share Your Site
- [ ] Update social media profiles with link
- [ ] Add to LinkedIn profile
- [ ] Share on relevant platforms
- [ ] Add to GitHub profile README

## Ongoing Maintenance

### Adding New Content

1. **Create content file locally**:
   ```bash
   # Example: new DevOps article
   src/content/devops/my-new-article.md
   ```

2. **Test locally**:
   ```bash
   cd src
   make devserver
   # Visit http://localhost:8100
   ```

3. **Deploy**:
   ```bash
   git add .
   git commit -m "Add new article: My New Article"
   git push origin main
   # Render auto-deploys
   ```

### Regular Updates

**Monthly**:
- [ ] Update dependencies: `uv sync --upgrade`
- [ ] Test locally
- [ ] Push if everything works

**As Needed**:
- [ ] Add new content
- [ ] Update existing content
- [ ] Optimize images
- [ ] Check for broken links

## Troubleshooting

### Build Fails on Render

**Check build logs in Render dashboard**

Common issues:
- Syntax error in markdown frontmatter
- Missing required fields (Title, Date, Category)
- Invalid Python in config files

### Site Deploys But Looks Wrong

- Check SITEURL in publishconf.py matches deployment URL
- Verify static.json is in output directory
- Check Render build logs for warnings

### Images Not Loading

- Verify images are in `src/content/images/`
- Check image paths in markdown start with `/images/`
- Ensure images are committed to git
- Check file names (no spaces)

### Styles Not Loading

- Clear browser cache
- Check theme is installed: `uv run pip list | grep alchemy`
- Rebuild: `cd src && make clean && make html`

## Quick Commands Reference

```bash
# Local development
cd src && make devserver

# Production build
cd src && make publish

# Clean and rebuild
cd src && make clean && make html

# Check build
cd src && uv run pelican content -s pelicanconf.py

# Update dependencies
uv sync

# Deploy to production
git add . && git commit -m "Update" && git push origin main
```

## Support Resources

- **FINAL_SUMMARY.md** - Complete implementation details
- **README.md** - Full documentation
- **QUICKSTART.md** - Quick reference
- **NEXT_STEPS.md** - Detailed next actions
- **Render Docs**: https://render.com/docs/static-sites
- **Pelican Docs**: https://docs.getpelican.com/

## Success Criteria

Your deployment is successful when:
- ✅ Site is live and accessible
- ✅ All pages load correctly
- ✅ Navigation works
- ✅ Social links function
- ✅ Mobile view is responsive
- ✅ Lighthouse scores meet targets
- ✅ HTTPS is enabled
- ✅ Auto-deploy works on push

---

## Ready to Deploy?

**You have everything you need!**

1. ✅ Code is ready
2. ✅ Configuration is set
3. ✅ Documentation is complete
4. ✅ Personal info is updated

**Just follow the steps above and you'll be live in under 10 minutes!**

🚀 **Good luck with your deployment!** 🚀

---

*Last updated: February 10, 2026*  
*Status: Ready to Deploy*

