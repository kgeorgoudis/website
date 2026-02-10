AUTHOR = 'Konstantinos Georgoudis'
SITENAME = 'Blacklines.gr'
SITEURL = "http://localhost:8100"

PATH = "content"

TIMEZONE = 'Europe/Athens'

DEFAULT_LANG = 'en'

# Theme configuration
import os
import sys

# Get alchemy theme path from the package
THEME = os.path.join(sys.prefix, 'lib', 'python3.12', 'site-packages', 'alchemy')
THEME_CSS_OVERRIDES = ['static/css/custom.css']
SITESUBTITLE = 'DevOps, Sketchnotes, and DIY Creations'
SITEIMAGE = '/images/profile.jpg width=200 height=200'
DESCRIPTION = 'A portfolio showcasing DevOps articles, sketchnotes, urban sketches, and woodworking projects by Konstantinos Georgoudis'

# Content paths
ARTICLE_PATHS = ['devops', 'sketchnotes', 'diy']
PAGE_PATHS = ['pages']
STATIC_PATHS = ['images', 'extra']

# Copy static.json to output root for Render.com
EXTRA_PATH_METADATA = {
    'extra/static.json': {'path': 'static.json'},
}

# URL structure
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Navigation
MENUITEMS = (
    ('Home', '/'),
    ('DevOps', '/devops/'),
    ('Sketchnotes', '/sketchnotes/'),
    ('DIY & Crafts', '/diy/'),
    ('Contact', '/contact/'),
)

# Social links
SOCIAL = (
    ('github', 'https://github.com/kgeorgoudis'),
    ('linkedin', 'https://linkedin.com/in/kgeor'),
    ('instagram', 'https://www.instagram.com/k.georgoudis'),
    ('substack', 'https://kgeor.substack.com/'),
    ('envelope', 'mailto:kgeor@blacklines.gr'),
)

# Blogroll - remove default links
LINKS = ()

DEFAULT_PAGINATION = 10

# Development setting
RELATIVE_URLS = True
