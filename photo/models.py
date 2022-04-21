from pydoc import describe
from django.db import models
from django.urls import reverse
from photo.fields import ThumbnailImageField


class Album(models.Model):
    name = models.CharField(max_length=30)
    describtion = models.CharField('One Line Description' ,max_length=100, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def def get_absolute_url(self):
        return reverse('photo:album_detail', kwargs={'pk': self.id})


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField('TITLE' ,max_length=100, blank=True)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField(upload_ot='photo/%Y/%m')
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def def get_absolute_url(self):
        return reverse('photo:photo_detail', kwargs={'pk': self.id})