from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat
from django.http import HttpResponse
import csv

def cat_list(request):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    # login check start
    #if not request.user.is_authenticated :
     #   return redirect('mylogin')
    # login check end

    cat = Cat.objects.all()

    return render(request, 'back/cat_list.html', {'cat':cat})

def cat_add(request):
    if not request.user.is_authenticated:
        return redirect('mylogin')

    # login check start
    #if not request.user.is_authenticated :
     #   return redirect('mylogin')
    # login check end
    
    if request.method == 'POST':

        name = request.POST.get('name')

        if name == "" :

            error = "All Fields Requirded"
            return render(request, 'back/error.html' , {'error':error})

        if len(Cat.objects.filter(name=name)) != 0 :

            error = "This Name Used Before"
            return render(request, 'back/error.html' , {'error':error})

        b = Cat(name=name)
        b.save()
        return redirect('cat_list')
    
    return render(request, 'back/cat_add.html')

def delete_cat(request, pk):
    if not request.user.is_authenticated:
        return redirect('mylogin')
    q = Cat.objects.get(pk = pk)
    q.delete()
    return redirect('cat_list')

def export_cat_csv(request):
    resp = HttpResponse(content_type = 'text/csv')
    resp['Content-Disposition'] = 'attachment; filename = "cat.csv"'
    writer = csv.writer(resp)
    writer.writerow(['Title', 'Counter'])
    cat = Cat.objects.all()
    for i in cat:
        writer.writerow([i.name, i.count])

    return resp

def import_cat_csv(request):

    if request.method == 'POST' :

        csv_file = request.FILES['csv_file']

        if not csv_file.name.endswith('.csv'):
            error = "Please Input Csv File"
            return render(request, 'back/error.html' , {'error':error})

        if csv_file.multiple_chunks():
            error = "File Too Large"
            return render(request, 'back/error.html' , {'error':error})

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")

        for line in lines :

            fields =line.split(",")

            try:

                if len(Cat.objects.filter(name=fields[0])) == 0 and fields[0] != "Title" and fields[0] != "" :
                    b = Cat(name=fields[0])
                    b.save()
               
            except:
                print("finish")

    return redirect('cat_list')

