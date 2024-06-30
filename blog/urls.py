# blog/urls.py
from django.urls import path, include
from .views import BlogHome, DetailArcticleView, LikeArticle, LivingRoomPosts, DeleteArticleView, CreateArticleView, AddCommentView

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('blog-home/', BlogHome.as_view(), name='blog_home'),
    path('living/', LivingRoomPosts.as_view(), name='living'),
    path('<int:pk>/', DetailArcticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
    path('create/', CreateArticleView.as_view(), name='create_article'),
    path('<int:pk>/comment', AddCommentView.as_view(), name='add_comment')
]
