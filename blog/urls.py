# blog/urls.py
from django.urls import path, include
from .views import BlogHome

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('blog-home/', BlogHome.as_view(), name='blog_home'),
]
