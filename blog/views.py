
# Blog views

from django.shortcuts import render,redirect
from .forms import PhotoForm
from django.http import HttpResponse
from . models import Post, Photo  

# Create your views here.

def BlogHome(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog_home.html',context)

def BlogAbout(request):
    return render(request, 'blog/blog_about.html',{'title': "About Page"})

def UploadPhoto(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog/blog_home.html')  # Redirect to a page that lists uploaded photos
    else:
        form = PhotoForm()
    return render(request, 'blog/uploads.html', {'form': form})

def PhotoList(request):
    return render(request, 'blog/blog_home.html', {'\photos': Post})
