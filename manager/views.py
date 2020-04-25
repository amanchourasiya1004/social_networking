from django.shortcuts import render, get_object_or_404, redirect
from .models import Manager
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager
from django.contrib.contenttypes.models import ContentType

def manager_list(request):
    if not request.user.is_authenticated:
        return redirect('mylogin')
    managers = Manager.objects.all()
    return render(request, 'back/manager_list.html', {'manager' : managers})

def manager_delete(request, pk):
    if not request.user.is_authenticated:
        return redirect(request, 'mylogin')
    
    manager = Manager.objects.get(pk=pk)
    b = User.objects.filter(username=manager.username)
    b.delete()

    manager.delete()
    return redirect('manager_list')

def manager_group(request):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    
    group = Group.objects.all()

    return render(request, 'back/manager_group.html', {'group':group})



def manager_group_add(request):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    if request.method == 'POST' :

        name = request.POST.get('name')

        if name != "" :

            if len(Group.objects.filter(name=name)) == 0 :

                group = Group(name=name)
                group.save()
    
    

    return redirect('manager_group')

def manager_group_del(request, name):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    g = Group.objects.filter(name = name)
    g.delete()

    return redirect('manager_group')

def user_groups_show(request, pk):


     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    manager = Manager.objects.get(pk = pk)
    user = User.objects.get(username = manager.username)
    ugroup = []
    for i in user.groups.all():
        ugroup.append(i)
    group = Group.objects.all()
    return render(request, 'back/users_groups.html', {'ugroup':ugroup, 'group':group, 'pk':pk})


def add_users_to_groups(request,pk):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    if request.method == 'POST' :

        gname = request.POST.get('gname')

        group = Group.objects.get(name=gname)
        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.username)
        user.groups.add(group)
    
    

    return redirect('user_groups_show' , pk=pk)


def del_users_to_groups(request,pk,name):


     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    

    group = Group.objects.get(name=name)
    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.username)
    user.groups.remove(group)
    
    

    return redirect('user_groups_show' , pk=pk)

def manager_perms(request):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    permis = Permission.objects.all()
    return render(request, 'back/manager_perms.html', {'permis' : permis})

def manager_perms_add(request):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    if request.method == 'POST':
        name = request.POST.get('name')
        codename = request.POST.get('cname')

        if(name != '' and codename != ''):
            content_type = ContentType.objects.get(app_label = 'main', model = 'main')
            permission = Permission.objects.create(codename = codename, name = name, content_type = content_type)
            return redirect('manager_perms')
        else:
            return render(request, 'back/error.html', {'error' : "All fields required."})

    return redirect('manager_perms')

def manager_perms_del(request, name):

     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    perms = Permission.objects.filter(name = name)
    perms.delete()
    return redirect('manager_perms')

def user_perms(request, pk):
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    perms = Permission.objects.all()
    manager = Manager.objects.get(pk = pk)
    user = User.objects.get(username = manager.username)
    permission = Permission.objects.filter(user = user)
    uperms = []
    for i in permission:
        uperms.append(i.name)
    return render(request, 'back/user_perms.html', {'uperms' : uperms, 'perms' : perms, 'pk' : pk})

def user_perms_add(request, pk):

    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    if request.method == 'POST' :

        pname = request.POST.get('pname')

        manager = Manager.objects.get(pk=pk)
        user = User.objects.get(username=manager.username)

        permission = Permission.objects.get(name=pname)
        user.user_permissions.add(permission)

    return redirect('user_perms' , pk=pk)

def user_perms_del(request, pk, name):

    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    manager = Manager.objects.get(pk=pk)
    user = User.objects.get(username=manager.username)

    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)

    return redirect('user_perms' , pk = pk)

def groups_perms(request,name):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    group = Group.objects.get(name=name)
    perms = group.permissions.all()

    allperms = Permission.objects.all()

    return render(request, 'back/group_perms.html', {'perms':perms, 'name':name, 'allperms':allperms})


def groups_perms_del(request,gname,name):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})

    group = Group.objects.get(name=gname)
    perm = Permission.objects.get(name=name)

    group.permissions.remove(perm)

    return redirect('group_perms', name=gname)


def groups_perms_add(request,name):
    
     # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end


    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})


    if request.method == 'POST' :

        pname = request.POST.get('pname')

        group = Group.objects.get(name=name)
        perm = Permission.objects.get(name=pname)

        group.permissions.add(perm)

    return redirect('group_perms', name=name)


    