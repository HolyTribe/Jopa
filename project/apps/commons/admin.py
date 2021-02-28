from django.contrib import admin
from .models import ImageModel
from django.contrib.admin.sites import AdminSite


class CustomAdmin(AdminSite):
    """Кастомная админка сайта"""
    site_header = 'Сайт хеадер'
    site_title = 'Сайт тайтл'


site = CustomAdmin()


@admin.register(ImageModel, site=site)
class ImageAdmin(admin.ModelAdmin):

    readonly_fields = ['webp']


