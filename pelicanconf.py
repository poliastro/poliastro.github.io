#!/usr/bin/env python

AUTHOR = 'poliastro developer team'
SITENAME = 'poliastro'
SITESUBTITLE = u'poliastro website'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Madrid'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
INDEX_SAVE_AS = "blog/index.html"

DEFAULT_PAGINATION = 10

#SUMMARY_USE_FIRST_PARAGRAPH = True
SUMMARY_MAX_LENGTH = 140

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md', 'ipynb')
#PLUGINS = ['ipynb.markup']

MARKUP = ['md']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'pelican.plugins.liquid_tags',
]
IGNORE_FILES = ['.ipynb_checkpoints']

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# THEME SETTINGS
THEME = './theme/'

# HEAD MENU PAGES
DOCS_PAGE = 'https://docs.poliastro.space/en/latest/'
COMMUNITY_PAGE = 'http://chat.poliastro.space/'
TUTORIALS_PAGE = 'https://beta.mybinder.org/v2/gh/poliastro/poliastro/main?filepath=index.ipynb'
BLOG_PAGE = 'blog/index.html'
CODE_PAGE = 'https://github.com/poliastro/poliastro'
ARCHIVES_PAGE = 'archives.html'
ABOUT_PAGE = 'pages/about-poliastro.html'
MASTODON_URL = 'https://fosstodon.org/@poliastro'
GITHUB_USERNAME = 'poliastro'
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ISSO_HOST = 'localhost:1234'

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Footer info

LICENSE_URL = "https://github.com/poliastro/poliastro.github.io/blob/sources/LICENSE"
LICENSE = "CC-BY for content and MIT for code"
