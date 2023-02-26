from django.http import JsonResponse
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [AllowAny]


class LoginSuccessView(TemplateView):

    template_name = "login-success.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user.username)
        context['token'], created = Token.objects.get_or_create(user=self.request.user)
        return context


class UserDetailView(APIView):

    def get(self, request, *args, **kwargs):

        # Read token from Authorisation Header
        token = request.headers['Authorization'].replace("Bearer ", "")
        user = Token.objects.get(key=token).user

        bookmarks = []
        for bookmark in user.bookmarks.all():
            bookmarks.append({
                "command": bookmark.command,
                "keywords": [
                    keyword.name for keyword in bookmark.keywords.all()
                ]
            })

        return JsonResponse({"user": {
            "id": user.id,
            "bookmarks": bookmarks
        }})
