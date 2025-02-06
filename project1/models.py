from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Movie(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

