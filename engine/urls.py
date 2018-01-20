
from django.conf.urls import url, include

from engine import views


app_name = 'engine'


observer_urls = [

    # http://127.0.0.1:8000/engine/observer/2/edit/
    url(r'^edit/$', views.ObserverEditView.as_view(), name='edit_observer'),

    url(r'^moment/$', views.MomentView.as_view(), name='edit_moment'),
    # url(r'^edit/api/$', views.AjaxEditModule.as_view()),
    # url(r'^delete/$', views.ModuleDeleteView.as_view(), name='delete_module'),
    # url(r'^details/$', views2.ModuleDetailsView.as_view(), name='details_module'),
]


urlpatterns = [

    url(r'^new-observer/$', views.NewObserverView.as_view(), name='new_observer'),

    # http://127.0.0.1:8000/engine/observer/2/
    url(r'^observer/(?P<place_id>\d+)/', include(observer_urls)),

]
