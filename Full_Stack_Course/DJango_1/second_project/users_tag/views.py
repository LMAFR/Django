from django.shortcuts import render
from .forms import FormUsers
from users_tag.forms import FormUsers
from users_tag.models import Users

# Create your views here.
# def add_db(request):
#     users_list = Users.objects.order_by("fname")
#     names_dict = {"new_db" : users_list}
#     return render(request,"users_tag/main_file.html",names_dict)

def add_form(request):
    form = FormUsers

    if request.method == "POST":

        form = FormUsers(request.POST)

        if form.is_valid():

            print("VALIDATION SUCCESS!")
            print("FIRST NAME: " + form.cleaned_data["fname"])
            print("LAST NAME: " + form.cleaned_data["lname"])
            print("EMAIL: " + form.cleaned_data["email"])

            form.save()
            # I did not create a main page with its usual function (let´s call it "index()"), but if I would have done it, we could go back to
            # that page after sending the POST request by adding the next line of code:
            # return index(request)

        else:
            print("Error form invalid")

    return render(request, "users_tag/main_file.html", {"form":form})