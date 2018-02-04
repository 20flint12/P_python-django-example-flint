
from django.contrib.auth import get_user_model

from rest_framework import serializers

from astrofactor import settings
from astrouser.models import UserProfile
from engine.models import MoonZodiacContent, MoonZodiac, MoonDayContent, MoonDay, SummaryFactor, Observer


# ========================= User, UserProfile =================================

class UserSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="api:user-detail",
    )

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'url',
            'first_name',
            'email',
            'is_staff',
            # 'related_account',
        )


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="api:userprofile-detail",
    )

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'url',
            # 'account',
            'user_name',
            'user_surname',
            'add_email',
            'is_active',
            # 'related_observer',
        )


# ========================= MoonZodiac ========================================

class MoonZodiacContentSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="api:moonzodiaccontent-detail",
    )

    class Meta:
        model = MoonZodiacContent
        # fields = '__all__'
        fields = (
            'id',
            'url',
            # 'moonzodiac',
            'title',
            'text',
            'image',
        )


class MoonZodiacSerializer(serializers.HyperlinkedModelSerializer):
    # moonzodiaccontents = MoonZodiacContentSerializer(source='moonzodiaccontent_set', many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(
        view_name="api:moonzodiac-detail",
    )

    related_mzcontent = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:moonzodiaccontent-detail',
    )

    # summaryfactor = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='api:summaryfactor-detail',
    # )

    class Meta:
        model = MoonZodiac
        fields = (
            'id',
            'url',
            # 'summaryfactor',
            'title',
            'zodiac_choice',
            'related_mzcontent',
        )


# ========================= MoonDay ===========================================

class MoonDayContentSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="api:moonzodiaccontent-detail",
    )

    class Meta:
        model = MoonDayContent
        # fields = '__all__'
        fields = (
            'id',
            'url',
            # 'moonday',
            'title',
            'description',
            'image',
        )


class MoonDaySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MoonDay
        fields = (
            'id',
            'url',
            'summaryfactor',
            'title',
            'quality',
            'day_choice',
            'related_mdcontent',
        )


# ========================= SummaryFactor =====================================

class SummaryFactorSerializer(serializers.HyperlinkedModelSerializer):
    # moonzodiacs = MoonZodiacSerializer(source='moonzodiac_set', many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(
        view_name="api:summaryfactor-detail",
    )

    class Meta:
        model = SummaryFactor
        fields = (
            'id',
            'url',
            'marked_at',
            'title',
            # 'related_mzodiac',
            # 'related_mday',
        )


class ObserverSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="api:summaryfactor-detail",
    )

    class Meta:
        model = Observer
        fields = (
            'id',
            'url',
            # 'userprofile',
            'created_at',
            'updated_at',
            'title',
            'longitude',
            'latitude',
            'timezone_name',
        )

