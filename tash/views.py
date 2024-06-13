from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class WelcomePage(TemplateView):
    template_name = 'welcome_page.html'

class AboutPage(TemplateView):
    template_name = 'about.html'

class ServicesPage(TemplateView):
    template_name = 'services.html'

class GalleryPage(TemplateView):  # Ensure correct spelling if intended
    template_name = 'gallery.html'

class GalleryDetailsPage(TemplateView):  # Ensure correct spelling if intended
    template_name = 'gallery_details.html'

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
            return HttpResponseRedirect(reverse("exit_page"))
        return super().get(request, *args, **kwargs)
