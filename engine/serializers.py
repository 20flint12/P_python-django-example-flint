from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import serializers

# import astrouser.models
import astrouser
from astro import settings
from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'url',
            'first_name',
            'email',
            'is_staff'
        )


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
    # moonzodiaccontents = MoonZodiacContentSerializer(source='moonzodiaccontent_set', many=True, read_only=True)

    class Meta:
        model = models.MoonZodiac
        fields = (
            'id',
            'mzodiac',
            'title',
            'zodiac_choice',
            # 'moonzodiaccontents',
            'mzodiac_content',
        )


class SummaryFactorSerializer(serializers.HyperlinkedModelSerializer):
    # moonzodiacs = MoonZodiacSerializer(source='moonzodiac_set', many=True, read_only=True)

    class Meta:
        model = models.SummaryFactor
        fields = (
            'id',
            'marked_at',
            'title',
            # 'moonzodiacs',
            'factor_mzodiac',
        )


