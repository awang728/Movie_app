import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    release_date = models.DateField('release date')
    def __str__(self):
        return self.movie_name

    @admin.display(
        boolean=True,
        ordering='release_date',
        description="Recent release?"
    )
    def was_released_recently(self):
        now = timezone.now().date()
        return now - datetime.timedelta(days=365) <= self.release_date

class Movie(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
