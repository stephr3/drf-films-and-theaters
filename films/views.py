from films.models import *
from films.serializers import *
from rest_framework.response import Response
from rest_framework import generics
import pdb

class FilmList(generics.ListCreateAPIView):
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

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return FilmSerializer
        return FilmWriteSerializer

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()

    def get_serializer_class(self):
        if(self.request.method == 'GET'):
            return FilmSerializer
        return FilmWriteSerializer

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

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

class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

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
