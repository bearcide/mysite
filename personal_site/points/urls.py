from django.urls import path
from . import views

urlpatterns = [
    path('content/', views.display_content, name='content_display'),
]