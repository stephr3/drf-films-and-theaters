from rest_framework import serializers
from films.models import Film, Theater, Genre

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre')

class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'films')

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')
