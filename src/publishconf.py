# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
# Update this with your actual Render.com URL or custom domain
SITEURL = "https://blacklines.onrender.com"  # Replace with actual Render URL or custom domain
RELATIVE_URLS = False

# Feed generation for production
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

# Clean output directory before building
DELETE_OUTPUT_DIRECTORY = True

# Optimization settings
LOAD_CONTENT_CACHE = False
