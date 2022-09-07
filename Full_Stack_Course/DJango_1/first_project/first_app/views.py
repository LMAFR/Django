from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("<em>Hello world!</em>")

    # my_dict = {"insert_me" : "Hello, I am from views.py!"}
    # return render(request, "index.html", context=my_dict)

    my_dict = {"insert_me" : "Hello, I am from first_app/index.html!"}
    return render(request, "first_app/index.html", context=my_dict)