from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# Секој автомобил се карактеризира со задолжителни податоци како производител, цена, број на шасија, модел, боја,
# година на производство, километража, тип на автомобил (sedan, SUV, hatchback, coupe), негова фотографија.
# За производителот се чуваат неговото име, локација, корисник кој го додал, година на основање и бројот на вработени.

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.IntegerField()
    number_employees = models.IntegerField()
    def __str__(self):
        return self.name


class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('hatchback', 'Hatchback'),
        ('coupe', 'Coupe'),
    ]
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.FloatField()
    chassis = models.IntegerField()
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    year = models.IntegerField()
    kilometers = models.IntegerField()
    type = models.CharField(max_length=50, choices=CAR_TYPE_CHOICES)
    photo = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.model
