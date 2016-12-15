from films.models import *
from films.serializers import *
from rest_framework.response import Response
from rest_framework import generics, permissions
from films.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
import pdb
import requests

@api_view(['GET'])
def film_title(request, format=None):
    """
    Get a list of films that have the word 'hunger' in the title
    """
    if request.method == 'GET':
        films = requests.get('http://www.omdbapi.com/?type=movie&s=hunger')
        json = films.json()
        a = []
        for key in json['Search']:
            films_dict = {}
            films_dict['title'] = key['Title']
            films_dict['year_prod'] = key['Year']
            a.append(films_dict)
        serializedFilm = FilmSerializer(a, many=True)
        return Response(serializedFilm.data)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    queryset = Film.objects.all()

    def get(self, request, *args, **kwargs):
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            films = Film.objects.filter(**filter_dict)
            serialized_films = FilmSerializer(films, many=True)
            return Response(serialized_films.data)
        else:
            return Response(FilmSerializer(Film.objects.all(), many=True).data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return FilmSerializer
        return FilmWriteSerializer

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return FilmSerializer
        return FilmWriteSerializer

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly)
    def get(self, request, *args, **kwargs):
        k = request.GET.keys()
        filter_dict = {}
        if(k):
            for key, value in request.GET.items():
                filter_dict[key] = value
            theaters = Theater.objects.filter(**filter_dict)
            serialized_theaters = TheaterSerializer(theaters, many=True)
            return Response(serialized_theaters.data)
        else:
            return Response(TheaterSerializer(Theater.objects.all(), many=True).data)

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return TheaterSerializer
        return TheaterWriteSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly)

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return TheaterSerializer
        return TheaterWriteSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return GenreSerializer
        return GenreWriteSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return GenreSerializer
        return GenreWriteSerializer
