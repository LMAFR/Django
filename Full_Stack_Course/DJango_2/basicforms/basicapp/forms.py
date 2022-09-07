# import email
# from enum import unique
# from msilib.schema import Error
# from socket import fromshare
# from unicodedata import name
# from xml.dom import ValidationErr
from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != "z":
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
    # We could also add a verification step just including a previously created function in the validators list of the attribute we want to verify:
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again: ") 
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)

# The term "clean" is used to talk about the action of verifying a variable
# Method equivalent to apply validators.MaxLengthValidator()
# def clean_botcatcher(self):
#     botcatcher = self.cleaned_data["botcatcher"]
#     if len(botcatcher) > 0:
#         raise forms.ValidationError("WE GOT A BOT!")
#     return botcatcher

# We could also define a method to check all (or several) the attributes at the same time:
# def clean(self):
#     all_clean_data = super().clean()
#     email = all_clean_data["email"]
#     vemail = all_clean_data["verify_email"]

#     if email != vemail:
#         raise forms.ValidationError("The emails do not match!")

# These two last functions are not raising the error as it should. I have to further investigate this issue later!