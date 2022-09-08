from django.views import generic
from .models import Service

# Create your views here.

class ServiceListView(generic.ListView):
    model = Service
