from django.views import generic
from .models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CreateRequest(generic.CreateView):
    fields = ('name', 'title', 'description')
    model = Contact