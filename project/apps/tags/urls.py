from django.urls import path

from apps.tags import views


urlpatterns = [
    path('create/', views.TagCreateView.as_view(), name='tag_create'),
]
