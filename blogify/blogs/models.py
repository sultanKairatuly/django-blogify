from django.db import models

# Create your models here.
class Movie (models.Model):
        title = models.CharField(max_length = 100)
        image = models.CharField(max_length = 200)
        rate = models.FloatField()
        description = models.TextField()
        director = models.CharField(max_length = 50)
        year = models.IntegerField()
        actors = models.TextField()
        genres = models.TextField()