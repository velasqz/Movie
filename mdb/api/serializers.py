from django.urls import reverse
from rest_framework import serializers

from mdb.models import MovieRate, Movie


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    release_date = serializers.DateField()
    duration = serializers.IntegerField()
    rate = serializers.SerializerMethodField(method_name='get_movie_rate')

    def get_movie_rate(self, obj):
        rates = MovieRate.objects.get_rate_for_movie(obj)
        if rates.exists():
            return rates.first()['rate']

        return ''


class MovieRateSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='drf-movierate-detail')
    user = serializers.StringRelatedField()
    movie = serializers.HyperlinkedRelatedField(read_only=True, view_name='drf-movie-detail', lookup_field='slug')

    class Meta:
        model = MovieRate
        fields = ('movie', 'user', 'rate', 'id')

class MovieRateSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model=MovieRate
        fields = ('movie','user','rate','comment')


class MovieRateSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model=MovieRate
        fields = ('movie','rate','comment')


class MovieRateSerializerDelete(serializers.ModelSerializer):

    class Meta:
        model = MovieRate
        field = ('id')


class MovieRateSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = MovieRate
        fields = '_all_'

class MovieSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(source='id')
    poster = serializers.ImageField(read_only=True)
    trailer_url = serializers.URLField(required=False)
    class Meta:
        model = Movie
        fields = (

            'title'
            'duration'
            'poster'
            'detail'
            'trailer_url'
            'genre'
            'original_language'
            'country'
            'release_date',
            'pk'
        )