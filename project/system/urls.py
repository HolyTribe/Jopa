import debug_toolbar
from apps.commons.admin import site
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
                  path('admin/', site.urls),
                  path('account/', include('apps.users.urls')),
                  path('tags/', include('apps.tags.urls')),
                  path('', include('apps.pages.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
                + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
