from django.db import models
from sorl.thumbnail import ImageField
from ..storage import HashedImageStorage, WebpStorage
from ..libs.webp.compress import convert_to_webp
from pathlib import Path
from django.conf import settings
from django.core.files import File
from django.db.models.signals import post_save
import os


class ImageModel(models.Model):
    image = ImageField('Изображение', storage=HashedImageStorage)
    webp = ImageField('Webp изображение', blank=True, default="", storage=WebpStorage)
    alt = models.CharField('Альтернативный текст', max_length=120, blank=True, default="")
    upload_date = models.DateTimeField(verbose_name="Дата загрузки", auto_now_add=True)


def generate_webp(sender, instance, **kwargs):
    if hasattr(instance, 'PSAVED'):
        return
    webp_name = f"{instance.image.name.split('.')[0]}.webp"
    webp_path = os.path.join(settings.MEDIA_ROOT, webp_name)
    image_path = os.path.join(settings.MEDIA_ROOT, instance.image.name)
    success_convert = convert_to_webp(image_path, webp_path)
    if success_convert:
        os.path.normpath(webp_path)
        with open(webp_path, 'rb') as f:
            instance.webp = File(f, webp_name)
            instance.PSAVED = True
            instance.save()
        del instance.PSAVED
    print(instance.image.name)
    
post_save.connect(generate_webp, sender=ImageModel)
