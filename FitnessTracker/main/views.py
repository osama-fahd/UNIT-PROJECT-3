from django.shortcuts import render, redirect
from django.http import HttpRequest

from datetime import datetime

from .forms import ContactForm

from routines.models import Routine

from django.contrib import messages


def home_view(request:HttpRequest):
    routines = Routine.objects.all()

    return render(request, 'main/home.html', {'routines': routines})

def contact_view(request:HttpRequest):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, "Your Message Has Been Sent Successfully!", "alert-success")
            return redirect('main:home_view')
        else:
            messages.error(request, "Couldn't Send Your Message!", "alert-danger")
            return render(request, "main/contact.html")

    return render(request, 'main/contact.html')