from django.contrib import admin
from .models import Movie, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "release_date", "created_at")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ("id", "movie", "user", "rating", "created_at")

