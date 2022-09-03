from django.db import models
from datetime import datetime
# Create your models here.
from app1.models import Car


class Post(models.Model):
    title = models.CharField(max_length=120, help_text='title of message.')
    description = models.TextField(max_length=500, help_text=" write more informations about your car ...")
    time = models.DateTimeField(default=datetime.now)
    carToBePublished = models.ForeignKey(Car,verbose_name=("car"), on_delete=models.CASCADE)
    def __str__(self):
        return self.title

