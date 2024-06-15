
# Blog views

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        # 'img': 'image-1.png ',
        'author': 'Thabo Mbatha',
        'title': 'Blog Post 1',
        'content': 'This is my first blog post',
        'date_posted': '15th June 2024',
        # 'comments_no': '12 comments',
        # 'Button': 'Read More',
        # 'quote': 'The best interiors'
    },  
    {
        # 'image': 'image-2.png ',
        'author': 'Thomas Tash',
        'title': 'Blog Post 2',
        'content': 'This is my second blog post',
        'date_posted': '16th June 2024',
        # 'comments': '12 comments',
        # 'Button': 'Read More',
        # 'quote': 'The best interiors in the world'

    },
]

def BlogHome(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_home.html',context)

def BlogAbout(request):
    return render(request, 'blog/blog_about.html',{'title': "About Page"})
