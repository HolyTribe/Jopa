from django.db import models


class SeoMixin(models.Model):
    fields = ('meta_title', 'meta_description')
    fieldsets = ('SEO', {
        'fields': fields,
    })
    meta_title = models.CharField('Название', max_length=125, default="", blank=True)
    meta_description = models.CharField('Описание', max_length=250, default="", blank=True)

    class Meta:
        abstract = True
