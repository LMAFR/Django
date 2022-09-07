from django.urls import path, include
from users_tag import views

urlpatterns = [
    # path("", views.add_db, name="add_db"),
    path("", views.add_form, name="add_form"),
]