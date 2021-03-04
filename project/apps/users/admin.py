from django.contrib import admin
from apps.users.models import User
from apps.commons.admin import site


@admin.register(User, site=site)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    search_fields = ['username__startswith', 'email__startswith']
