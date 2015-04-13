from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



##############################################################
import views
# from polls.models import Poll
# from my_tests import views
# import my_tests.views
##############################################################
# from mysite.views import hello, current_datetime



admin.autodiscover()




urlpatterns = patterns(
    '',
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # (r'^hello/$',   views.hello),  ##############################
    (r'^time/$',    views.current_datetime),
    (r'^scrape/$',  views.scrape_data_req),
    (r'^astro/$',   views.astro_req),

)

urlpatterns += staticfiles_urlpatterns()
