from django.db import models


def image_directory_path(instance, filename):
    app = instance._meta.app_label
    model = instance._meta.model_name
    return f'images/{app}/{model}/{filename}'


class ImageMixin(models.Model):
    image = models.ImageField('Изображение', upload_to=image_directory_path)
    image_hash = models.CharField('Hash', max_length=63, blank=True, default="")
    alt = models.CharField('Альтернативный текст', blank=True, default="")

    class Meta:
        abstract = True
