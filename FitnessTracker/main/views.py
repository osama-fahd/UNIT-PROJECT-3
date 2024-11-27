from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from datetime import datetime

from .models import Contact
from .forms import ContactForm

from django.core.mail import EmailMessage
from django.contrib import messages


def home_view(request:HttpRequest):

    return render(request, 'main/home.html', {})

def contact_view(request:HttpRequest):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            
            return redirect('main:home_view')
        else:
            return render(request, "main/contact.html")

    return render(request, 'main/contact.html')