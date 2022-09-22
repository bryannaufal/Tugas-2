from django.db import models

class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField()
    release_date = models.TextField()
    rating = models.IntegerField()
    review = models.CharField(max_length=255)
