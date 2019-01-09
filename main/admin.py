from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    #fields = ('name', 'description', 'year', 'released', 'imdb_rating')
    list_display = ('name', 'description', 'year', 'released', 'imdb_rating')
