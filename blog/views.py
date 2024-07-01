# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import AnonymousUser
from .models import Article, Comment, Bio
from .forms import ArticleForm, CommentForm, BioForm

class BioView(LoginRequiredMixin, View):
    def get(self, request):
        bio, created = Bio.objects.get_or_create(user=request.user)
        form = BioForm(instance=bio)
        return render(request, 'blog/bio.html', {'form': form, 'bio': bio})

    def post(self, request):
        bio, created = Bio.objects.get_or_create(user=request.user)
        form = BioForm(request.POST, request.FILES, instance=bio)
        if form.is_valid():
            form.save()
            return redirect('bio')
        return render(request, 'blog/bio.html', {'form': form, 'bio': bio})

class BlogHome(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blog/blog_home.html'
    paginate_by = 4

class LivingRoomPosts(ListView):
    model = Article
    queryset = Article.objects.filter(living=True).order_by('-date')
    template_name = 'blog/blog_living.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['living_count'] = self.get_queryset().count()
        return context

class BedroomPosts(ListView):
    model = Article
    queryset = Article.objects.filter(bedroom=True).order_by('-date')
    template_name = 'blog/blog_bedroom.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bedroom_count'] = self.get_queryset().count()
        return context
    
class KitchenPosts(ListView):
    model = Article
    queryset = Article.objects.filter(kitchen=True).order_by('-date')
    template_name = 'blog/blog_kitchen.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kitchen_count'] = self.get_queryset().count()
        return context
    
class BathroomPosts(ListView):
    model = Article
    queryset = Article.objects.filter(bathroom=True).order_by('-date')
    template_name = 'blog/blog_bathroom.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bathroom_count'] = self.get_queryset().count()
        return context
    
class OutdoorPosts(ListView):
    model = Article
    queryset = Article.objects.filter(outdoor=True).order_by('-date')
    template_name = 'blog/blog_outdoor.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outdoor_count'] = self.get_queryset().count()
        return context
    
class OfficePosts(ListView):
    model = Article
    queryset = Article.objects.filter(office=True).order_by('-date')
    template_name = 'blog/blog_office.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['office_count'] = self.get_queryset().count()
        return context

class DetailArcticleView(DetailView):
    model = Article
    template_name = 'blog/blog_post.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        context['comments'] = Comment.objects.filter(article=article).order_by('-date')
        context['comment_form'] = CommentForm()
        context['comment_count'] = Comment.objects.filter(article=article).count()

        # Posts count
        context['living_count'] = Article.objects.filter(living=True).count()
        context['bedroom_count'] = Article.objects.filter(bedroom=True).count()
        context['kitchen_count'] = Article.objects.filter(kitchen=True).count()
        context['bathroom_count'] = Article.objects.filter(bathroom=True).count()
        context['outdoor_count'] = Article.objects.filter(outdoor=True).count()
        context['office_count'] = Article.objects.filter(office=True).count()

        # Check if the user is authenticated before querying the Bio model
        if isinstance(self.request.user, AnonymousUser):
            context['user_bio'] = None
        else:
            context['user_bio'] = Bio.objects.get_or_create(user=self.request.user)[0]

        return context

class LikeArticle(View):
    def post(self, request, pk):
        article = Article.objects.get(id=pk)
        if article.likes.filter(pk=request.user.id).exists():
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

class CreateArticleView(LoginRequiredMixin, View):
    def get(self, request):
        form = ArticleForm()
        return render(request, 'blog/blog_create.html', {'form': form})

    def post(self, request):
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('blog_home')
        return render(request, 'blog/blog_create.html', {'form': form})

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
        return redirect('detail_article', pk)
