import scrapy

class CarSpider(scrapy.Spider):
    name="car"
    marque=''
    color=''
    carburant=''
    model=''
    start_urls=[
        'https://www.moteur.ma/fr/voiture/achat-voiture-occasion/recherche/?marque='+marque+'&modele='+model+'&carburant='+carburant+'&boite=Automatique&annee_min=2022&couleur='+color+''
    ]
    def parse(self,response):
        #page = response.url.split('/')[-1]
        #page=response.url
        #marque='mercedes'
        #file_name = 'caris.html'
        #with open(file_name,'wb') as f :
            #f.write(response.body)
            print(response.css('title'))




