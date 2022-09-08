from django.views import generic

class HomePage(generic.TemplateView):
    template_name = "base.html"

class About(generic.TemplateView):
    template_name = "about.html"