from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager
import datetime
import time


def news_cm_add(request, pk):
    if request.method == 'POST':
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        
        if len(str(day)) == 1 :
            day = "0" + str(day)
        if len(str(month)) == 1 :
            month = "0" + str(month)

    
        date = str(year) + "/" + str(month) + "/" + str(day)
        time = str(now.hour) + ":" + str(now.minute)

        msg = request.POST.get('msg')
        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            c = Comment(name = user.username, email = user.email, comment = msg, news_id = pk, date = date, time = time)
            c.save()

        else:

            name = request.POST.get('name')
            email = request.POST.get('email')

            b = Comment(name=name,email=email,comment=msg,news_id=pk,date=date,time=time)
            b.save()
            

    newsname = News.objects.get(pk=pk).name

    return redirect('news_detail' , word=newsname)

def comments_list(request):

    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    comment = Comment.objects.all()
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        user = User.objects.get(username = request.user)
        comment = Comment.objects.filter(name = user.username)
    

    

    return render(request, 'back/comments_list.html', {'comment':comment})



def comments_del(request, pk):
    
    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        a = Comment.objects.get(pk = pk).name
        if a != str(request.user) :
            error = "Access Denied"
            return render(request, 'back/error.html' , {'error':error})
    

    comment = Comment.objects.filter(pk=pk)
    comment.delete()

    return redirect('comments_list')


def comments_confirm(request,pk):
    
    # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if(perm == 0):
        error = "Access Denied"
        return render(request, 'back/error.html' , {'error':error})
    

    comment = Comment.objects.get(pk=pk)
    comment.status = 1
    comment.save()

    return redirect('comments_list')
            