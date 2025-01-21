from django.contrib.auth.models import User
from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    filters = models.TextField()
    key_words = models.TextField()
    photo_url = models.TextField()
    rating = models.IntegerField()


class FavoriteMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.OneToOneField(Movies, on_delete=models.CASCADE, related_name='favorites')

class ReviewMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()


