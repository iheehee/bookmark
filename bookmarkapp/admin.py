from bookmarkapp.models import Bookmarkapp
from django.contrib import admin


@admin.register(Bookmarkapp)
class BookmarkappAdmin(admin.ModelAdmin): 
    list_display = (
        'id',
        'title',
        'url'
    )