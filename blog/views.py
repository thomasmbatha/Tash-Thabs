# blog/views.py
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Article
# Create your views here.


class BlogHome(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/blog_home.html'
    paginate_by = 1

class DetailArcticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'