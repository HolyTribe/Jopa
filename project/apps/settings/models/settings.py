from django.db import models


class Settings(models.Model):
    """Настройки сайта"""
    title = models.CharField('Название', max_length=125)
    title_default = models.CharField('Название по умолчанию', max_length=125, default="", blank=True)
    description_default = models.CharField('Описание по умолчанию', max_length=125, default="", blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'

    def __str__(self):
        return self.title
