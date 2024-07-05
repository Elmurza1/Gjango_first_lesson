from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField()
    size = models.IntegerField()
    prise = models.FloatField()


class Sushi(models.Model):
    name = models.CharField(max_length=100)

    consist = models.TextField()
    prise = models.IntegerField()
    is_spicy = models.BooleanField()


class Burger(models.Model):
    name = models.CharField(max_length=100)
    is_spicy = models.BooleanField()
    consist = models.TextField()
    prise = models.IntegerField()


class Drink(models.Model):
    name = models.CharField(max_length=222)

    price = models.IntegerField()
