from films.models import Film
from films.serializers import FilmSerializer
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

# @api_view(['GET', 'POST'])
# def theater_list(request, format=None):
#     if request.method == 'GET':
#         theaters = Theater.objects.all()
#         serializedTheater = TheaterSerializer(theaters, many=True)
#         return Response(serializedTheater.data)
#     elif request.method == 'POST':
#         serializedTheater = TheaterSerializer(data=request.data)
#         if serializedTheater.is_valid():
#             serializedTheater.save()
#             return Response(serializedTheater.data, status=status.HTTP_201_CREATED)
#         return Response(serializedTheater.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def theater_detail(request, pk, format=None):
#     try:
#         theater = Theater.objects.get(pk=pk)
#     except Theater.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializedTheater = TheaterSerializer(theater)
#         return Response(serializedTheater.data)
#     elif request.method == 'PUT':
#         serializedTheater = TheaterSerializer(theater, data=request.data)
#         if serializedTheater.is_valid():
#             serializedTheater.save()
#             return Response(serializedTheater.data)
#         return Response(serializedTheater.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         theater.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# @api_view(['GET', 'POST'])
# def genre_list(request, format=None):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         serializedGenre = GenreSerializer(genres, many=True)
#         return Response(serializedGenre.data)
#     elif request.method == 'POST':
#         serializedGenre = GenreSerializer(data=request.data)
#         if serializedGenre.is_valid():
#             serializedGenre.save()
#             return Response(serializedGenre.data, status=status.HTTP_201_CREATED)
#         return Response(serializedGenre.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def genre_detail(request, pk, format=None):
#     try:
#         genre = Genre.objects.get(pk=pk)
#     except Genre.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializedGenre = GenreSerializer(genre)
#         return Response(serializedGenre.data)
#     elif request.method == 'PUT':
#         serializedGenre = GenreSerializer(genre, data=request.data)
#         if serializedGenre.is_valid():
#             serializedGenre.save()
#             return Response(serializedGenre.data)
#         return Response(serializedGenre.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         genre.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
