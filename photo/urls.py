#from django.urls import path, re_path
#from blog import views

app_name = 'photo'
urlpatterns = [
    path('', views.AlbumLV.as_view(), name='index'),
    path('album', views.AlbumLV.as_view(), name='album_list'),
    #path('album/<int:pk>', views.AlbumDV.as_view(), name='album_detail'),
    #path('photo/<int:pk>', views.AlbumDV.as_view(), name='photo_detail'),
]
