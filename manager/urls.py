from django.urls import path
from . import views

urlpatterns = [
    path('panel/manager/list/', views.manager_list, name = 'manager_list'),
    path('panel/manager/del/<int:pk>/', views.manager_delete, name = 'manager_delete'),
    path('panel/manager/group/', views.manager_group, name = 'manager_group'),
    path('panel/manager/group/add/', views.manager_group_add, name = 'manager_group_add'),
    path('panel/manager/group/del/<name>', views.manager_group_del, name = 'manager_group_del'),
    path('panel/manager/group/show/<int:pk>/', views.user_groups_show, name = 'user_groups_show'),
    path('panel/manager/addtogroup/<int:pk>/', views.add_users_to_groups, name = 'add_users_to_groups'),
    path('panel/manager/deltogroup/<int:pk>/<name>/', views.del_users_to_groups, name = 'del_users_to_groups'),
    path('panel/manager/perms/', views.manager_perms, name = 'manager_perms'),
    path('panel/manager/perms/del/<name>/', views.manager_perms_del, name = 'manager_perms_del'),
    path('panel/manager/perms/add/', views.manager_perms_add, name = 'manager_perms_add'),
    path('panel/manager/user/perms/add/<int:pk>/', views.user_perms_add, name = 'user_perms_add'),
    path('panel/manager/user/perms/<int:pk>/', views.user_perms, name = 'user_perms'),
    path('panel/manager/perms/del/<int:pk>/<name>/', views.user_perms_del, name = 'user_perms_del'),
    path('panel/manager/group/perms/<name>/', views.groups_perms, name = 'group_perms'),
    path('panel/manager/group/perms/add/<name>/', views.groups_perms_add, name = 'group_perms_add'),
    path('panel/manager/group/perms/del/<gname>/<name>/', views.groups_perms_del, name = 'group_perms_del'),
]