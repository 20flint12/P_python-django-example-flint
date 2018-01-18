#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
print("### BASE_DIR=", BASE_DIR)
# print("PROJECT_ROOT=", PROJECT_ROOT)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '_rs%0pq1+b#@-&amp;lbd0y%hb_t9w(tz5n-hpv1b!k=&amp;0=@ve*t7n'
###############################################################################

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'astro-factor.herokuapp.com']

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# *****************************************************************************

ADMIN_EMAIL = '20flint12@gmail.com'
APP_EMAIL = '20flint12@gmail.com'
# DEFAULT_FROM_EMAIL = '20flint12@gmail.com'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'akuta.m9@gmail.com'
# EMAIL_HOST_PASSWORD = 'ddipass2016changed'
# EMAIL_PORT = 465
# EMAIL_USE_SSL = True


EMAIL_SENDER   = "astroreminder@gmail.com"
EMAIL_USERNAME = "astroreminder@gmail.com"
EMAIL_PASSWORD = "95dd2d301"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'astroreminder@gmail.com'
DEFAULT_FROM_EMAIL = 'astroreminder@gmail.com'
SERVER_EMAIL = 'astroreminder@gmail.com'
EMAIL_HOST_PASSWORD = '95dd2d301'

# *****************************************************************************


ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    print("ON_HEROKU")
    # DATABASE_URL = 'postgresql:///postgresql'
else:
    print("ON_LOCAL")


# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'rest_framework',

    'astrofactor',
    'astrouser',
    'records',
    'polls',
    'grabber',
    'engine',
    'reminder',
]

# INSTALLED_APPS += ['tastypie']

# MIDDLEWARE_CLASSES = [
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# if True:
#     INSTALLED_APPS += ['debug_toolbar']
#     MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware']
#     INTERNAL_IPS = ['127.0.0.1']
#     DEBUG_TOOLBAR_PATCH_SETTINGS = False


# List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# #     'django.template.loaders.eggs.Loader',
# )

# TEMPLATE_DEBUG = DEBUG

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [
        #     '{0}/templates/'.format(PROJECT_ROOT),
        #     '{0}/my_templates/'.format(PROJECT_ROOT),
        # ],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'debug': DEBUG,
        },
    },
)

AUTH_USER_MODEL = 'astrouser.User'
LOGIN_URL = '/account/sign-in/'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'astrofactor.wsgi.application'


# -----------------------------------------------------------------------------
DATABASE_URL = 'postgresql:///flint'
DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# Update database configuration with $DATABASE_URL.
# db_from_env = dj_database_url.config(default=DATABASE_URL, conn_max_age=500)
# DATABASES = {'default': db_from_env}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'flint',
#         'USER': 'flint',
#         'PASSWORD': '63933',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# print "DATABASES=", DATABASES

AUTH_PASSWORD_VALIDATORS = (
    # {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    # {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    # {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
)

TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'en-us'

# SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# URL that handles the media served from MEDIA_ROOT.
MEDIA_URL = '/media/'




# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "staticfiles"),
    os.path.join(BASE_DIR, "static"),
    # os.path.join(BASE_DIR, 'astrofactor/static'),
    # os.path.join(BASE_DIR, 'engine/static'),
]





# List of finder classes that know how to find static files in
# various locations.
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )

ROOT_URLCONF = 'astrofactor.urls'


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# =============================================================================


# import astro.config_ASR as conf
# import engine.astro_routines.geo_preload as geopr
# # import pprint
#
# geopr.GEO_PLACE_dict = geopr.read_config_to_geo(PROJECT_ROOT + "/" + conf.GEO_FILE)
# # print "conf.GEO_PLACE_dict=\n", pprint.pprint(geopr.GEO_PLACE_dict)


DATETIME_FORMAT = 'Y-m-d H:i'

DATETIME_INPUT_FORMATS ='%Y-%m-%d %H:%M:%S'     # '2006-10-25 14:30:59'


try:
    from .local_settings import *
except ImportError:
    pass

