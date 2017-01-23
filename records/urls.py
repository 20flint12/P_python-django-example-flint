from django.conf import settings
from django.conf.urls import url

from records import views


urlpatterns = [

    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^search2/$', views.search2),
    url(r'^news/$', views.news),
    url(r'^weather/$', views.weather),

    url(r'^wchart/$', views.weather_chart, name='wchart'),

    url(r'^static_image/$', views.static_image, name='static_image'),

    # url(r'^wchart/(?P<num>[0-9]{4})/$', records.views.weather_chart),
    # url(r'^wchart/(?P<num>[0-9]{2})/$', records.views.weather_chart),

    url(r'^clear/$',                        views.clear_weather_data),
    url(r'^clear/([0-9]{4})/$',             views.clear_weather_data),
    url(r'^clear/([0-9]{4})/([0-9]{4})/$',  views.clear_weather_data),

    url(r'^clear/(?P<numfirst>[0-9]{4})/$', views.clear_weather_data),
    url(r'^clear/(?P<numfirst>\w+)/$',      views.clear_weather_data),

]
