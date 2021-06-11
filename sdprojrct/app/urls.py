from django.core.mail import send_mail
from django.urls import path,include
from . import views
#from views import sendanemail
urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('work/',views.work,name='work'),
    path('logout/',views.logout,name='logout'),
    path('mail/',views.sendanemail,name='mail'),
    path('soccergo/', views.soccergo, name='soccergo'),
    path('profile/',views.profile,name='profile'),
    path('horsego/',views.horsego,name='horsego'),
    path('F1go/',views.F1go,name='F1go'),
    path('news/',views.news,name='news'),
    path('paypal/',views.paypal,name='paypal'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contact,name='contact'),
]