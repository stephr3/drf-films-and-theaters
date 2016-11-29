from films.models import *
from films.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class FilmList(APIView):
    """
    List all films, or create a new film.
    """
    def get(self, request, format=None):
        films = Film.objects.all()
        serialized_films = FilmSerializer(films, many=True)
        return Response(serialized_films.data)

    def post(self, request, format=None):
        film = FilmSerializer(data=request.data)
        if film.is_valid():
            film.save()
            return Response(film.data, status=status.HTTP_201_CREATED)
        return Response(film.errors, status=status.HTTP_400_BAD_REQUEST)


class FilmDetail(APIView):
    """
    Retrieve, update or delete a film instance.
    """
    def get_object(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except Film.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        film = self.get_object(pk)
        serialized_film = FilmSerializer(film)
        return Response(serialized_film.data)

    def put(self, request, pk, format=None):
        film = self.get_object(pk)
        serialized_film = FilmSerializer(film, data=request.data)
        if serialized_film.is_valid():
            serialized_film.save()
            return Response(serialized_film.data)
        return Response(serialized_film.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        film = self.get_object(pk)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TheaterList(APIView):
    def get(self, request, format=None):
        theaters = Theater.objects.all()
        serialized_theaters = TheaterSerializer(theaters, many=True)
        return Response(serialized_theaters.data)

    def post(self, request, format=None):
        theater = TheaterSerializer(data=request.data)
        if theater.is_valid():
            theater.save()
            return Response(theater.data, status=status.HTTP_201_CREATED)
        return Response(theater.errors, status=status.HTTP_400_BAD_REQUEST)

class TheaterDetail(APIView):
    """
    Retrieve, update or delete a film instance.
    """
    def get_object(self, pk):
        try:
            return Theater.objects.get(pk=pk)
        except Theater.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        theater = self.get_object(pk)
        serialized_theater = TheaterSerializer(theater)
        return Response(serialized_theater.data)

    def put(self, request, pk, format=None):
        theater = self.get_object(pk)
        serialized_theater = TheaterSerializer(theater, data=request.data)
        if serialized_theater.is_valid():
            serialized_theater.save()
            return Response(serialized_theater.data)
        return Response(serialized_theater.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        theater = self.get_object(pk)
        theater.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GenreList(APIView):
    """
    List all films, or create a new film.
    """
    def get(self, request, format=None):
        genres = Genre.objects.all()
        serialized_genres = GenreSerializer(genres, many=True)
        return Response(serialized_genres.data)

    def post(self, request, format=None):
        genre = GenreSerializer(data=request.data)
        if genre.is_valid():
            genre.save()
            return Response(genre.data, status=status.HTTP_201_CREATED)
        return Response(genre.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetail(APIView):
    """
    Retrieve, update or delete a genre instance.
    """
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        genre = self.get_object(pk)
        serialized_genre = GenreSerializer(genre)
        return Response(serialized_genre.data)

    def put(self, request, pk, format=None):
        genre = self.get_object(pk)
        serialized_genre = GenreSerializer(genre, data=request.data)
        if serialized_genre.is_valid():
            serialized_genre.save()
            return Response(serialized_genre.data)
        return Response(serialized_genre.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
