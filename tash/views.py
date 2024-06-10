from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

# class AboutPage(TemplateView):
#     template_name = 'about.html'

# class ContactPage(TemplateView):
#     template_name = 'contacts.html'

# class ProductsPage(TemplateView):
#     template_name = 'products.html'

# class TestimonialsPage(TemplateView):
#     template_name = 'testimonials.html'

class WelcomePage(TemplateView):
    template_name = 'welcome_page.html'

class ExitPage(TemplateView):
    template_name = 'exit_page.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("exit"))
        return super().get(request, *args, **kwargs)

