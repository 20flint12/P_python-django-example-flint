from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


##############################################################
# from mysite import views
import views
# from polls.models import Poll
# from my_tests import views
##############################################################


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('',

    (r'^search-form/$', 'records.views.search_form'),
    (r'^search/$',      'records.views.search'),
    (r'^search2/$',     'records.views.search2'),
    (r'^news/$',        'records.views.news'),

)


urlpatterns += patterns('',

    # (r'^hello/$',   views.hello),  ##############################
    (r'^time/$',    views.current_datetime),
    (r'^scrape/$',  views.scrape_data_req),
    (r'^astro/$',   views.astro_req),
    (r'^meta/$',    views.display_meta),
    (r'^json/$',    views.json_req),

    (r'^main/$',    views.main_index),

    # (r'^charts/simple.png$', 'myapp.views.charts.simple'),
    (r'^charts/$',  views.my_simple),

)


urlpatterns += staticfiles_urlpatterns()
