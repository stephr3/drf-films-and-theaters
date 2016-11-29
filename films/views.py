from films.models import *
from films.serializers import *
from rest_framework.response import Response
from rest_framework import generics
import pdb

class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def get(self, request, *args, **kwargs):
        first_letter = request.GET.get('first_letter', '')
        year_prod = request.GET.get('year_prod', '')
        if first_letter:
            if year_prod:
                films = Film.objects.filter(title__istartswith=first_letter).filter(year_prod=year_prod)
            else:
                films = Film.objects.filter(title__istartswith=first_letter)
        elif year_prod:
            films = Film.objects.filter(year_prod=year_prod)
        else:
            films = Film.objects.all()

        serialized_films = FilmSerializer(films, many=True)
        return Response(serialized_films.data)

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class TheaterList(generics.ListCreateAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class TheaterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
