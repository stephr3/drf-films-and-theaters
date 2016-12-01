from rest_framework import serializers
from films.models import *

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'film_set')
        depth = 1

class GenreWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'name', 'film_set')

class FilmSerializer(serializers.ModelSerializer):
    # genre = GenreSerializer()

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set')
        depth = 1

class FilmWriteSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set')

class TheaterSerializer(serializers.ModelSerializer):
#     films = FilmSerializer(many=True) # nest a list of films
# # make with primary keys
    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'films')
        depth = 1

class TheaterWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theater
        fields = ('id', 'name', 'city')
