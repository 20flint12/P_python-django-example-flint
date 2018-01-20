
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from api import views
from . import viewsets


app_name = 'api'


# Create a router and register our viewsets with it.
router = DefaultRouter()

router.register(r'users', viewsets.UserViewSet)
router.register(r'user-profiles', viewsets.UserProfileViewSet)

router.register(r'moon-zodiacs', viewsets.MoonZodiacViewSet)
router.register(r'moon-zodiac-contents', viewsets.MoonZodiacContentViewSet)

router.register(r'moon-days', viewsets.MoonDayViewSet )
router.register(r'moon-day-contents', viewsets.MoonDayContentViewSet)

router.register(r'summary-factors', viewsets.SummaryFactorViewSet)
router.register(r'observers', viewsets.ObserverViewSet)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]



