from django.contrib import messages
from django.shortcuts import render,redirect
from datetime import time
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from .models import Building


def home(request):
    template="building/home.html"
    building = Building.objects.all()
    context={'building':building}
    return render(request,template,context)


def about(request):
    template="building/about.html"
    context={}
    return render(request,template,context)


def contact(request):
    name=request.POST.get("name",)
    email=request.POST.get("email",)
    phone=request.POST.get("phone",)
    message=request.POST.get("message",)

 
    if request.method == 'POST' and name and email and message:
        message="My name is %s"%name + " and my phone number is %s : "%phone + message
        receiver = settings.IZU 
        msg = EmailMultiAlternatives(subject, message, email, [receiver])
        msg.send()
        messages.success(request,"Message Sent. You Will Be Contacted Soon.")
        return redirect("/")
    else:
        return render(request,"building/contact.html")