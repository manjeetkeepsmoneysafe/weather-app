from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class Data(models.Model):
    city = models.CharField(default="", max_length=1000)
    country = models.CharField(default="", max_length=1000)
    long = models.FloatField(default=0.00)
    lati = models.FloatField(default=0.00)

class Person(models.Model):
    email = models.EmailField(max_length=500, default="", primary_key=True)
    password = models.CharField(max_length=100, default="")
    plong = models.ManyToManyField(Data, related_name="person_longitude")
    plati = models.ManyToManyField(Data, related_name="person_latitude")

class HistoryData(models.Model):
    weatherInfo = models.JSONField(default=dict)
    date = models.DateTimeField(default=datetime.now)

class User(AbstractUser):
    data = models.ManyToManyField(HistoryData)