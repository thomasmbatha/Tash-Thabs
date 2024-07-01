from django.urls import path, include
from .views import (BlogHome, DetailArcticleView, LikeArticle,
                    LivingRoomPosts, DeleteArticleView, 
                    CreateArticleView, AddCommentView, BedroomPosts,
                    KitchenPosts, BathroomPosts, OutdoorPosts,
                    OfficePosts, BioView)

urlpatterns = [
    path('tinymce/', include('tinymce.urls')),
    path('blog-home/', BlogHome.as_view(), name='blog_home'),
    path('living/', LivingRoomPosts.as_view(), name='living'),
    path('bedroom/', BedroomPosts.as_view(), name='bedroom'),
    path('kitchen/', KitchenPosts.as_view(), name='kitchen'),
    path('bathroom/', BathroomPosts.as_view(), name='bathroom'),
    path('outdoor/', OutdoorPosts.as_view(), name='outdoor'),
    path('office/', OfficePosts.as_view(), name='office'),
    path('<int:pk>/', DetailArcticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
    path('create/', CreateArticleView.as_view(), name='create_article'),
    path('<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
    path('bio/', BioView.as_view(), name='bio')
]
