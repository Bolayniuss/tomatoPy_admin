# -*- coding: utf-8 -*-
# tomatoPy_admin

# Settings used for development
__author__ = 'Michael Bolay'
from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += ("debug_toolbar", )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "static"),
#)

URL_PATTERNS = (
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

