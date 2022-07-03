from django.contrib import admin
from .models import Category, Genre, Movie, MovieShot, ActorAndDirector, Rating, RatingStar, Reviews


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShot)
admin.site.register(ActorAndDirector)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
