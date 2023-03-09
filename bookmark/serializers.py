from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import CharField, ModelSerializer

from bookmark.models import Bookmark, Keyword, User
from rest_framework.authtoken.models import Token


class KeywordSerializer(ModelSerializer):

    class Meta:
        model = Keyword
        fields = ['name']


class UserCreateSerializer(ModelSerializer):
    token = CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'token']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        token, state = Token.objects.get_or_create(user_id=instance.id)
        data["token"] = token.key
        return data


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'organisation']


class BookmarkSerializer(ModelSerializer):

    keywords = KeywordSerializer(many=True, required=False)

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
