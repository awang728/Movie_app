import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

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