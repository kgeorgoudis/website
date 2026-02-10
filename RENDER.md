# Render.com Build Configuration
# This file documents the build settings for Render.com Static Site deployment

# Build Settings (configure in Render dashboard):
# - Build Command: cd src && uv run pelican content -s publishconf.py
# - Publish Directory: src/output
# - Environment: Python 3.12+

# Auto-Deploy:
# - Branch: main
# - Auto-deploy: Yes

# Environment Variables (if needed):
# None required for basic deployment

# Custom Domain:
# After deployment, you can add a custom domain in Render dashboard:
# 1. Go to your static site settings
# 2. Click "Custom Domains"
# 3. Add your domain (e.g., blacklines.gr or www.blacklines.gr)
# 4. Follow DNS configuration instructions
# 5. Update SITEURL in src/publishconf.py to match your custom domain

# Notes:
# - Render automatically installs uv if it detects pyproject.toml
# - Build should complete in under 3 minutes on free tier
# - HTTPS is automatically enabled
# - Static files are served via CDN

