from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

##############################################################
import astrouser.urls
import polls.urls


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^account/', include(astrouser.urls)),
    # url(r'^account/', include(polls.urls)),

    url(r'^polls/', include(polls.urls)),

    url(r'^records/', include('records.urls')),
    url(r'^reminder/', include('reminder.urls')),
    url(r'^engine/', include('engine.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]