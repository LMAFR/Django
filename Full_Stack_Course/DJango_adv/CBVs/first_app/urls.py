from django.urls import path, re_path
from first_app import views

app_name = "first_app"

urlpatterns = [
    path("", views.first_app.as_view(), name="first_app"),
    path("school_list/", views.SchoolListView.as_view(), name="list"),
    # <pk> stands for "primary key". schools.id will be 1, 2, etc.
    re_path(r"^school_list/(?P<pk>\d+)/$", views.SchoolDetailView.as_view(), name="detail"),
    path("create/", views.CreateSchool.as_view(), name = "create"),
    # The UpdateView method require we use a url with a pk or a slug (for instance, "name1-name2-name3...etc"), 
    # but it will create the form without asking for an html file:
    re_path(r"^school_list/(?P<pk>\d+)/update/$", views.UpdateSchool.as_view(), name = "update"),
    re_path(r"^delete/(?P<pk>\d+)/$", views.DeleteSchool.as_view(), name="delete"),
]