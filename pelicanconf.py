#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Dillon Brout'
SITENAME = 'AstroApps'
SITEURL = 'https://djbrout.github.io/astroapps'

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
LINKS = (('Home', 'index.html'),
         ('Archives', 'archives.html'),
         ('Tags', 'tags.html'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = "/Users/djbrout/Dropbox/astroapps/ghpages/themes/pelican-themes/aboutwilson"
#THEME = "/Users/djbrout/Dropbox/astroapps/ghpages/themes/pelican-themes/voce"




PLUGIN_PATHS = ["plugins", "/Users/djbrout/Dropbox/astroapps/ghpages/pelican-plugins/"]
PLUGINS = ["assets"]

DISQUS_SITENAME = "astroapps"


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True