from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from bookmark.models import Bookmark, Keyword, User


class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'organisation']


class BookmarkSerializer(serializers.ModelSerializer):

    keywords = KeywordSerializer(many=True)

    class Meta:
        model = Bookmark
        fields = ['command', 'count', 'keywords', 'object_id']

    def create(self, validated_data):
        print(self.context['request'].headers['Authorization'])
        print(validated_data)
        data = validated_data.copy()
        keywords = data.pop("keywords")
        print(data)
        print(keywords)

        data['content_type'] = ContentType.objects.get(model='user')
        bookmark, created = Bookmark.objects.get_or_create(**data)
        if "keywords" in validated_data:
            for keyword in keywords:
                keyword, created = Keyword.objects.get_or_create(name=keyword["name"])
                bookmark.keywords.add(keyword)

        bookmark.save()
        return bookmark
