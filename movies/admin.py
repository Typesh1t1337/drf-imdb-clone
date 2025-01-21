from django.contrib import admin

from movies.models import Movies,FavoriteMovies

admin.site.register(Movies)
admin.site.register(FavoriteMovies)

