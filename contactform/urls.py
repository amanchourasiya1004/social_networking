from django.urls import path
from . import views

urlpatterns = [
    path('contact/submit/', views.contact_add, name = 'contact_add'),
    path('panel/contactform/', views.contactform, name = 'contactform'),
    path('panel/contactform/del/<int:p>/', views.delete_contact, name = 'delete_contact'),
]