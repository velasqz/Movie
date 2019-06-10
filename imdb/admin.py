from django.contrib import admin
from imdb.models import Movie, MovieRate

admin.site.register(Movie)
admin.site.register(MovieRate)