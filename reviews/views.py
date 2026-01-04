from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly


class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all().order_by("-created_at")
	serializer_class = MovieSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


class ReviewViewSet(viewsets.ModelViewSet):
	queryset = Review.objects.all().order_by("-created_at")
	serializer_class = ReviewSerializer
	permission_classes = [IsOwnerOrReadOnly | IsAuthenticatedOrReadOnly]

	def perform_create(self, serializer):
		# Attach user if authenticated; allow anonymous reviews as null user
		user = self.request.user if self.request and self.request.user and self.request.user.is_authenticated else None
		serializer.save(user=user)

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer


class MovieViewSet(viewsets.ModelViewSet):
	queryset = Movie.objects.all().order_by("-created_at")
	serializer_class = MovieSerializer
	permission_classes = [AllowAny]


class ReviewViewSet(viewsets.ModelViewSet):
	queryset = Review.objects.all().order_by("-created_at")
	serializer_class = ReviewSerializer
	permission_classes = [AllowAny]

