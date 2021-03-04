from django.contrib.auth import get_user_model
from django.db import models


class Tag(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название тега')
    slug = models.SlugField(max_length=255, verbose_name='slug для тегов в url')

    active = models.BooleanField(default=False, verbose_name='Активность тега')

    users = models.ManyToManyField(
        get_user_model(),
        verbose_name='Пользователи, которые попытались создать тег',
        related_name='tags',
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
