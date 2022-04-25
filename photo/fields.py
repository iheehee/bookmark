import os
from PIL import Image
from django.db.models.fields import ImageField, ImageFieldFile

class ThumbnailImageFieldsfiles(ImageFieldFile) :
    def _add_thumb(self):
        parts = self.split(".")
        parts.insert(-1, "thumb")
        if parts[-1].lower() not in ['jpeg', 'jpg']:
            parts[-1] = 'jpg'
        return ".".join(parts)

    @property
        