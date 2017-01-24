from django.contrib.auth.models import User

from rest_framework import serializers

import astrouser.models
from . import models


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = astrouser.User
#         fields = (
#             'id',
#             # 'url',
#             'username',
#             'first_name',
#             'email',
#             'is_staff'
#         )


class MoonZodiacContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.MoonZodiacContent
        fields = (
            'id',
            'title',
            'text',
            'image',
        )


class MoonZodiacSerializer(serializers.HyperlinkedModelSerializer):
    content = MoonZodiacContentSerializer(source='moonzodiaccontent_set', many=True, read_only=True)

    class Meta:
        model = models.MoonZodiac
        fields = (
            'id',
            'title',
            'zodiac_choice',
            'content',
        )
