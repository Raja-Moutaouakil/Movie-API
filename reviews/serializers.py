from rest_framework import serializers
from .models import Movie, Review


class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ["id", "title", "description", "release_date", "created_at"]


class ReviewSerializer(serializers.ModelSerializer):
	movie_title = serializers.CharField(source="movie.title", read_only=True)

	class Meta:
		model = Review
		fields = ["id", "movie", "movie_title", "user", "rating", "content", "created_at"]
		read_only_fields = ["user", "created_at"]

