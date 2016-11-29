from rest_framework import serializers
from films.models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'film_set')

class FilmSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(allow_null=True) #Returns a string instead of nested genres or keys

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre')

class FilmWriteSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True) #When you write, you don't have to write nested genre or genre string

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre')

class TheaterSerializer(serializers.ModelSerializer):
    films = FilmSerializer(many=True) # nest a list of films
# make with primary keys
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'films')
