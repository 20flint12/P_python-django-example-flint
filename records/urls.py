from django.conf import settings
from django.conf.urls import url, include

import records
from records import views


urlpatterns = [

    url(r'^search-form/$', records.views.search_form),
    url(r'^search/$',      records.views.search),
    url(r'^search2/$',     records.views.search2),
    url(r'^news/$',        records.views.news),
    url(r'^weather/$',     records.views.weather),

    url(r'^wchart/$',                   records.views.weather_chart),
    # url(r'^wchart/(?P<num>[0-9]{4})/$', records.views.weather_chart),
    # url(r'^wchart/(?P<num>[0-9]{2})/$', records.views.weather_chart),

    url(r'^clear/$',                        records.views.clear_weather_data),
    url(r'^clear/([0-9]{4})/$',             records.views.clear_weather_data),
    url(r'^clear/([0-9]{4})/([0-9]{4})/$',  records.views.clear_weather_data),

    url(r'^clear/(?P<numfirst>[0-9]{4})/$', records.views.clear_weather_data),
    url(r'^clear/(?P<numfirst>\w+)/$',      records.views.clear_weather_data),

]


