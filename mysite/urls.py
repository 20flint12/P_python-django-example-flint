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
    # url(r'^polls/', include('polls.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)


# urlpatterns += patterns('',
#
#     (r'^search-form/$', 'records.views.search_form'),
#     (r'^search/$',      'records.views.search'),
#     (r'^search2/$',     'records.views.search2'),
#     (r'^news/$',        'records.views.news'),
#     (r'^weather/$',     'records.views.weather'),
#
#     (r'^wchart/$',      'records.views.weather_chart'),
# )


urlpatterns += patterns('',

    # (r'^hello/$',   views.hello),  ##############################
    (r'^time/$',    views.current_datetime),
    (r'^scrape/$',  views.scrape_data_req),
    (r'^astro/$',   views.astro_req),
    (r'^meta/$',    views.display_meta),
    (r'^json/$',    views.json_req),

    (r'^main/$',    views.main_index),

    # (r'^charts/$',  views.my_simple),

    # (r'^email/$',   views.my_email),

)


urlpatterns += staticfiles_urlpatterns()




import logging
logging.basicConfig()


import email_ASR as mail

# from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

# sched = BlockingScheduler()
sched = BackgroundScheduler()

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three hundreds minutes.')
    mail.email_reminder()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=5)
def scheduled_job():
    print('This job is run every weekday at 5pm.')


# sched.configure(options_from_ini_file)
sched.start()