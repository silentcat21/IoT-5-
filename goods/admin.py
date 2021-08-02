from django.contrib import admin
from goods.models import Bookmark

@admin.register(Goods)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'goods', 'count', ' ')       # 사이트에서 출력할 컬럼 목록
# Register your models here.
