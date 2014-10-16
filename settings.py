# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os
from djangoappengine.utils import on_production_server

# Activate django-dbindexer for the default database
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': DATABASES['default']}
AUTOLOAD_SITECONF = 'indexes'

JAVASCRIPT_TRANSLATION_VERSION = 1

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dlklkhvi'

ALLOWED_HOSTS = ['']

LOGIN_URL = '/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/login_redirect_url/'
LOGIN_REDIRECT_URL_ADMIN = '/admin/'

from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('pt', _('Portuguese')),
)

GET_SOLO_TEMPLATE_TAG_NAME = 'get_config'
SOLO_CACHE = 'default'

SUMMERNOTE_CONFIG = {
    # Change editor size
    'width': '600',
    'height': '400',

    # Customize toolbar buttons
    'toolbar': [
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['fontsize', ['fontsize']],
        ['para', ['ul', 'ol', 'paragraph']],
        ['insert', ['link']],
    ],
}


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'filetransfers',

    'modeltranslation',
    'django_summernote',
    'solo',

    'main',
    'config',


    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.cache.FetchFromCacheMiddleware',
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'TIMEOUT': 0,
    },
    'dev': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

if on_production_server:
    CACHE_MIDDLEWARE_ALIAS = 'default'
    CACHE_MIDDLEWARE_SECONDS = 60
else:
    CACHE_MIDDLEWARE_ALIAS = 'dev'
    CACHE_MIDDLEWARE_SECONDS = 0

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

STATIC_URL = '/static/'
STATIC_ROOT = 'static/'

ROOT_URLCONF = 'urls'
