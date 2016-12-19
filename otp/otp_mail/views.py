from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.core.mail import send_mail
from models import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def send_otp(request):
    email = request.GET.get('email')
    username = request.GET.get('name')
    last_otp_used = User.objects.all()
    if last_otp_used:
        last_otp_used = last_otp_used.last().otp
    else:
        last_otp_used = 0
    last_otp_used += 1
    User.objects.create(email=email, name=username, otp=last_otp_used)
    send_mail(
        'Authentication OTP',
        'Hey ' + username + ',\n Your OTP for authentication is ' + str(last_otp_used),
        'archit.bansal18@gmail.com',
        [email],
        fail_silently=False,
    )
    return HttpResponse(last_otp_used);

def check_otp(request):
    email = request.GET.get('email')
    otp = request.GET.get('otp')
    actual_otp = User.objects.filter(email=email)
    if actual_otp:
        actual_otp = actual_otp.first().otp
    else:
        return HttpResponse('Email not registered')
    if int(actual_otp) == int(otp):
        return HttpResponse('Success')
    return HttpResponse('Failure')
