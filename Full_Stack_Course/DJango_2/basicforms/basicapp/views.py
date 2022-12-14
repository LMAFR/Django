from django.shortcuts import render
# from DJango_2.basicforms.basicapp import forms
from basicapp import forms

# Create your views here.

def main_page(request):
    return render(request, "basicapp/main_page.html")

def form_name_view(request):
    form = forms.FormName

    if request.method == "POST":

        form = forms.FormName(request.POST)

        if form.is_valid():

            print("VALIDATION SUCCESS!")
            print("NAME: " + form.cleaned_data["name"])
            print("EMAIL: " + form.cleaned_data["email"])
            print("TEXT: " + form.cleaned_data["text"])

    return render(request, "basicapp/form_page.html", {"form": form})
