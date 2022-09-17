from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.views import generic
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import mail

# Create your views here.

    # Reference: https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # subject = "¡{} nos ha contactado!".format(form.cleaned_data['name'])
            body = {
                'email_address':form.cleaned_data['email_address'],
                'title':form.cleaned_data['title'],
                'description':form.cleaned_data['description'],
            }
            message = "\n".join(body.values())

            try:
                connection = mail.get_connection()
                connection.open()
                email = mail.EmailMessage(
                    body['title'],
                    message,
                    body['email_address'],
                    ['admin@example.com'],
                    connection=connection,
                )
                email.send()
            # The except below prevent attackers from inserting extra email headers:
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')

    form = ContactForm()
    return render(request, "contact/contact_form.html", {'form':form})

    # Reference 1: https://stackoverflow.com/questions/70508674/django-how-do-you-email-a-completed-create-view-form