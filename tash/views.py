from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class WelcomePage(TemplateView):
    template_name = 'welcome_page.html'

class AboutPage(TemplateView):
    template_name = 'about.html'

class ServicesPage(TemplateView):
    template_name = 'services.html'

class GallaryPage(TemplateView):
    template_name = 'gallary.html'

class TeamPage(TemplateView):
    template_name = 'team.html'

class BlogPage(TemplateView):
    template_name = 'blog.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'
class ExitPage(TemplateView):
    template_name = 'exit_page.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("exit"))
        return super().get(request, *args, **kwargs)

