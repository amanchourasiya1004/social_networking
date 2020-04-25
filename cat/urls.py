from django.urls import path
from . import views

urlpatterns = [
    path('panel/category/add/', views.cat_add, name = 'cat_add'),
    path('panel/category/list/', views.cat_list, name= 'cat_list'),
    path('panel/category/del/<int:pk>/', views.delete_cat, name= 'cat_delete'),
    path('export/csv/', views.export_cat_csv, name= 'export_cat_csv'),
    path('import/csv/', views.import_cat_csv, name= 'import_cat_csv'),
]