import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    rating_choices = [
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17')
    ]

    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)
    release_year = models.IntegerField('release date', default=datetime.date.today().year)
    rating = models.CharField(choices = rating_choices, default='PG', max_length=5)
    image = models.ImageField(upload_to='movie_images/', default='movie_images/default.jpg')
    description = models.TextField()
    dollar_price = models.DecimalField(max_digits=4, decimal_places=2, default=10.00)
   
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
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
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
        return str(self.id) + ' - ' + self.movie.movie_name;
