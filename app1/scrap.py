from asyncio.windows_events import NULL
from contextlib import nullcontext
from pyexpat import model
from unicodedata import decimal

from bs4 import BeautifulSoup
import requests
import pandas as pd
from .models import *
def mercedes():
    concessionnaire1 = Concessionnaire.objects.first()
    for i in range(0,31,15):
    #for i in range(0,1):
        website_url = 'https://www.moteur.ma/fr/voiture/achat-voiture-occasion/recherche/?prix_max=999999999999999999999999999&per_page='+str(i)+''
        #website_url ='https://www.moteur.ma/fr/voiture/achat-voiture-occasion/recherche/?prix_max=999999999999999999999999999'
        response = requests.get(website_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        cars = soup.find_all('div', {'class', 'row-item'})
        for car in cars :

            try:
                img = str(car.find('img').get('data-original'))
            except:
                img = ""
            try:
                title = car.find('a', {'class': 'slide'}).get('href')
            except:
                title = ""
            website_url2 = title
            print(title)
            print("////////////////////////////////////")
            response = requests.get(website_url2)
            soup2 = BeautifulSoup(response.content, 'html.parser')
            try:
                name = str(soup2.find('span', {'class', 'text_bold'}).get_text().strip())
            except:
                name = ""
            try:
                price = str(soup2.find('div', {'class', 'color_primary text_bold price-block'}).get_text().strip())
            except:
                price = ""
                #col-md-12
            try:
                div = soup2.find('div', {'class', 'col-md-12'}).get_text().strip()
                description =soup2.select('#main > div > div > div.col-md-8.sidebar > div:nth-child(2) > div:nth-child(2) > div > div')[0].string.strip()
            except:
                description = ""

            details = soup2.find_all('div', {'class', 'detail_line'})
            # img = soup2.find('img',{'class','image-hb _web-inspector-hide-shortcut_'}).get('src')
            try:
                mileage = str(details[0].find('span', {'class', 'text_bold'}).get_text().strip())
            except:
                mileage = ""
            try:
                model = str(details[1].find('span', {'class', 'text_bold'}).get_text().strip())
            except:
                model = ""
            try:
                gearbox = str(details[2].find('span', {'class', 'text_bold'}).get_text().strip())
            except:
                gearbox = ""
            try:
                fuel = str(details[3].find('span', {'class', 'text_bold'}).get_text().strip())
            except:
                fuel = ""
            try:
                dateOfPub = str(details[4].find('span', {'class', 'text_bold'}).get_text().strip())
            except:
                dateOfPub = ""
            try:
                fiscalPower = str(details[5].find('span', {'class', 'text_bold'}).get_text().strip())
            except:
                fiscalPower = ""
            try:
                color = str(details[7].find('span', {'class', 'text_bold'}).get_text().strip())
            except:
                color = ""

            marque = name.split()[0]
            print(img)
            print(name.strip()+"\n"+mileage.strip()+"\n"+price.strip()+"\n"+model.strip()+"\n"+gearbox.strip()+"\n"+fuel.strip()+"\n"+dateOfPub+"\n"+fiscalPower+"\n"+color+"\n"+description)
            car = Car(name=name,mileage=mileage, img=img, price=price, category='',model=model,marque=marque,gearbox=gearbox,fuel=fuel,description=description,
                    dateOfPub=dateOfPub,fiscalPower=fiscalPower,color=color,concessionnaire=concessionnaire1)
            print(car)
            if Car.objects.filter(name=name,mileage=mileage,model=model ).exists() or img=='None':
                car = NULL
                print("\n car exists in database ")

            else :
                car.save()

"""
def searchScrap(searched):
    url = 'https://www.moteur.ma/fr/voiture/achat-voiture-occasion/recherche/?marque='+str(marque)+'&modele='+str(model)+'&carburant='+str(fuel)+'&boite='+str(gearbox)+'&prix_max='+str(price)+'&annee_min=2012&km='+str(mileage)+'&couleur='+str(color)+''
    marqueSearched = marque
    modelSearched = model
    fuelSearched = fuel
    gearboxSearched = gearbox
    priceSearched = price 
    mileageSearched = mileage
    colorSearched = color 
    
"""
# if Car.objects.filter(name=name, marque='', mileage=mileage[0], price=price[0],
#                       concessionnaire=concessionnaire1).exists():
#     name = []
#     mileage = []
#     price = []
#     rating = []
#     reviews = []
#     dealer = []
#     imgg = []
# else:
#     #car.save()
#     name = []
#     mileage = []
#     price = []
#     rating = []
#     reviews = []
#     dealer = []
#     imgg = []
