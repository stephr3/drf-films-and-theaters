from rest_framework import serializers
from films.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    films = serializers.PrimaryKeyRelatedField(many=True, queryset=Film.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'films')

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
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set', 'owner')
        depth = 1

class FilmWriteSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), allow_null=True)

    class Meta:
        model = Film
        fields = ('id', 'title', 'year_prod', 'genre', 'theater_set')

class TheaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theater
        fields = ('id', 'name', 'city', 'films')
        depth = 1

class TheaterWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Theater
        fields = ('id', 'name', 'city')
