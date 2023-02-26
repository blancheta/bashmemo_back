from django.contrib import admin

from bookmark.models import User, Organisation, Keyword, Bookmark


class UserAdmin(admin.ModelAdmin):
    model = User


class OrganisationAdmin(admin.ModelAdmin):
    model = Organisation


class KeywordAdmin(admin.ModelAdmin):
    model = Keyword


class BookmarkAdmin(admin.ModelAdmin):
    model = Bookmark


admin.site.register(User, UserAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
