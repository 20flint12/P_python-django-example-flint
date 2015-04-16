from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



##############################################################
# from mysite import views
import views
# from polls.models import Poll
# from my_tests import views
##############################################################

# from ..astro_routines import ephem1
# from ...records import ephem1



admin.autodiscover()




urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)



urlpatterns += patterns('',

    # (r'^hello/$',   views.hello),  ##############################
    (r'^time/$',    views.current_datetime),
    (r'^scrape/$',  views.scrape_data_req),
    (r'^astro/$',   views.astro_req),
    (r'^meta/$',    views.display_meta),

    (r'^search-form/$', views.search_form),
    (r'^search/$',      views.search),
)



urlpatterns += staticfiles_urlpatterns()
