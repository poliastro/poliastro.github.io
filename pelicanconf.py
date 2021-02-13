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
AUTHOR_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'

# Set the article URL
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DEFAULT_PAGINATION = 10

#SUMMARY_USE_FIRST_PARAGRAPH = True
SUMMARY_MAX_LENGTH = 140

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#MARKUP = ('md', 'ipynb')
#PLUGINS = ['ipynb.markup']

MARKUP = ['md']
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = [
    'summary',       # auto-summarizing articles
    'feed_summary',  # use summaries for RSS, not full articles
    'pelican.plugins.liquid_tags',
]
IGNORE_FILES = ['.ipynb_checkpoints']

# for liquid tags
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# THEME SETTINGS
THEME = './theme/'

ABOUT_PAGE = '/pages/about-poliastro.html'
#TWITTER_USERNAME = 'poliastro'
GITHUB_USERNAME = 'poliastro'
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

ISSO_HOST = 'localhost:1234'

ENABLE_MATHJAX = True

STATIC_PATHS = ['images', 'figures', 'videos', 'downloads', 'favicon.ico', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Footer info

LICENSE_URL = "https://github.com/poliastro/poliastro.github.io-source/blob/master/LICENSE"
LICENSE = "CC-BY for content and MIT for code"
