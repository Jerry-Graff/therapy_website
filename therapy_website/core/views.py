import os
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm


def home(request):
    form = ContactForm()
    return render(request, "core/home.html", {'form': form})


def form_send(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        clean = form.cleaned_data
        body = f"Message from {clean['name']} ({clean['email']}):\n\n{clean['message']}"
        owner_email = os.environ.get('FORM_EMAIL')
        send_mail(
            'Contact Form Submission',
            body,
            owner_email,
            [owner_email],
            fail_silently=False,
            reply_to=[clean['email']]
        )
        return redirect('home')
    return render(request, 'core/home.html', {'form': form})
