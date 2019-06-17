from django.urls import reverse
from rest_framework import serializers

from mdb.models import MovieRate


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    release_date = serializers.DateField(input_formats=['%d/%m/%Y'])
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