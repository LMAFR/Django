from django.urls import path
from . import views

app_name="sectors"

urlpatterns = [
    path('', views.SectorListView.as_view(), name='all'),
]
