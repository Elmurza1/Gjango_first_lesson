from django.contrib import admin
from .models import Pizza, Sushi, Burger, Drink
# Register your models here.

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Sushi)
class SushiAdmin(admin.ModelAdmin):
    list_display = ['name', 'prise']

@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ['name']
