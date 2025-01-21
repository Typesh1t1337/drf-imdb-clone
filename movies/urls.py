from django.urls import path
from .views import *

urlpatterns = [
    path('api/movies/', MovieListAPI.as_view(), name='movies'),
    path('api/add/watchlist/',AddToFavoriteListAPI.as_view(), name='add-to-favorite-list'),
    path('api/watchlist/<str:username>/',FavoriteMovieListAPI.as_view(), name='favorite-movies'),
    path('api/remove/watchlist/<str:username>/<int:movie_id>/',FavoriteDeleteMovieAPI.as_view(),name='remove-favorite-movie'),
    path('api/movies/review/<int:movie_id>/', MovieReviewsAPI.as_view(), name='review-movies'),
    path('api/movies/display/<int:movie_id>/',ReviewDisplayView.as_view()),
    path('api/users/review/<str:username>/',RetrieveUsersReviewView.as_view(), name='review-users'),
]