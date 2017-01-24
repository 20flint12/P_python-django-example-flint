
from django.contrib.auth.models import User

from rest_framework import viewsets

from . import serializers, models

from rest_framework import permissions
# from lmcback.permissions import IsOwnerOrReadOnly


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     This endpoint presents the users in the system.
#
#     As you can see, the collection of snippet instances owned by a user are
#     serialized using a hyperlinked representation.
#     """
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer


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


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

