"""
URL configuration for tash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePage.as_view(), name="home"),
    path("welcome/", views.WelcomePage.as_view(), name="welcome_page"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("services/", views.ServicesPage.as_view(), name="services"),
    path("gallery/", views.GalleryPage.as_view(), name="gallery"),
    path("gallery_details/", views.GalleryDetailsPage.as_view(), name="gallery_details"),
    path("blog_single/", views.BlogSinglePage.as_view(), name="blog_single"),
    path("team/", views.TeamPage.as_view(), name="team"),
    path("blog/", views.BlogPage.as_view(), name="blog"),
    path("contacts/", views.ContactPage.as_view(), name="contacts"),
    path("exit/", views.ExitPage.as_view(), name="exit_page"),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("auth/", include("django.contrib.auth.urls")),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)