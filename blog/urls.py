# blog/urls.py
from django.urls import path, include
from .views import BlogHome,DetailArcticleView,LikeArticle,Featured

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('blog-home/', BlogHome.as_view(), name='blog_home'),
    path('<int:pk>/', DetailArcticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('featured/', Featured.as_view(), name='featured')
]
