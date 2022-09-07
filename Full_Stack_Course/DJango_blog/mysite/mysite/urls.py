"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("accounts/login/", views.LoginView.as_view(), name = "login"),
    # The kwargs argument in the line below is to redirect the user to the main page ("/") after he logs out:
    path("accounts/logout/", views.LogoutView.as_view(next_page=reverse_lazy('post_list')), name = "logout"),
]
