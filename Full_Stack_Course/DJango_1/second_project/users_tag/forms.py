from dataclasses import field, fields
from django import forms
from users_tag.models import Users

class FormUsers(forms.ModelForm):

    class Meta():
        model = Users
        fields = "__all__"


