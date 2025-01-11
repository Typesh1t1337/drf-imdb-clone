from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    filters = models.TextField()
    key_words = models.TextField()
    photo_url = models.TextField()
    rating = models.IntegerField()

