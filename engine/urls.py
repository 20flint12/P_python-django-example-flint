
from django.conf.urls import url, include
from rest_framework import routers

from engine import views
from . import viewsets

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

# router.register(r'users', viewsets.UserViewSet)
# router.register(r'languages', viewsets.LanguageViewSet)
# router.register(r'sections', viewsets.SectionViewSet)
router.register(r'moon-zodiacs', viewsets.MoonZodiacViewSet)
router.register(r'moon-zodiac-contents', viewsets.MoonZodiacContentViewSet)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
