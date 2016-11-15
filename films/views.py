from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from films.models import *
from films.serializers import *


@api_view(['GET', 'POST'])
def film_list(request, format=None):
    """
    List all snippets, or create a new film.
    """
    if request.method == 'GET':
        films = Film.objects.all()
        serializedFilm = FilmSerializer(films, many=True)
        return Response(serializedFilm.data)

    elif request.method == 'POST':
        serializedFilm = FilmWriteSerializer(data=request.data)
        if serializedFilm.is_valid():
            serializedFilm.save()
            return Response(serializedFilm.data, status=status.HTTP_201_CREATED)
        return Response(serializedFilm.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def film_detail(request, pk, format=None):
    """
    Retrieve, update or delete a film instance.
    """
    try:
        film = Film.objects.get(pk=pk)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedFilm = FilmSerializer(film)
        return Response(serializedFilm.data)

    elif request.method == 'PUT':
        serializedFilm = FilmWriteSerializer(film, data=request.data)
        if serializedFilm.is_valid():
            serializedFilm.save()
            return Response(serializedFilm.data)
        return Response(serializedFilm.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def theater_list(request, format=None):
    if request.method == 'GET':
        theaters = Theater.objects.all()
        serializedTheater = TheaterSerializer(theaters, many=True)
        return Response(serializedTheater.data)
    elif request.method == 'POST':
        serializedTheater = TheaterSerializer(data=request.data)
        if serializedTheater.is_valid():
            serializedTheater.save()
            return Response(serializedTheater.data, status=status.HTTP_201_CREATED)
        return Response(serializedTheater.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def theater_detail(request, pk, format=None):
    try:
        theater = Theater.objects.get(pk=pk)
    except Theater.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedTheater = TheaterSerializer(theater)
        return Response(serializedTheater.data)
    elif request.method == 'PUT':
        serializedTheater = TheaterSerializer(theater, data=request.data)
        if serializedTheater.is_valid():
            serializedTheater.save()
            return Response(serializedTheater.data)
        return Response(serializedTheater.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        theater.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def genre_list(request, format=None):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializedGenre = GenreSerializer(genres, many=True)
        return Response(serializedGenre.data)
    elif request.method == 'POST':
        serializedGenre = GenreSerializer(data=request.data)
        if serializedGenre.is_valid():
            serializedGenre.save()
            return Response(serializedGenre.data, status=status.HTTP_201_CREATED)
        return Response(serializedGenre.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk, format=None):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializedGenre = GenreSerializer(genre)
        return Response(serializedGenre.data)
    elif request.method == 'PUT':
        serializedGenre = GenreSerializer(genre, data=request.data)
        if serializedGenre.is_valid():
            serializedGenre.save()
            return Response(serializedGenre.data)
        return Response(serializedGenre.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
