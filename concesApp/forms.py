from urllib import request

from django import forms
from .models import Post
from app1.models import Car, Concessionnaire



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields ='__all__' #("title","description","time")


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields ='__all__' #("name","marque","mileage","model","price","img","description","gearbox","fuel","dateOfPub","fiscalPower","color")


