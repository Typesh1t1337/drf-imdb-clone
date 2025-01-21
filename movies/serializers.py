from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class AddToFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovies
        fields = ['movie']


class DeleteFromFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovies
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    class Meta:
        model = ReviewMovies
        fields = ['movie', 'user', 'review']

class ReviewDisplaySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    class Meta:
        model = ReviewMovies
        fields = '__all__'

class RetrieveUsersReviewSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(source='movie.title', read_only=True)
    class Meta:
        model = ReviewMovies
        fields = ['movie', 'user', 'review']
