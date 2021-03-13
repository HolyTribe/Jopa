from django.contrib import admin
from apps.commons.admin import site

from apps.tags.models import Tag


@admin.register(Tag, site=site)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
