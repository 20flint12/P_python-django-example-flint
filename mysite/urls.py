from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


##############################################################
# from mysite import views
import views

import records.views
import polls.urls

# from polls.models import Poll
# from my_tests import views
##############################################################


admin.autodiscover()


# urlpatterns = patterns('',
#                        url(r'^polls/', include(polls.urls)),
#                        url(r'^admin/', include(admin.site.urls)),
#                        )

urlpatterns = [
    url(r'^polls/', include(polls.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [

    url(r'^search-form/$', records.views.search_form),
    url(r'^search/$',      records.views.search),
    url(r'^search2/$',     records.views.search2),
    url(r'^news/$',        records.views.news),
    url(r'^weather/$',     records.views.weather),

    url(r'^wchart/$',      records.views.weather_chart),
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
