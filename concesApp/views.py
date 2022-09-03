from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from app1.models import Concessionnaire,Car
from .forms import PostForm,CarForm
from .models import Post


def concessionnaire(request):
    concess = Concessionnaire.objects.get(email=request.session['Email'])
    if request.method == "POST":
        searched = request.POST['searched']
        multiple_search = Q(Q(name__icontains=searched)|Q(marque__icontains=searched)|Q(price__icontains=searched)|Q(mileage__icontains=searched)|Q(model__icontains=searched)|Q(gearbox__icontains=searched))
        data1 = Car.objects.filter(concessionnaire=concess)
        data = data1.filter(multiple_search)
        context={'concessionnaire':concess,'cars':data }
        return render(request, 'compteConces.html',context)
    context = {'cars': Car.objects.filter(concessionnaire=concess),'concessionnaire':concess}
    return render(request,'concessionnaire/posts.html',context)


def concessionnaire1(request):
    concess = Concessionnaire.objects.get(email=request.session['Email'])
    if request.method == "POST":
        searched = request.POST['searched']
        multiple_search = Q(Q(name__icontains=searched) | Q(marque__icontains=searched) | Q(price__icontains=searched) | Q(
            mileage__icontains=searched) | Q(model__icontains=searched) | Q(gearbox__icontains=searched))
        data1 = Car.objects.filter(concessionnaire=concess)
        data = data1.filter(multiple_search)
        context = {'concessionnaire': concess, 'cars': data}
        return render(request, 'compteConces.html', context)
    context = {'cars': Car.objects.filter(
        concessionnaire=concess), 'concessionnaire': concess}
    return render(request, 'concessionnaire/posts1.html', context)

def update(request,id):
    car_id = Car.objects.get(id=id)
    if request.method == 'POST':
        car_save = CarForm(request.POST,request.FILES ,instance=car_id)
        if car_save.is_valid():
            car_save.save()
            return redirect('/login/myPosts')
    else:
        car_save = CarForm(instance=car_id)
    context={
        'CarForm':car_save
    }
    return render(request,'concessionnaire/update.html',context)


def update1(request, id):
    car_id = Car.objects.get(id=id)
    if request.method == 'POST':
        car_save = CarForm(request.POST, request.FILES, instance=car_id)
        if car_save.is_valid():
            car_save.save()
            return redirect('/login/posta')
    else:
        car_save = CarForm(instance=car_id)
    context = {
        'CarForm': car_save
    }
    return render(request, 'concessionnaire/update.html', context)

def delete(request,id):
    car_delete = get_object_or_404(Car,id=id)
    if request.method =='POST':
        car_delete.delete()
        return redirect('/login/myPosts')
    return render(request,'concessionnaire/delete.html')


def delete1(request, id):
    car_delete = get_object_or_404(Car, id=id)
    if request.method == 'POST':
        car_delete.delete()
        return redirect('/login/posta')
    return render(request, 'concessionnaire/delete.html')
    
def addCar(request):
    concess = Concessionnaire.objects.get(email=request.session['Email'])
    initial_data = {
        'concessionnaire':concess
    }
    context={
        'CarForm':CarForm
    }
    if request.method == 'POST':
        carForm = CarForm(request.POST,request.FILES,initial=initial_data)
        if carForm.is_valid():
            carForm.save()
            return  redirect('/login/myPosts')
    return render(request,'concessionnaire/addCar.html',context)


def addCar1(request):

    concess = Concessionnaire.objects.get(email=request.session['Email'])
    initial_data = {
        'concessionnaire': concess
    }
    context = {
        'CarForm': CarForm
    }
    if request.method == 'POST':
        carForm = CarForm(request.POST, request.FILES, initial=initial_data)
        if carForm.is_valid():
            carForm.save()
            return redirect('/login/posta')
    return render(request, 'concessionnaire/addCar.html', context)
