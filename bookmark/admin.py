from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url') # 사이트에서 출력할 컬럼 목록
