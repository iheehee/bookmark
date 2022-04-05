from bookmarkapp.models import Bookmarkapp
from django.contrib import admin
from bookmarkapp.models import Bookmarkapp

@admin.register(Bookmarkapp)
class BookmarkappAdmin(admin.ModelAdmin): 
    list_display = (
        'id',
        'title',
        'url'
    )