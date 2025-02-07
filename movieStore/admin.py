from django.contrib import admin
from .models import Movie, Review

class MovieAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["movie_name"]}),
        ("Date information", {"fields": ["release_date"], "classes": ["collapse"]}),
    ]
    list_display = ["movie_name", "release_date", "was_released_recently"]
    list_filter = ["release_date"]
    search_fields = ["movie_name"]

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)