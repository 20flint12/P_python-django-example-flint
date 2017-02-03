
from django.contrib.auth import get_user_model

from rest_framework import serializers

from astrofactor import settings
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


# ========================= MoonZodiac ========================================

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
            'related_mzcontent',
        )


# ========================= MoonDay ===========================================

class MoonDayContentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.MoonDayContent
        fields = (
            'id',
            'mdcontent',
            'title',
            'text',
            'image',
        )


class MoonDaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.MoonDay
        fields = (
            'id',
            'mday',
            'title',
            'day_choice',
            'related_mdcontent',
        )


# ========================= SummaryFactor =====================================

class SummaryFactorSerializer(serializers.HyperlinkedModelSerializer):
    # moonzodiacs = MoonZodiacSerializer(source='moonzodiac_set', many=True, read_only=True)

    class Meta:
        model = models.SummaryFactor
        fields = (
            'id',
            'marked_at',
            'title',
            # 'moonzodiacs',
            'related_mzodiac',
        )


class PlaceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Place
        fields = (
            'id',
            # 'profile',
            'created_at',
            'updated_at',
            'title',
            'longitude',
            'latitude',
            'timezone_name',

        )

