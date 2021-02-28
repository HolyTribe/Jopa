from django.db import models


class TagMixin(models.Model):
    tag_title = models.CharField('Имя', max_length=50)
    tag_slug = models.SlugField('Слаг', max_length=100)
    tag_references = models.PositiveIntegerField('Кол-во упоминаний', blank=True, default=0)

    class Meta:
        abstract = True