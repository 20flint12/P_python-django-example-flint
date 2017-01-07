
from django.conf.urls import url
from reminder import views


urlpatterns = [

    url(r'^$', views.ReminderView.as_view(), name='reminder'),

    # (r'^hello/$',   views.hello),  ##############################
    url(r'^time/$', views.current_datetime, name='time'),
    url(r'^scrape/$', views.scrape_data_req, name='scrape'),
    url(r'^meta/$', views.display_meta, name='meta'),

    url(r'^main/$', views.main_index),

    # (r'^charts/simple.png$', 'myapp.views.charts.simple'),
    url(r'^charts/$', views.my_simple, name='charts'),

]
