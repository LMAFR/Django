from django.urls import path
from helptag_app import views

urlpatterns = [
    path('', views.help, name='help')
]