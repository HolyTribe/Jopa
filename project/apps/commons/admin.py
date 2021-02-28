
from django.contrib import admin
from apps.commons.admin import site
from .models import ImageModel
from django.contrib.admin.sites import AdminSite

class CustomAdmin(AdminSite):
    """Кастомная админка сайта"""
    site_header = 'Сайт хеадер'
    site_title = 'Сайт тайтл'


site = CustomAdmin()

@admin.register(ImageModel, site=site)
class ImageAdmin(admin.ModelAdmin):
  pass
