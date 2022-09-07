from django.shortcuts import render

# Create your views here.
def help(request):
    dict_1 = {"Help" : "This is the Help Section of this website."}
    return render(request,"helptag_app/help.html", context = dict_1)