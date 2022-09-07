from django.urls import path
from first_app import views

# When we use relative paths in html files by {% url "app_name:relative_tag_name" %}, app_name has to be stored in a variable as in the next line:
app_name = "first_app"

urlpatterns = [
    path("", views.base, name = "base"),
    path("other/", views.other, name="other"),
    path("relative/", views.relative, name="relative"),
]