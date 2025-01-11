from django.urls import path
from .views import *

urlpatterns = [
    path('api/movies/', MovieListAPI.as_view(), name='movies'),
]