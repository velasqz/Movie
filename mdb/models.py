from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse_lazy

from mdb.choices import THRILLER
from mdb.queryset import MovieRateQueryset
from .choices import MOVIE_GENRE


def movie_directory_path(instance, filename):
    return f'movie/{instance.title}/{filename}'


class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    poster = models.ImageField(upload_to=movie_directory_path)
    detail = models.TextField(null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)
    genre = models.CharField(max_length=25, choices=MOVIE_GENRE, default=THRILLER)
    original_language = models.CharField(max_length=2)
    country = models.CharField(max_length=200)
    release_date = models.DateField(null=True)
    slug = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('movie-detail', args=(self.title, ))

#    def save(self, force_insert=False, force_update=False, using=None,
#             update_fields=None):
#        self.slug = slugify(self.title)
#        super(Movie, self).save(force_insert=force_insert, force_update=force_update, using=using,
#                                update_fields=update_fields)


class MovieActor(models.Model):
    name = models.CharField(max_length=60)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class MovieDirector(models.Model):
    name = models.CharField(max_length=60)
    age = models.PositiveIntegerField()


class MovieRate(models.Model):
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.SET_NULL)

    objects = MovieRateQueryset.as_manager()

    class Meta:
        unique_together = ('user', 'movie')
        permissions = (
            ('can_vote_two_times', 'Can vote two times'),
        )

    def __str__(self):
        return f'{self.user} : {self.rate}'
