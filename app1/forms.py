from django import forms 
from .models import Concessionnaire, Client


class ConcessionnaireForm(forms.ModelForm):
    class Meta:
        model = Concessionnaire
        widgets = {
            'password':forms.PasswordInput()
        }
        fields = '__all__'
    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        if '@gmail' in email:
            return email
        else :
            raise forms.ValidationError('this is not a valid email')

class LoginForm(forms.ModelForm):
    email = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=16, required=True)
    class Meta:
        model = Concessionnaire
        fields = ("email","password")
    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        if '@gmail' in email:
            return email
        else :
            raise forms.ValidationError('this is not a valid email')


class ClientForm(forms.ModelForm):
    class Meta:
        model= Client
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = ("firstName","lastName","email", "password","phone","adresse","ville","birth")
        #fields = '__all__'
    def clean_email(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        if '@gmail' in email:
            return email
        else :
            raise forms.ValidationError('this is not a valid email')
