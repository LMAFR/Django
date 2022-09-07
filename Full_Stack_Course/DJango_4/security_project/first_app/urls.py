from django.urls import path
from first_app import views

# Template URLS

# To be able to add relatives path we have to assign the name we will put in {% url app_name:page_name %}:
app_name = "first_app"

# Paths:
urlpatterns = [
    path("", views.first_app, name = "first_app"),
    path("registration/", views.registration, name = "registration"),
    path("user_login/", views.user_login, name = "user_login"),
]
