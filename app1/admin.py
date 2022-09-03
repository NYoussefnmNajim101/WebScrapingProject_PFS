from django.contrib import admin

from concesApp.models import Post
from .models import Client,Concessionnaire,Car
# Register your models here.
admin.site.register(Client)
admin.site.register(Concessionnaire)
admin.site.register(Car)
