from django.contrib.admin.sites import AdminSite


class CustomAdmin(AdminSite):
    """Кастомная админка сайта"""
    site_header = 'Сайт хеадер'
    site_title = 'Сайт тайтл'


site = CustomAdmin()
