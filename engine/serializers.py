from django.contrib.auth.models import User

from rest_framework import serializers

from lmcback.models import Language
from . import models

from rest_framework_recursive.fields import RecursiveField


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            # 'url',
            'username',
            'first_name',
            'email',
            'is_staff'
        )


class ZodiacContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ContentImage
        fields = (
            'id',
            'content',
            'title',
            'image',
            'image_loc',
        )


class MoonZodiacSerializer(serializers.HyperlinkedModelSerializer):
    content = ZodiacContentSerializer(source='zodiaccontent_set', many=True, read_only=True)

    class Meta:
        model = models.Content
        fields = (
            'id',
            'name',
            'zodiac',
            'content',
        )


# class LanguageSerializer(serializers.HyperlinkedModelSerializer):
#     contents = ContentSerializer(source='content_set', many=True, read_only=True)
#     # user = serializers.ReadOnlyField(source='user.username')
#
#     class Meta:
#         model = Language
#         fields = (
#             'id',
#             'user',
#             'title',
#             'language_file',
#             'send_email',
#             'send_to_email',
#             'contents',
#         )


# class SectionSerializer(serializers.HyperlinkedModelSerializer):
#     contents = ContentSerializer(source='content_set', many=True, read_only=True)
#
#     # children = serializers.SerializerMethodField()
#
#     # def get_children(self, obj):
#     #     return [SectionSerializer(child).data for child in obj.section_set.all()]
#
#     children_section = serializers.ListSerializer(read_only=True, child=RecursiveField())
#
#     class Meta:
#         model = models.Section
#         fields = (
#             'id',
#             'parent',
#             'title',
#             'has_subsections',
#             # 'children',
#             'contents',
#             'children_section',
#         )


# class RecursiveModelSerializer(serializers.ModelSerializer):
#
#     # parent = RecursiveField(allow_null=True, read_only=True)
#     children_item = serializers.ListSerializer(read_only=True, child=RecursiveField())
#
#     # children = serializers.SerializerMethodField()
#     #
#     # def get_children(self, obj):
#     #     # qs = obj.recursivemodel_set.all()
#     #     # res = []
#     #     # for child in qs:
#     #     #     ser = RecursiveModelSerializer(child)
#     #     #     res.append(ser.data)
#     #     # return res
#     #     return [RecursiveModelSerializer(child).data for child in obj.recursivemodel_set.all()]
#
#     class Meta:
#         model = RecursiveModel
#         fields = (
#             'name',
#             # 'parent',
#             # 'children',
#             'children_item',
#         )


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


# class WaterBoardSerializer(serializers.Serializer):
#
#     location = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     amount = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     date = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     time = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     locale = serializers.CharField(required=False, allow_blank=True, max_length=100)
#
#     def create(self, validated_data):
#         """
#         //Create and return a new `Snippet` instance, given the validated data.
#         Receives:
#         {
#           "location": "Kharkiv",
#           "amount": "123",
#           "date": "sdgfsdafgsd",
#           "time": "ds3436gsd",
#           "locale": "language"
#         }
#         """
#         # return Snippet.objects.create(**validated_data)
#         return validated_data
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         # instance.title = validated_data.get('title', instance.title)
#         # instance.code = validated_data.get('code', instance.code)
#         # instance.linenos = validated_data.get('linenos', instance.linenos)
#         # instance.save()
#         return instance



