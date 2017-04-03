#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Viral Parekh'
SITENAME = u'Viral Parekh'
SITEURL = 'https://researchweb.iiit.ac.in/~parekh.viral'
OUTPUT_PATH = '/research/ms/ms2k15/cse/parekh.viral/public_html/'
STATIC_PATHS = ['images', 'pdfs']
PATH = 'content'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = '/research/ms/ms2k15/cse/parekh.viral/site_builder/themes/pelican-hyde'
NEWEST_FIRST_ARCHIVES = True

#pelican-hyde specific
PROFILE_IMAGE='me.jpg'
BIO='Research Scholar @IIIT Hyderabad, Maker , Foodie, Pro Gujarati, Chef & Writer in progress.'
SOCIAL =( ('linkedin','https://www.linkedin.com/in/vparekh1'),
	  ('twitter', 'https://twitter.com/viralmparekh'),
          ('facebook', 'https://facebook.com/viral034'),
          ('github', 'https://github.com/viralparekh'),
          ('quora', 'https://www.quora.com/profile/Viral-Parekh'),
	  ('email','viral@live.in'),)

PLUGINS = ['pelican_gist']
