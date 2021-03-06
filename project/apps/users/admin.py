from django.contrib import admin

from apps.users.models import User, Profile, ProfileGallery
from apps.commons.admin import site


@admin.register(User, site=site)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    search_fields = ['username__startswith', 'email__startswith']


@admin.register(Profile, site=site)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username']
    list_display = ['get_username', 'number_of_works_done']

    def get_username(self, obj):
        return obj.user.username

    get_username.short_description = 'Пользователь'
    get_username.admin_order_field = 'user__username'


@admin.register(ProfileGallery, site=site)
class ProfileGallery(admin.ModelAdmin):
    pass
