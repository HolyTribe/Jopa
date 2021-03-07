from django.contrib.auth import get_user_model
from django.db import models
from sorl.thumbnail import ImageField

from apps.commons.models import ImageModel
from apps.commons.storage import HashedImageStorage


class Profile(models.Model):
    """Model for profile"""

    user = models.ForeignKey(
        get_user_model(),
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='profile'
    )
    avatar = ImageField(verbose_name='Аватарка', storage=HashedImageStorage, blank=True, null=True)
    description = models.TextField(verbose_name='Описание профиля', blank=True, null=True)
    number_of_works_done = models.PositiveIntegerField(verbose_name='Общеее количество сделанных заказов', default=0)

    def __str__(self):
        return f'Профиль пользователя - {self.user.username}'

    def get_all_images(self):
        all_gallery = self.gallery.select_related('image')
        return [gallery.image for gallery in all_gallery]

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['-id']


class ProfileGallery(models.Model):
    """Gallery for image upload in profile"""
    image = models.ForeignKey(
        ImageModel,
        verbose_name='Изображения для галерее',
        on_delete=models.CASCADE,
        related_name='gallery'
    )
    profile = models.ForeignKey(
        Profile,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='gallery'
    )

    def __str__(self):
        return f'Изображения для галереи пользователя {self.profile.user.username}'

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерии'
        ordering = ['-id']
