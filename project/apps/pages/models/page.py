from django.db import models

from apps.seo.models import SeoMixin


class Page(SeoMixin):
    """Модель страницы"""

    class TemplateChoice(models.TextChoices):
        """Выборы для шаблоных страниц"""
        INDEX = 'index', 'Главная'

        __empty__ = 'Текстовая страница'

    title = models.CharField('Заголовок', max_length=125)
    template = models.CharField('Шаблон', max_length=50, choices=TemplateChoice.choices, null=True, editable=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title
