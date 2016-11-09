from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)


class Film(models.Model):
    title = models.CharField(max_length=100)
    year_prod = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)

class Theater(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    films = models.ManyToManyField(Film)

    class Meta:
        ordering = ('city',)
