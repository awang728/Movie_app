import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    release_date = models.DateField('release date')
    price = models.IntegerField(default=0)
    description = models.TextField(default='Not currently Available.')
    image = models.ImageField(upload_to='movie_images/', default='movie_images/default.jpg')
   
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

class Cart(models.Model):
    userName = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie,
                              on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.movie.name
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total_price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User,
        on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username
