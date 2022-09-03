from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import pandas as pd
from django.http import HttpResponse


from .scrap import mercedes
from django.shortcuts import render
from .forms import ConcessionnaireForm, LoginForm, ClientForm
from .models import Concessionnaire, Car, Client
from django.db.models import Q
from django.shortcuts import redirect



# Create your views here.
def home1(request):
    #mercedes()
    if request.method == "POST":
        searched = request.POST['searched']

        multiple_search = Q(Q(name__icontains=searched)|Q(marque__icontains=searched)|Q(price__icontains=searched)|Q(mileage__icontains=searched)|Q(model__icontains=searched)|Q(gearbox__icontains=searched))

        data = Car.objects.filter(multiple_search)
        context={'cars':data }
        return render(request, 'home1.html',context)
    else:
        context={'cars':Car.objects.all()}
        return render(request,'home1.html',context)
def concessionnaire(request):
    concess = Concessionnaire.objects.get(email=request.session['Email'])
    if request.method == "POST":
        searched = request.POST['searched']
        multiple_search = Q(Q(name__icontains=searched)|Q(marque__icontains=searched)|Q(price__icontains=searched)|Q(mileage__icontains=searched)|Q(model__icontains=searched)|Q(gearbox__icontains=searched))
        data1 = Car.objects.filter(concessionnaire=concess)
        data = data1.filter(multiple_search)
        context={'cars':data }
        return render(request, 'compteConces.html',context)
    else:
        context={'cars':Car.objects.filter(concessionnaire=concess) }
        return render(request,'compteConces.html',context)


def client(request):
    client = Client.objects.get(email=request.session['Email'])

    multiple_search = Q(Q(name__icontains=client.getlast()) | Q(marque__icontains=client.lastVisite1))
    data1 = Car.objects.filter(multiple_search)

    if request.method == "POST":

        searched = request.POST['searched']
        multiple_search = Q(Q(name__icontains=searched) | Q(marque__icontains=searched))
        data = Car.objects.filter(multiple_search)
        client.lastVisite1 = searched
        print(client.lastVisite1)
        client.save()
        context = {'cars1': data1,'cars': data}
        return render(request, 'compteClient.html', context)
    else:

        context = {'cars1': data1,'cars': Car.objects.all()}
        return render(request, 'compteConces.html', context)


def contact(request):
    return render(request, 'contact.html')
def profil(request):
    if Client.objects.filter(email=request.session['Email']).exists():
        client = Client.objects.get(email=request.session['Email'])
        context = {'client': client}
        return render(request, 'profilClient.html', context)
    else:
        concess = Concessionnaire.objects.get(email=request.session['Email'])
        context = {'concessionnaire': concess}
        return render(request, 'profilConss.html', context)




def login(request):
    context = {'msg': ''}
    if request.method == 'POST':
        if Concessionnaire.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            concess = Concessionnaire.objects.get(email=request.POST['email'])
            request.session['Email'] = request.POST['email']
            context = {'cars': Car.objects.filter(concessionnaire=concess),'concessionnaire':concess}
            if request.POST['email'] == 'ynajims@gmail.com':
                return render(request, 'compteConces1.html', context)
            else :
                return render(request, 'compteConces.html', context)
                 
        elif Client.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            request.session['Email'] = request.POST['email']

            client1 = Client.objects.get(email=request.POST['email'])
            multiple_search = Q(Q(name__icontains=client1.getlast()) | Q(marque__icontains=client1.lastVisite1))
            data1 = Car.objects.filter(multiple_search)
            context = {'cars1': data1, 'cars': Car.objects.all(),'client':client1}
            return render(request, 'compteClient.html', context)
            # return client(request)
            # return client(request)
        else:
            context = {'msg': 'Invalid username or password'}
    return render(request, 'login.html', context)


def inscrire(request):
    if request.method == 'POST':
        add_concessionnaire= ConcessionnaireForm(request.POST)
        if add_concessionnaire.is_valid():
            add_concessionnaire.save()
            return redirect('/login')
        else:
            HttpResponse('wrong informations Dear Concessionnaire ')
    dict = {
      'concesForm':ConcessionnaireForm(),  
    }
     
    return render(request,'inscrire.html',dict)

def inscrireClient(request):
    if request.method == 'POST':
        add_client = ClientForm(request.POST)
        if add_client.is_valid():
            add_client.save()
            return redirect('/login')
        else :
            return HttpResponse('wrong informations dear Client')
    new_dict={
        'clientForm':ClientForm
    }
    return render(request,'client/clientInscription.html',new_dict)