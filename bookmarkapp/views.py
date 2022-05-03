from .models import Bookmarkapp
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from bookmark.views import OwnerOnlyMixin


class BookmarkLV(ListView):
    model = Bookmarkapp
    

class BookmarkDV(DetailView):
    model = Bookmarkapp

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmarkapp
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmarkapp:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmarkapp.objects.filter(owner=self.request.user)

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model=Bookmarkapp
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmarkapp
    success_url = reverse_lazy('bookmark:index')

