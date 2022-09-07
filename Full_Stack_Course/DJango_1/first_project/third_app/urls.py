from django.urls import path
from third_app import views

urlpatterns = [
    path("", views.add_db_table, name = "add_db_table"),
]