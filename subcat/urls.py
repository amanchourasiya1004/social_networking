from django.urls import path
from . import views

urlpatterns = [
    path('panel/subcategory/add/', views.subcat_add, name = 'subcat_add'),
    path('panel/subcategory/list/', views.subcat_list, name= 'subcat_list'),
]