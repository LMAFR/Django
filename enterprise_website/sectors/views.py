from django.views import generic
from .models import Sector
# Create your views here.

class SectorListView(generic.ListView):
    model=Sector