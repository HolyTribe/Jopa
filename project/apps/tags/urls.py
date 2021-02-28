from django.urls import path

from apps.tags import views


app_name = 'tags'
urlpatterns = [
    path('create/', views.TagCreateView.as_view(), name='create'),
]
