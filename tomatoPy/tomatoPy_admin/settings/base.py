# -*- coding: utf-8 -*-
# tomatoPy_admin

__author__ = 'Michael Bolay'

import os
import json

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# JSON-based secrets module
with open(os.path.join(BASE_DIR, "secrets.json")) as f:
    secrets = json.loads(f.read())


def get_secret(setting, _secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return _secrets[setting]
    except KeyError:
        error_message = "Set the {0} entry in secrets.json file.".format(setting)
        raise ImproperlyConfigured(error_message)

# get the secret key from secrets.json
SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'json_field',
    'bootstrap3',
    'rest_framework',
    #'rest_framework.authtoken',
    'accounts',
    'remote_settings',
    'tvshows',
    'movies'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'accounts.authentication.ClientTokenAuthentication',
#    ),
#    'DEFAULT_PERMISSION_CLASSES': (
#        'rest_framework.permissions.IsAuthenticated',
#    )
}

ROOT_URLCONF = 'tomatoPy_admin.urls'

WSGI_APPLICATION = 'tomatoPy_admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/remote_settings/#databases
# Databases are set in local.py or production.py

DATABASES = {
}

# Templates
TEMPLATE_DIRS = ("templates", )

# Login
LOGIN_URL = "/accounts/login/"

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Zurich'

# Internationalization
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
MEDIA_ADMIN_URL = "/../media"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')


URL_PATTERNS = ()

# ADDONS SETTINGS

# BOOTSTRAP

BOOTSTRAP3_DEFAULTS = {
    'jquery_url': '//code.jquery.com/jquery.min.js',
    'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.1.1/',
    'css_url': None,
    'theme_url': None,
    'javascript_url': None,
    'javascript_in_head': False,
    'include_jquery': False,
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-4',
    'set_required': True,
    'form_required_class': 'inputError1',
    'form_error_class': 'inputError1',
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}

ADMIN_RELATION_COLORS = {
    "unused": "#E5482D",
    "used": "#2DA8E5",
    "sync": "#8AE62E"
}