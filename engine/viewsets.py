
from django.contrib.auth.models import User

from rest_framework import viewsets

from . import serializers, models

from rest_framework import permissions
from lmcback.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint presents the users in the system.

    As you can see, the collection of snippet instances owned by a user are
    serialized using a hyperlinked representation.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class SectionViewSet(viewsets.ModelViewSet):
    '''
    {
        "parent": null,
        "title": "New section 111",
        "has_subsections": false
    }
    '''

    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer

    filter_fields = ('id', 'title')

    def get_queryset(self):
        if self.action == 'list':
            return models.Section.objects.filter(parent__isnull=True)
        else:
            return self.queryset


class ContentViewSet(viewsets.ModelViewSet):
    '''
    Post new content data, like:
    {
        "language": "http://server/language/2/",
        "section": "http://server/sections/5/"
        "content_title": "Content title",
        "title": "Title4",
        "text": "some deccription",
    }
    '''

    queryset = models.Content.objects.all()
    serializer_class = serializers.ContentSerializer


class ContentImageViewSet(viewsets.ModelViewSet):
    '''
    Post new image data, like:
    {
        "content": "http://server/contents/2/"
        "title": "Image1",
        "image": "path_to_storage",
        "image_loc": "http://dbe63d5a.ngrok.io/images/axcela_imgs/2017/01/18/images.jpg",
    }
    '''

    queryset = models.ContentImage.objects.all()
    serializer_class = serializers.ContentImageSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    '''
    Post new image data, like:
    {
        "title": "Language name",
        "send_email": false,
        "send_to_email": "sdfsadfas@com.ua"
    }
    '''

    queryset = models.Language.objects.all()
    serializer_class = serializers.LanguageSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


# class RecursiveModelViewSet(viewsets.ModelViewSet):
#     queryset = models.RecursiveModel.objects.all()
#     serializer_class = serializers.RecursiveModelSerializer
#
#     def get_queryset(self):
#         return self.queryset

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

