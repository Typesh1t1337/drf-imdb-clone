from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

class MovieListAPI(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

