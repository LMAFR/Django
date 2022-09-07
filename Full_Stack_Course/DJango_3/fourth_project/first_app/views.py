from unicodedata import name
from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {"sentence" : "Hello world!", "number" : 100}
    return render(request, "first_app/index.html", my_dict)

def base(request):
    return render(request, "first_app/base.html")

def other(request):
    return render(request, "first_app/other.html")

def relative(request):
    return render(request, "first_app/relative_url_template.html")