from apps.tags import views
from django.urls import path

app_name = 'tags'

urlpatterns = [
    path('create/', views.TagCreateView.as_view(), name='create'),
]
