from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (View, TemplateView, ListView, DetailView, 
                                    CreateView, UpdateView, DeleteView) 
from . import models
from django.urls import reverse_lazy


# Create your views here.
# The Class Based Views are views called as classes that inherit from the View class previously imported
# class index(View):
#     def get(self,request):
#         return HttpResponse("This is my first CBV!")

class index(TemplateView):
    template_name = "index.html"

class first_app(TemplateView):
    template_name = "first_app/first_app.html"

    # **kwargs stands for "keyword arguments" and it allows us to pass any number of arguments which will be stored as a dictionary whose keys are the
    # name of the argument itself and whose values will be the values we pass to those arguments (for example name = "George" will have name as key 
    # and "George" as value).
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inject_me"] = "THIS IS MY FIRST CBV INJECTION!"
        return context

class SchoolListView(ListView):
    # The next line let us assign a name for the context of this view (it is not mandatory, by default the context would be model_name_list, 
    # where model_name would be in lowercase):
    context_object_name = "schools"
    # The next line assign the model with all its features
    model = models.School

class SchoolDetailView(DetailView):
    # DetailView returns, by default, the context "model_name" (in lowercase), not model_name_detail as could be thought based on ListView.
    # Anyway, assign out own name to the context can makes things easier to understand in the future, so we do it:
    context_object_name = "school_details"
    # The next line assign a template to the view:
    template_name = "first_app/school_detail.html"
    model = models.School

class CreateSchool(CreateView):
    fields = ("name", "principal", "location")
    model = models.School

class UpdateSchool(UpdateView):
    # A school is not likely to change its location, so we won't include that attribute in the update form:
    fields = ("name", "principal")
    model = models.School

class DeleteSchool(DeleteView):
    model = models.School
    # We use reverse_lazy in order to get back to the corresponding url after the changes have been done. 
    success_url = reverse_lazy("first_app:list")