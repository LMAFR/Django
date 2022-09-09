from django.views import generic
from .models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CreateRequest(generic.CreateView):
    fields = ('name', 'email_address', 'title', 'description')
    model = Contact
    # template_name = "contact/contact_form.html"

    # def form_valid(self, form):

    # Reference 1: https://stackoverflow.com/questions/70508674/django-how-do-you-email-a-completed-create-view-form
    # Reference 2: https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend