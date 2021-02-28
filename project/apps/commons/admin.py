from django.contrib import admin
from apps.commons.admin import site
from .models import ImageModel

@admin.register(ImageModel, site=site)
class ImageAdmin(admin.ModelAdmin):
  pass
