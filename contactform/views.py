from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import login, logout, authenticate
from django.core.files.storage import FileSystemStorage
import datetime

def contact_add(request):
    if(request.method == 'POST'):
        d = datetime.datetime.now()
        year = str(d.year)
        month = str(d.month)
        day = str(d.day)
        if(len(day) == 1):
            day = "0" + day
        if(len(month) == 1):
            month = "0" + month
        dt = year + "/" + month + "/" + day
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        if(name == "" or email == "" or msg == ""):
            return render(request, 'front/msgbox.html', {'msg' : "All fields required."})
        
        q = Contact(name = name, email = email, msg = msg, date = dt)
        q.save()

        return render(request, 'front/msgbox.html', {'msg' : "Message received"})  
    return render(request, 'front/msgbox.html', {'msg' : "Message received"})   

def contactform(request):
    message = Contact.objects.all()
    return render(request, 'back/contact_form.html', {'message' : message})  

def delete_contact(request, p):
    q = Contact.objects.get(pk = p)
    q.delete()
    return redirect('contactform')

