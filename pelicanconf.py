#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Dillon Brout'
SITENAME = 'AstroApps'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'EST5EDT'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "/Users/djbrout/Dropbox/astroapps/ghpages/themes/pelican-themes/aboutwilson"

PLUGIN_PATHS = ["plugins", "/Users/djbrout/Dropbox/astroapps/ghpages/pelican-plugins"]
PLUGINS = ["assets", "liquid_tags", "sitemap", "pelican_comment_system"]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True