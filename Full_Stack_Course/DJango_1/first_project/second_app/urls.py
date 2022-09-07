from django.urls import path
from second_app import views

urlpatterns = [
    path("", views.add_image, name = "add_image"),
]