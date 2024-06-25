# blog/views.py
from typing import Any
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView
from .forms import ArticleForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article
# Create your views here.


class BlogHome(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/blog_home.html'
    paginate_by = 4

class Featured(ListView):
    model = Article
    queryset = Article.objects.filter(featured=True).order_by('-date')
    template_name = 'blog/featured.html'
    paginate_by = 4
class DetailArcticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailArcticleView, self).get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context


class LikeArticle(View):
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(request.user.id)
        else:
            article.likes.add(request.user.id)
        article.save()
        return redirect('detail_article', pk)
    
class DeleteArticleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog_home')

    def test_func(self):
        article = Article.objects.get(id=self.kwargs.get('pk'))
        return self.request.user.id == article.author.id
    
class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)