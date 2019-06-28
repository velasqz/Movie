from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse_lazy
from mdb.queryset import MovieRateQueryset
from .choices import movie_genre
import uuid


def movie_directory_path(instance, filename):
    return f'movie/{instance.title}/{filename}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    poster = models.ImageField(upload_to=movie_directory_path)
    detail = models.TextField(null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)
    genre = models.CharField(max_length=25, choices=movie_genre)
    original_language = models.CharField(max_length=2)
    relase_date = models.DateField(null=True)
    country = models.ForeignKey('country', null=True,  on_delete=models.SET_NULL)
    directors = models.ManyToManyField('MovieDirector')
    actors =  models.ManyToManyField('MovieActor')
    release_date = models.DateField(null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('movie-detail', args=(self.title, ))


class MovieRate(models.Model):
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    movie = models.ForeignKey('Movie', null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)
    comment = models.TextField(null=False, max_length=150)

    objects = MovieRateQueryset.as_manager()

    def __str__(self):
        return 'Movie: {}'.format(self.movie.title)


class MovieActor(models.Model):
    name = models.CharField(max_length=60, unique=True, null=False)
    age = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name


class MovieDirector(models.Model):
    name = models.CharField(max_length=60, unique=True, null=False)
    age = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)

    def __str__(self):
        return self.name

class UserToken(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    token = models.UUIDField(default=uuid.uuid4)