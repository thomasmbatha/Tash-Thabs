# blog/urls.py
from django.urls import path
from .views import BlogHome

urlpatterns = [
    path('blog-home/', BlogHome.as_view(), name='blog_home')
]
