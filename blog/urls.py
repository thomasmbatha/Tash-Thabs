# Blog urls
from django.urls import path
from . import views
from . views import UploadPhoto, PhotoList

urlpatterns = [
    path('blog-home/', views.BlogHome, name="blog_home"),
    path('blog-about/', views.BlogAbout, name="blog_about"),
    path('blog-upload/', UploadPhoto, name="upload_photo"),
    path('blog-list/', PhotoList, name="photo_list"), #this I need to make it home
]
