from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, Group, Permission
from manager.models import Manager


# Create your views here.
def home(request):
    site = "Mysite"
    news_dt = News.objects.filter(confirm = 1)
    cat = Cat.objects.all()
    popnews = News.objects.filter(confirm = 1).order_by('-show')
    subcat = SubCat.objects.all()
    lastnews = News.objects.filter(confirm = 1).order_by('-pk')[:3]
    return render(request, 'front/home.html',{'site' : site, 'news' : news_dt, 'cat' : cat, 'subcat' : subcat, 'lastnews' : lastnews, 'popnews' : popnews})

def about(request):
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    site = "Mysite"
    popnews = News.objects.filter(confirm = 1).order_by('-show')
    return render(request, 'front/about.html', {'site' : site, 'popnews' : popnews, 'cat' : cat, 'subcat' : subcat})

def panel(request):
    
    if not request.user.is_authenticated:
        return redirect('mylogin')
    
    perms = Permission.objects.filter(user = request.user)
    return render(request, 'back/home.html', {})
    
def mylogin(request):

    if request.user.is_authenticated:
        return redirect('panel')
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(username != "" and password != ""):
            user = authenticate(username = username, password = password)
            if(user != None):
                login(request, user)
                user = User.objects.get(username = username)
                return redirect('panel')
            else:
                return redirect('mylogin')
        else:
            return redirect('mylogin')
    return render(request, 'front/login.html')

def mylogout(request):
    logout(request)
    return redirect('mylogin')

def sitesettings(request):
        # login check start
    if not request.user.is_authenticated :
        return redirect('mylogin')
    # login check end
    if request.method == 'POST' :

        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        link = request.POST.get('link')
        txt = request.POST.get('txt')

        if fb == "" : fb = "#"
        if tw == "" : tw = "#"
        if yt == "" : yt = "#"
        if link == "" : link = "#"

        try : 
    
            myfile = request.FILES['myfile']
            
            fs = FileSystemStorage()
    
            filename = fs.save(myfile.name, myfile)

            url = fs.url(filename)

            picurl = url
        
            picname = filename
            
        except :
            picurl = "-"
            picname = "-"



        try : 

            myfile2 = request.FILES['myfile2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)
            url2 = fs2.url(filename2)

            picurl2 = url2
            picname2 = filename2

        except :
            picurl2 = "-"
            picname2 = "-"



        b = Main.objects.get(pk=2)
        b.name = name
        b.tell = tell
        b.fb = fb
        b.tw = tw
        b.yt = yt
        b.link = link
        b.about = txt
        
        if picurl != "-" : b.picurl = picurl
        if picname != "-" : b.picname = picname
        if picurl2 != "-" :  b.picurl2 = picurl2
        if picname2 != "-" : b.picname2 = picname2
        
        b.save()


       


    site = Main.objects.get(pk=2)


    return render(request, 'back/setting.html', {'site':site})

def contact(request):
    news = News.objects.all()
    subcat = SubCat.objects.all()
    site = Main.objects.get(pk = 2)
    popnews = News.objects.all().order_by('-show')[:3]
    cat = Cat.objects.all()
    return render(request, 'front/contact.html', {'site' : site, 'popnews' : popnews, 'cat' : cat, 'subcat' : subcat, 'news' : news})

def change_pass(request):
    if(request.method == 'POST'):
        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')
        
        if(oldpass == '' or newpass == ''):
            error = 'All fields required'
            return render(request, 'back/error.html', {'error' : error})
        
        user = authenticate(username = request.user, password = oldpass)
        if user != None :

            if len(newpass) < 8 :
                error = "Your Password Most Be At Less 8 Character"
                return render(request, 'back/error.html' , {'error':error})
                
            user = User.objects.get(username = request.user)
            user.set_password(newpass)
            user.save()
            return redirect('mylogout')
        
        error = 'Wrong password'
        return render(request, 'back/error.html', {'error' : error})
    return render(request, 'back/changepass.html')

def myregister(request):
    
    if request.method == 'POST':

        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        
        if password1 != password2 :
            msg = "Your Pass Didn't Match"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if len(password1) < 8 :
            msg = "Your Pass Must Be 8 Character"
            return render(request, 'front/msgbox.html', {'msg':msg})

        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0 :
            user = User.objects.create_user(username=uname,email=email,password=password1)
            user.save()
            q = Manager(name = name, username = uname, password = password1, email = email)
            q.save()
            user = authenticate(username = uname, password = password1)
            login(request, user)
            user = User.objects.get(username = uname)
            return redirect('panel')

        if(len(User.objects.filter(username=uname))):
            msg = 'Username already taken.'
            return render(request, 'front/msgbox.html', {'msg':msg})
        if len(User.objects.filter(email=email)):
            msg = 'Email already taken.'
            return render(request, 'front/msgbox.html', {'msg':msg})

    return render(request, 'front/login.html')
