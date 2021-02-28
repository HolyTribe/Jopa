from django.db import models


class TagMixin(models.Model):
    tag_title = models.CharField('Имя', max_length=50)
    tag_slug = models.SlugField('Слаг', max_length=100)
    tag_references = models.PositiveIntegerField('Кол-во упоминаний', blank=True, default=0)
    tag_cleaned_name = models.CharField('Уникальное имя', unique=True, blank=True, max_length=50)

    # Под вопросом
    def save(self, *args, **kwargs):
        self.tag_cleaned_name = self.tag_title.lower().replace(' ', '')
        super(TagMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True