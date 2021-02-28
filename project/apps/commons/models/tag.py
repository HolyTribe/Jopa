from django.db import models


class TagMixin(models.Model):
    title = models.CharField('Имя', max_length=50)
    slug = models.SlugField('Слаг', max_length=100)
    references = models.PositiveIntegerField('Кол-во упоминаний', blank=True, default=0)
    cleaned_name = models.CharField('Уникальное имя', unique=True, blank=True, max_length=50)

    def save(self, *args, **kwargs):
        self.cleaned_name = self.title.lower().replace(' ', '')
        super(TagMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True