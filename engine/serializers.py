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
            'mzcontent',
            'title',
            'text',
            'image',
        )


class MoonZodiacSerializer(serializers.HyperlinkedModelSerializer):
    mzcontent = MoonZodiacContentSerializer(source='mzcontent_set', many=True, read_only=True)

    class Meta:
        model = models.MoonZodiac
        fields = (
            'id',
            'mzodiac',
            'title',
            'zodiac_choice',
            'mzcontent',
        )


class SummaryFactorSerializer(serializers.HyperlinkedModelSerializer):
    mzodiac = MoonZodiacSerializer(source='mzodiac_set', many=True, read_only=True)

    class Meta:
        model = models.SummaryFactor
        fields = (
            'id',
            'marked_at',
            'title',
            'mzodiac',
        )


