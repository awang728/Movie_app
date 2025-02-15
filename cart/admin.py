from django.contrib import admin
from movieStore.models import Movie


# Register your models here.
from .models import Item, Order
admin.site.register(Order)
admin.site.register(Item)

