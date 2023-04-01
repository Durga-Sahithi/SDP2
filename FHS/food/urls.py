from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home,name='home'),
    #path('demo/',views.fun1,name='function1'),
    path('',views.fun2,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('aboutfun',views.aboutfun,name='aboutfun'),
    path('contactfun',views.contactfun,name='contactfun'),
    path('poppage',views.poppage,name='poppage'),
    path('link5',views.orderfunction,name='ordering'),
    path('link6',views.icecream,name='icecream'),
    path('link7',views.briyani,name='biryanis'),
    path('link8',views.manch,name='manchurian'),
    path('link9',views.sharama,name='shawarma'),
    path('link10',views.feedback,name='feedback')
    #path('register',views.registerView,name='register')
    #path('dt/',views.datetimefun,name='dtfun'),
    #path('qrcode1/',views.qrcode12,name='qrcode1'),
    #path('qrcd/',views.qrcode3,name='qrcd'),
    #path('weather1/',views.weather,name='weather1'),
    #path('w1/',views.weafun,name='w1'),
    #path('con/',views.contactus1,name='con'),
    #path('rp/',views.newregpage,name='rp'),
]