from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from subcat.models import SubCat
from django.core.files.storage import FileSystemStorage
import datetime
from cat.models import Cat
from django.contrib.auth.models import User, Group, Permission
from comment.models import Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def news_detail(request, word):
    comment = Comment.objects.filter(status = 1)
    cmcount = len(comment)
    site = Main.objects.get(pk = 2)
    news_d = News.objects.get(name = word)
    cat = Cat.objects.all()
    news = News.objects.filter(confirm = 1)
    subcat = SubCat.objects.all()
    news_d.show += 1
    news_d.save()
    popnews = News.objects.filter(confirm = 1).order_by('-show')
    tag = news_d.tags.split(',')
    return render(request, 'front/news_detail.html', {'shownews' : news_d, 'site' : site, 'cat' : cat, 'news' : news, 'subcat' : subcat, 'popnews' : popnews, 'tag' : tag, 'code' : news_d.pk, 'cmcount' : cmcount, 'comment' : comment})
    
def news_list(request):
    if not request.user.is_authenticated:
        return redirect('mylogin')
    news = News.objects.all()
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser" : perm = 1

    if perm == 0 :
        news = News.objects.filter(writer=request.user)
    elif perm == 1 :
        newss = News.objects.all()
        paginator = Paginator(newss,2)
        page = request.GET.get('page')

        try:
            news = paginator.page(page)

        except EmptyPage :
            news = paginator.page(paginator.num_pages)

        except PageNotAnInteger :
            news = paginator.page(1)
        
    
    return render(request, 'back/news_list.html', {'news':news})

def news_add(request):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    subcat = SubCat.objects.all()
    d = datetime.datetime.now()
    year = str(d.year)
    month = str(d.month)
    day = str(d.day)
    if(len(day) == 1):
        day = "0" + day
    if(len(month) == 1):
        month = "0" + month
    dt = year + "/" + month + "/" + day
    if request.method == 'POST':
        body_tx = request.POST.get('newst')
        title = request.POST.get('newstitle')
        short_tx = request.POST.get('newstxtshort')
        newsid = request.POST.get('newscat')
        tag_t = request.POST.get('tag')
        cat = SubCat.objects.get(pk = newsid)
        myfile = request.FILES['files']
        f = FileSystemStorage()
        ocatid = cat.catid
        filename = f.save(myfile.name, myfile)
        url = f.url(filename)
        q = News(name = title, short_txt = short_tx, body_txt = body_tx, date = dt, pic = url, writer = request.user, tags = tag_t, catname = cat, views = 0, catid = newsid, picname = filename, ocatid = ocatid)
        q.save()
        b = len(News.objects.filter(ocatid = ocatid))
        q = Cat.objects.get(pk = ocatid)
        q.count = b
        q.save()
        return redirect('news_list')
    return render(request, 'back/news_add.html', {'subcat' : subcat})

def delete_news(request, pk):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    perms = Permission.objects.filter(user = request.user)
    for i in perms:
        if i.name == 'master_user':
            perm = 1
    if(perm == 0):
        a = News.objects.get(pk = pk).writer
        if str(a) != str(request.user):
            return render(request, 'back/error.html', {'error' : "Access Denied."})

    q = News.objects.get(pk = pk)
    fs = FileSystemStorage()
    fs.delete(q.picname)
    ocatid = q.ocatid
    q.delete()
    b = len(News.objects.filter(ocatid = ocatid))
    q = Cat.objects.get(pk = ocatid)
    q.count = b
    q.save()
    return redirect('news_list')

def news_edit(request, pk):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    perm = 0
    perms = Permission.objects.filter(user = request.user)
    for i in perms:
        if i.name == 'master_user':
            perm = 1
    if(perm == 0):
        a = News.objects.get(pk = pk).writer
        if str(a) != str(request.user):
            return render(request, 'back/error.html', {'error' : "Access Denied."})
    news_it = News.objects.all()
    news = News.objects.get(pk = pk)
    subcat = SubCat.objects.all()
    d = datetime.datetime.now()
    year = str(d.year)
    month = str(d.month)
    day = str(d.day)
    if(len(day) == 1):
        day = "0" + day
    if(len(month) == 1):
        month = "0" + month
    dt = year + "/" + month + "/" + day
    if request.method == 'POST':
        fs = FileSystemStorage()
        fs.delete(news.picname)
        body_tx = request.POST.get('newst')
        title = request.POST.get('newstitle')
        short_tx = request.POST.get('newstxtshort')
        newsid = request.POST.get('newscat')
        tag_t = request.POST.get('tag')
        write = request.POST.get('writer')
        cat = SubCat.objects.get(pk = newsid)
        myfile = request.FILES['files']
        f = FileSystemStorage()
        filename = f.save(myfile.name, myfile)
        url = f.url(filename)
        news.body_txt = body_tx
        news.short_txt = short_tx
        news.name = title
        news.catid = newsid
        news.tags = tag_t
        news.writer = write
        news.pic = url
        news.picname = filename
        news.catname =cat.name
        news.date = dt
        if perm == 0:
            news.confirm = 0
        else:
            news.confirm = 1
        news.save()
        return redirect('news_list')
    else:
        return render(request, 'back/news_edit.html', {'news' : news, 'subcat' : subcat})

def news_publish(request, pk):
    perm = 0
    perms = Permission.objects.filter(user = request.user)
    for i in perms:
        if i.name == 'master_user':
            perm = 1
    if(perm == 0):
        return render(request, 'back/error.html', {'error' : "Not authorized to publish."})

    news = News.objects.get(pk = pk)
    news.confirm = 1
    news.save()
    return redirect('news_list')

def news_unpublish(request, pk):
    perm = 0
    perms = Permission.objects.filter(user = request.user)
    for i in perms:
        if i.name == 'master_user':
            perm = 1
    if(perm == 0):
        return render(request, 'back/error.html', {'error' : "Not authorized to publish."})

    news = News.objects.get(pk = pk)
    news.confirm = 0
    news.save()
    return redirect('news_list')