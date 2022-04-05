from django.views.generic import ListView, DetailView
from bookmarkapp.models import Bookmarkapp

class BookmarkLV(ListView):
    model = Bookmarkapp

class BookmarkDV(DetailView):
    model = Bookmarkapp


