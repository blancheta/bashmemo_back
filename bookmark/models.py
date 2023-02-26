from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Organisation
# Name

# User
# email
# password
# username


class Keyword(models.Model):
    name = models.CharField(max_length=20, blank=True, null=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

# Keyword
# id
# name


class Bookmark(models.Model):
    command = models.CharField(max_length=255, blank=True, null=False)
    count = models.IntegerField(default=0)
    keywords = models.ManyToManyField(Keyword, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.command

    def __repr__(self):
        return self.command


class Organisation(models.Model):
    name = models.CharField(max_length=100, blank=True, null=False)
    bookmarks = GenericRelation(Bookmark)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bookmarks = GenericRelation(Bookmark)
    organisation = models.ForeignKey(Organisation, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username

# owner (could be a user or an organisation)
# command
# count
# keywords

