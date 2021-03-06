from django.urls import path
from . import views

urlpatterns = [
    path('comment/add/<int:pk>/', views.news_cm_add, name = 'news_cm_add'),
    path('comments/list/', views.comments_list, name = 'comments_list'),
    path('comment/del/<int:pk>/', views.comments_del, name = 'comments_del'),
    path('comment/confirm/<int:pk>/', views.comments_confirm, name = 'comments_confirm'),
    path('comment/answer/<int:pk>/', views.comments_answer, name = 'comments_answer'),
]