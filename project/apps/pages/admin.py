from apps.commons.admin import site
from apps.pages.models import Page
from django.contrib import admin


@admin.register(Page, site=site)
class PageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'template']
    readonly_fields = ['template']
    fieldsets = (
        (None, {
            'fields': ('title', 'template')
        }),
        Page.fieldsets,
    )

    def has_delete_permission(self, request, obj=None):
        if obj and obj.template:
            return False
        return super(PageAdmin, self).has_delete_permission(request, obj)
