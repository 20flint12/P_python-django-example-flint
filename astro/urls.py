from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
##############################################################

import polls.urls


admin.autodiscover()

urlpatterns = [
    url(r'^polls/', include(polls.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/', include('astrouser.urls')),

    url(r'^records/', include('records.urls')),
    url(r'^reminder/', include('reminder.urls')),

    url(r'^engine/', include('engine.urls')),
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )