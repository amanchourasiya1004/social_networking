from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name= 'about'),
    path('panel/', views.panel, name= 'panel'),
    path('contact/', views.contact, name= 'contact'),
    path('login/', views.mylogin, name= 'mylogin'),
    path('logout/', views.mylogout, name= 'mylogout'),
    path('panel/setting/', views.sitesettings, name= 'sitesettings'),
    path('panel/change/pass/', views.change_pass, name= 'change_pass'),
    path('register/', views.myregister, name= 'myregister'),
]