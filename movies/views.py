from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import *
from django.contrib.auth.models import User
from account.permissions import *

class PaginationMovie(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000

class MovieListAPI(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]
    pagination_class = PaginationMovie

class AddToFavoriteListAPI(generics.CreateAPIView):
    queryset = FavoriteMovies.objects.all()
    serializer_class = AddToFavoriteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if not "user" in serializer.validated_data:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

class FavoriteMovieListAPI(APIView):
    permission_classes = [IsAuthenticated,IsOwner]
    def get(self,request,username):
        user = User.objects.get(username=username)
        favorites = FavoriteMovies.objects.filter(user=user).select_related('movie')
        movies = [fav.movie for fav in favorites]
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class FavoriteDeleteMovieAPI(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,IsOwner]
    serializer_class = FavoriteMovies

    def delete(self,request,username,movie_id):
        user = User.objects.get(username=username)
        favorite = FavoriteMovies.objects.get(user=user, movie_id=movie_id)

        favorite.delete()
        return Response({
            'status': 'success',
        })



class MovieReviewsAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MovieReviewSerializer
    def post(self, request, movie_id):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                movie = serializer.validated_data['movie']
                review = serializer.validated_data['review']
                user = serializer.validated_data['user']


                user_objects = User.objects.get(username=user)

                movie_review = ReviewMovies.objects.create(movie=movie, user=user_objects, review=review)
                movie_review.save()
                return Response({
                    'status': 'success',
                })
            except Exception as e:
                return Response({
                    'status': f"error {str(e)}",
              })

        else:
            return Response({
                'status': 'serializer invalid',
            })



class ReviewDisplayView(APIView):
    permission_classes = [AllowAny]
    serializer_class = ReviewDisplaySerializer
    def get(self,request,movie_id):
        movies = ReviewMovies.objects.all().filter(movie_id=movie_id)
        serializer = MovieReviewSerializer(movies, many=True)
        return Response(
            serializer.data,
        )

class RetrieveUsersReviewView(APIView):
    permission_classes = [IsAuthenticated,IsOwner]
    serializer_class = RetrieveUsersReviewSerializer


    def get(self, request, username):
        user = request.user
        reviews = ReviewMovies.objects.all().filter(user=user)
        serializer = RetrieveUsersReviewSerializer(reviews, many=True)

        return Response(
            serializer.data,
        )
