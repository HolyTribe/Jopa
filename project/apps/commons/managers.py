from django.db import models
from django.db.models.signals import post_save


class ImageQuerySet(models.QuerySet):

    def update(self, **kwargs):
        super().update(**kwargs)
        for image in self.iterator():
            post_save.send(sender=image.__class__, instance=image)


class ImageManager(models.Manager):

    def get_queryset(self):
        return ImageQuerySet(self.model, using=self.db)
