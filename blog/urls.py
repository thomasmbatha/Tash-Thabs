# Blog urls
from django.urls import path
from . import views

urlpatterns = [
    path('blog-home/', views.BlogHome, name="blog_home"),
    path('blog-about/', views.BlogAbout, name="blog_about"),
]
