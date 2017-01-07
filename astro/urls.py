from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


##############################################################
import views

import polls.urls

admin.autodiscover()


urlpatterns = [
    url(r'^polls/', include(polls.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('astrouser.urls')),

    url(r'^', include('records.urls')),
]


urlpatterns += [

    # (r'^hello/$',   views.hello),  ##############################
    url(r'^time/$',    views.current_datetime),
    url(r'^scrape/$',  views.scrape_data_req),
    url(r'^meta/$',    views.display_meta),

    url(r'^main/$',    views.main_index),

    # (r'^charts/simple.png$', 'myapp.views.charts.simple'),
    url(r'^charts/$',  views.my_simple),
]


urlpatterns += staticfiles_urlpatterns()
