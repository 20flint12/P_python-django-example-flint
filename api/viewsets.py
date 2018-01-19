from django.contrib.auth import get_user_model

from rest_framework import viewsets

from astrouser.models import UserProfile
from engine import models
from api import serializers


# from lmcback.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of snippet instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class MoonZodiacContentViewSet(viewsets.ModelViewSet):
    '''
    Post new content data, like:
    {
        "content_title": "Content title",
        "title": "Title4",
    }
    '''

    queryset = models.MoonZodiacContent.objects.all()
    serializer_class = serializers.MoonZodiacContentSerializer


class MoonZodiacViewSet(viewsets.ModelViewSet):
    '''
    Post new image data, like:
    {
        "content": "http://server/contents/2/"
        "title": "Image1",
    }
    '''

    queryset = models.MoonZodiac.objects.all()
    serializer_class = serializers.MoonZodiacSerializer


class MoonDayContentViewSet(viewsets.ModelViewSet):
    '''
    Post new content data, like:
    {
        "content_title": "Content title",
        "title": "Title4",
    }
    '''

    queryset = models.MoonDayContent.objects.all()
    serializer_class = serializers.MoonDayContentSerializer


class MoonDayViewSet(viewsets.ModelViewSet):
    '''
    Post new image data, like:
    {
        "content": "http://server/contents/2/"
        "title": "Image1",
    }
    '''

    queryset = models.MoonDay.objects.all()
    serializer_class = serializers.MoonDaySerializer


class SummaryFactorViewSet(viewsets.ModelViewSet):
    '''
    Post new image data, like:
    {
        "content": "http://server/contents/2/"
        "title": "Image1",
    }
    '''

    queryset = models.SummaryFactor.objects.all()
    serializer_class = serializers.SummaryFactorSerializer


class ObserverViewSet(viewsets.ModelViewSet):
    '''
    Post new place data, like:
    {

    }
    '''

    queryset = models.Observer.objects.all()
    serializer_class = serializers.ObserverSerializer


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

