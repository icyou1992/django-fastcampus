from django.db import models

# Create your models here.

class Shop(models.Model):
  name = models.CharField(max_length=20)
  address = models.CharField(max_length=40)

class Menu(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  food = models.CharField(max_length=20)

class Orders(models.Model):
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  date = models.DateTimeField('date ordered')
  address = models.CharField(max_length=40)
  estimated_time = models.IntegerField(default=-1)
  delivered = models.BooleanField(default=0)

class Order(models.Model):
  order = models.ForeignKey(Orders, on_delete=models.CASCADE)
  food = models.CharField(max_length=20)