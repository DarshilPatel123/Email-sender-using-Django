from email import message
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'customer/home.html')

def sending(request):
    to=request.POST['to']
    subject=request.POST['subject']
    message=request.POST['message']
    send_mail(subject,message,settings.EMAIL_HOST_USER,[to],fail_silently=False)
    messages.success(request,'Email sent successfully')
    return redirect('/customer/')