import datetime
import time

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from . import models
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import datetime1, Register
from .forms import SignUpForm

# Create your views here.



# def home1(request):
#     return HttpResponse("Hello World Example of PFSD Project")
#
# def fun1(request):
#     return HttpResponse("<h1>2100030271 - K.Durga Sahithi</h1>")

def aboutfun(request):
    return render(request, 'about.html')
@login_required(login_url='index')

def fun2(request):
    return render(request, 'homepage.html')

def orderfunction(request):
    return render(request,'orderingfood.html')

def icecream(request):
    return render(request,'icecream.html')

def briyani(request):
    return render(request,'chickens.html')

def manch(request):
    return render(request,'manchurian.html')

def sharama(request):
    return render(request,'sharama.html')

def poppage(request):
    return render(request,'popup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'homepage.html')
            # assuming 'index' is a valid URL
        else:
            messages.info(request,'Invalid credentials')
            return render(request, 'login.html')

    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobileno = request.POST.get('mobileno')
        password = request.POST.get('password')
        password1=request.POST.get('password1')
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'newuserregister.html')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'newuserregister.html')
        return render(request, "login.html")
    else:
        return render(request, "newuserregister.html")


# def registerView(request):
#     if request.method=="POST":
#         form=SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login.html')
#     else:
#             form=SignUpForm()
#     return render(request,'newuserregister.html',{'form': form})



# def datetimefun(request):
#     var1=time.asctime(time.localtime(time.time()))
#     #To insert into database
#     data=datetime1(time12=var1)
#     data.save()
#     return HttpResponse(var1)

# def newregpage(request):
#     if request.method == "POST":
#        form=RegForm(request.POST)
#        if form.is_valid():
#             try:
#                form.save()
#                return redirect('/loginfun/')
#             except:
#                 pass
#     else:
#         form=RegForm()
#         return render(request,"newuserregister.html",{'form':form})


# def loginfun(request):
#     return render(request, 'login.html')
#
# def regfun(request):
#     return render(request, 'newuserregister.html')

# def contactus1(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         subject = request.POST['subject']
#         message=request.POST['message']
#         tosend=message+'----------------This is just the contactus mail----------------'
#         data=contactus(name=name,email=email,subject=subject,message=message)
#         data.save()
#         send_mail(
#             'Thank You for Contacting FHS System',
#             tosend,
#             'sahithikonakall11@gmail.com',
#             [email],
#             fail_silently=False
#         )
#         return HttpResponse("<h1><center>Mail Sent</center></h1>")
#     else:
#         return HttpResponse("<h1>Error</h1>")

def qrcode3(request):
    return render(request,'qrcode1.html')

import qrcode
from django.http import FileResponse
def qrcode12(request):
    if request.method == 'POST':
        sid=request.POST.get('sid')
        sname=request.POST.get('sname')
        data1=sid+sname
        #creating an instance of QRCode class
        qr=qrcode.QRCode(version=1,box_size=30,border=5)
        #Adding data to the instance 'qr'
        qr.add_data(data1)
        qr.make(fit=True)
        img=qr.make_image(fill_color='black',back_color='white')
        img.save('static/images/KLU.png')
        img1=open('static/images/KLU.png','rb')
        #rb-read binary
        response = FileResponse(img1)
        return response
    else:
        return HttpResponse("not working")

def weafun(request):
    return render(request, 'weather1.html')


import requests
def weather(request):
    api_key = 'a885f53c8efb25f65c7788ec104b4275'
    #user_input = input("Enter city: ")
    cname = request.POST.get('cname')
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={cname}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        #print("No City Found")
        return HttpResponse("No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        # °C = [(°F-32)×5] / 9
        temp1 = (((temp - 32) * 5) / 9)
        # print(type(temp))
        #print(f"The weather in {cname} is: {weather}")
        #print(f"The temperature in {cname} is: {temp}ºF")
        #print(f"The temperature in {cname} is: {temp1}ºC")

        return HttpResponse(temp1)


def feedback(request):
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Contact Form',
                  message+"Thank you",
                  settings.EMAIL_HOST_USER,
                  ['sahithikonakalla11@gmail.com'],
                  fail_silently=False)
    return render(request, 'feedback.html')


def contactfun(request):
    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Contact Form',
                  message+"\nThank you",
                  settings.EMAIL_HOST_USER,
                  # ['sahithikonakalla11@gmail.com'],
                  ['rehanashaik610@gmail.com'],
                  fail_silently=False)
    return render(request, 'contact.html')

# @login_required(login_url='index')