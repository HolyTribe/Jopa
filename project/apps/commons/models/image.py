from django.db.models.signals import post_save, pre_delete
from django.core.files import File
from django.conf import settings
from django.db import models

from ..storage import HashedImageStorage, WebpStorage
from ..libs.webp.compress import convert_to_webp
from ..managers import ImageManager

from sorl.thumbnail import ImageField

import os


class ImageModel(models.Model):
    image = ImageField('Изображение', storage=HashedImageStorage)
    webp = ImageField('Webp изображение', blank=True, default="", storage=WebpStorage)
    alt = models.CharField('Альтернативный текст', max_length=120, blank=True, default="")
    upload_date = models.DateTimeField(verbose_name="Дата загрузки", auto_now_add=True)

    objects = ImageManager()

    def __str__(self):
        return f'{self.alt}__{self.image}'

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


def generate_webp(sender, instance, **kwargs):
    """
    Постсейв имаги. PSAVED используется чтобы не упасть
    в рекурсию после сейва в пост-сейве.

    Тут короче конверчу имагу в вебп !!!и сохраняю ее под хешем имаги!!!
    """
    if hasattr(instance, 'PSAVED') or not instance.image:
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
            instance.save(update_fields=['webp'])
        del instance.PSAVED


def delete(sender, instance, **kwargs):
    """
    Если не осталось объектов с такой имагой, то удаляю имагу.
    Если в папке больше нет имаг, удаляется папка
    """
    path = "/".join(os.path.join(settings.MEDIA_ROOT, instance.image.name).split('/')[:-1])
    if ImageModel.objects.filter(image=instance.image).count() < 2:
        instance.image.delete()
        if instance.webp:
            instance.webp.delete()
    if not os.listdir(path):
        os.rmdir(path)


post_save.connect(generate_webp, sender=ImageModel)
pre_delete.connect(delete, sender=ImageModel)
