from django.db import models
from django import forms

# Create your models here.
from django.urls import reverse


class Client(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=50)
    birth = models.DateField(auto_now=False, auto_now_add=False)
    lastVisite1 = models.CharField(max_length=200)

    def getlast(self):
        return self.lastVisite1

    class Meta:
        verbose_name = ("Client")
        verbose_name_plural = ("Clients")

    def __str__(self):
        return self.lastName

    #def get_absolute_url(self):
      #  return reverse("Client_detail", kwargs={"pk": self.pk})


class Concessionnaire(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=200)
    companyLocation = models.CharField(max_length=50)
    companyName = models.CharField(max_length=200)
    companyDesc = models.TextField()
    
    class Meta:
        verbose_name = ("Concessionnaire")
        verbose_name_plural = ("Concessionnaires")

    def __str__(self):
        return self.lastName

    #def get_absolute_url(self):
        #return reverse("Concessionnaire_detail", kwargs={"pk": self.pk})


class ForeignConcessionnaire(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=200)
    companyLocation = models.CharField(max_length=50)
    companyName = models.CharField(max_length=200)
    companyDesc = models.TextField()

    class Meta:
        verbose_name = ("ForeignConcessionnaire")
        verbose_name_plural = ("ForeignConcessionnaires")

    def __str__(self):
        return self.lastName

    #def get_absolute_url(self):
       # return reverse("ForeignConcessionnaire_detail", kwargs={"pk": self.pk})


class Car(models.Model):
    name = models.CharField(max_length=250)
    marque = models.CharField(max_length=250)
    mileage = models.CharField(max_length=250)
    model = models.CharField(max_length=250, null=True)
    price = models.CharField(max_length=250)
    category = models.CharField(max_length=250, null=True,default='something')
    img = models.ImageField(upload_to="photos")
    description = models.TextField(("write something"), null=True)
    concessionnaire = models.ForeignKey(Concessionnaire,verbose_name=("concessionnaire"), on_delete=models.CASCADE)
    gearbox = models.CharField(max_length=220, null=True)
    fuel = models.CharField(max_length=220, null=True)
    dateOfPub = models.CharField(max_length=220, null=True)
    fiscalPower = models.CharField(max_length=200,null=True)
    color = models.CharField(max_length=220, null=True)
    class Meta:
        verbose_name = ("Car")
        verbose_name_plural = ("Cars")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('car:single',args=[self.id])

    #def get_absolute_url(self):
       #return reverse("Car_detail", kwargs={"pk": self.pk})

class Website(models.Model):
    url = models.CharField(max_length=255)
    class Meta:
        verbose_name = ("Website")
        verbose_name_plural = ("Websites")



    #def get_absolute_url(self):
        #return reverse("Websites_detail", kwargs={"pk": self.pk})

class Annonce(models.Model):
    idCar = models.ForeignKey(Car, verbose_name=("car"), on_delete=models.CASCADE)
    idConcessionnaire = models.ForeignKey(Concessionnaire, verbose_name=("concessionnaire"), on_delete=models.CASCADE)
    idWebsite = models.ForeignKey(Website, verbose_name=("Website"), on_delete=models.CASCADE)
    datePublication = models.DateField()
    class Meta:
        verbose_name = ("Annonce")
        verbose_name_plural = ("Annonces")


    #def get_absolute_url(self):
       # return reverse("Annonce_detail", kwargs={"pk": self.pk}
