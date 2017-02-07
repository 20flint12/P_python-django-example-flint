
from django.contrib.auth import get_user_model

from rest_framework import serializers

from astrofactor import settings
from astrouser.models import UserProfile
from . import models


# ========================= User, UserProfile =================================

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'url',
            'first_name',
            'email',
            'is_staff',
            'related_account',
        )


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id',
            'account',
            'user_name',
            'user_surname',
            'add_email',
            'is_active',
            'related_observer',
        )


# ========================= MoonZodiac ========================================

class MoonZodiacContentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.MoonZodiacContent
        fields = (
            'id',
            'moonzodiac',
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
            'summaryfactor',
            'title',
            'zodiac_choice',
            'related_mzcontent',
        )


# ========================= MoonDay ===========================================

class MoonDayContentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.MoonDayContent
        fields = (
            'id',
            'moonday',
            'title',
            'text',
            'image',
        )


class MoonDaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.MoonDay
        fields = (
            'id',
            'summaryfactor',
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
            'related_mzodiac',
            'related_mday',
        )


class ObserverSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Observer
        fields = (
            'id',
            'userprofile',
            'created_at',
            'updated_at',
            'title',
            'longitude',
            'latitude',
            'timezone_name',
        )

