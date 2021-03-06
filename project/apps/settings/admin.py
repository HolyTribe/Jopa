from django.contrib import admin

from apps.commons.admin import site
from apps.settings.models import Settings


@admin.register(Settings, site=site)
class SettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ('SEO', {
            'fields': ('title_default', 'description_default',)
        })
    )
