from django.urls import path
from . import views

urlpatterns = [
    path('news/<str:word>/', views.news_detail, name='news_detail'),
    path('panel/news/list/', views.news_list, name='news_list'),
    path('panel/news/add/', views.news_add, name='news_add'),
    path('panel/news/publish/<int:pk>/', views.news_publish, name='news_publish'),
    path('panel/news/unpublish/<int:pk>/', views.news_unpublish, name='news_unpublish'),
    path('panel/news/del/<int:pk>/', views.delete_news, name='news_delete'),
    path('panel/news/edit/<int:pk>/', views.news_edit, name='news_edit'),
]