from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blog_home')
        else:
            return render(request, 'blog/blog_home.html', {'form': form})
