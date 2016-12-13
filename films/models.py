from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100)
    year_prod = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        'auth.User',
        related_name='films',
        on_delete=models.CASCADE,
        null=True
    )
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Theater(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    films = models.ManyToManyField(Film)

    class Meta:
        ordering = ('city',)
