# blog/views.py
from django.shortcuts import render
from django.views import View
# Create your views here.


class BlogHome(View):
    def get (self,request):
        return render(request, 'blog/blog_home.html')