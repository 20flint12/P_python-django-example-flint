#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Django settings for mysite project.

import json
import os



PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


###############################################################################
#
# # redis server address
# # BROKER_URL = 'redis://localhost:6379/0'
# # store task results in redis
# # CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# task result life time until they will be deleted

CELERY_TASK_RESULT_EXPIRES = 7*86400  # 7 days
# needed for worker monitoring
CELERY_SEND_EVENTS = True
# where to store periodic tasks (needed for scheduler)
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
CELERY_RESULT_BACKEND = "djcelery.backends.database:DatabaseBackend"


# BROKER_URL = "amqp://guest:guest@localhost:5672//"
# BROKER_URL = 'amqp://guest:guest@localhost:15711//'
# BROKER_URL = 'django://'
# BROKER_URL = "amqp://guest@localhost//"



###############################################################################
# add following lines to the end of settings.py
import djcelery
djcelery.setup_loader()
###############################################################################


# https://www.cloudcontrol.com/dev-center/guides/python/add-on-credentials

try:
    # production settings
    f = os.environ['CRED_FILE']
    print "f=", f
    db_data = json.load(open(f))['MYSQLS']
    print "db_data=", db_data

    db_config = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_data['MYSQLS_DATABASE'],
        'USER': db_data['MYSQLS_USERNAME'],
        'PASSWORD': db_data['MYSQLS_PASSWORD'],
        'HOST': db_data['MYSQLS_HOSTNAME'],
        'PORT': db_data['MYSQLS_PORT'],
        'OPTIONS': {
            'sql_mode': 'TRADITIONAL',
            'charset': 'utf8',
            'init_command': 'SET '
                'storage_engine=INNODB,'
                'character_set_connection=utf8,'
                'collation_connection=utf8_bin'
                    }
    }
except KeyError, IOError:
    # development/test settings:
    db_config = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{0}/mysite.sqlite3'.format(PROJECT_ROOT),
    }







DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': db_config,
}

print "DATABASES=", DATABASES

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'read_default_file': 'mysql.cnf',
#         },
#     }
# }


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
# TIME_ZONE = 'Europe/Berlin'
TIME_ZONE = 'Europe/Kiev'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_rs%0pq1+b#@-&amp;lbd0y%hb_t9w(tz5n-hpv1b!k=&amp;0=@ve*t7n'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # './polls',
    # './records',
)

ROOT_URLCONF = 'mysite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATE_DIRS = (
    '{0}/templates/'.format(PROJECT_ROOT),
    '{0}/my_templates/'.format(PROJECT_ROOT),
    '{0}/front-end/'.format(PROJECT_ROOT),

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'gunicorn',
    'polls',
    'records',

    'djcelery',
    'kombu.transport.django',

    # 'celerytest',

)

# INSTALLED_APPS += ['tastypie']



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'



#==============================================================================
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'astroreminder@gmail.com'
DEFAULT_FROM_EMAIL = 'astroreminder@gmail.com'
SERVER_EMAIL = 'astroreminder@gmail.com'
EMAIL_HOST_PASSWORD = '95dd2d30'


#==============================================================================

import mysite.config_ASR as conf
import mysite.astro_routines.geo_preload as geopr
import pprint


# For cron
# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_geo_file = os.path.dirname(os.path.abspath(__file__)) + "/" + conf.GEO_FILE


conf.GEO_PLACE_dict = geopr.read_config_to_geo(path_geo_file)
print "conf.GEO_PLACE_dict=\n", pprint.pprint(geopr.GEO_PLACE_dict)
















