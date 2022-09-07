from django.shortcuts import render
from .forms import UserProfileInfoForm
from first_app.forms import UserForm, UserProfileInfoForm

# For the login/logout step:
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, "first_app/index.html")

def registration(request):

    registered = False

    if request.method == "POST":
        
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            # Save the data inserted in the user form in the database
            user = user_form.save()
            # Apply the password hasher to the password
            user.set_password(user.password)
            # Save the password (now hashed) in the database. It overwrites the previous password.
            user.save()

            # For the profile form, we are going to deal with the inserted data before pass it to the database, so we will use commit=False 
            # (by default is True)
            profile = profile_form.save(commit=False)
            # As we declared profile_form().user and User would have a One to One field relationship (in the models), now we have to create that
            # relationship here: 
            profile.user = user

            # Import the image inserted in the form to the database:
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, "first_app/registration.html", {"registered" : registered,
                                                            "user_form":user_form,
                                                            "profile_form":profile_form})

def first_app(request):
    return render(request, "first_app/first_app.html")

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                # The user will be logged-in and we will return him to the main page of the website:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            
            else:
                # Give back the corresponding message:
                return HttpResponse("Account is not active!")

        else:
            # Let´s print the information provided in case the user fails, just to be able to prevent malicious tries:
            print("Someone tried to login and failed.")
            print("Username: {}.\nPassword:{}".format(username, password))
            # Give back the corresponding message:
            return HttpResponse("Login credentials are not registered!")

    else:

        return render(request, "first_app/login.html")

# The decorator below makes the function work just if the user is logged-in
@login_required
def user_logout(request):
    # Logout the user: 
    logout(request)
    # Return him to the main page
    return HttpResponseRedirect(reverse("index"))

# Another posible use of that decorator would be to print a messageto let the user know he is logged in:
@login_required
def special(request):
    return HttpResponse("You are logged in, nice!")

