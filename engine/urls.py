
from django.conf.urls import url, include
from rest_framework import routers

from engine import views
from . import viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'users', viewsets.UserViewSet)

router.register(r'moon-zodiacs', viewsets.MoonZodiacViewSet)
router.register(r'moon-zodiac-contents', viewsets.MoonZodiacContentViewSet)

router.register(r'moon-days', viewsets.MoonDayViewSet)
router.register(r'moon-day-contents', viewsets.MoonDayContentViewSet)

router.register(r'summary-factor', viewsets.SummaryFactorViewSet)
router.register(r'place-observer', viewsets.PlaceViewSet)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


place_urls = [
    url(r'^edit/$', views.PlaceEditView.as_view(), name='edit_place'),
    url(r'^moment/$', views.MomentView.as_view(), name='edit_moment'),
    # url(r'^edit/api/$', views.AjaxEditModule.as_view()),
    # url(r'^delete/$', views.ModuleDeleteView.as_view(), name='delete_module'),
    # url(r'^details/$', views2.ModuleDetailsView.as_view(), name='details_module'),
]


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^new-place/$', views.NewPlaceView.as_view(), name='new_place'),
    url(r'^place/(?P<place_id>\d+)/', include(place_urls)),

]
