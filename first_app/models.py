from django.db import models
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime,date
from datetime import datetime


# Create your models here.
class Diabetics(models.Model):
    name = models.CharField(max_length=254)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
    
class Otc(models.Model):
    name = models.CharField(max_length=254)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
    
class BabyCare(models.Model):
    name = models.CharField(max_length=254)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
    
class WomenChoice(models.Model):
    name = models.CharField(max_length=254)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
    
class PersonalCare(models.Model):
    name = models.CharField(max_length=254)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)

class SWellness(models.Model):
    name = models.CharField(max_length=254)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)

class Cart (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Diabetics,on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)


class CheckOut(models.Model):
    name = models.CharField(max_length=254)
    cardnumber = models.IntegerField()
    expiration = models.CharField(max_length=400)
    cvv = models.IntegerField()
    number = models.IntegerField()
    def __str__(self):
        return self.name + '-' +str(self.cardnumber) + ' - '+  self.expiration + ' - ' +str(self.cvv) + ' - ' + str(self.number)
 
    
