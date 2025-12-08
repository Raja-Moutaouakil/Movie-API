from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Movie, Review
from .serializers import (
    MovieSerializer,
    ReviewSerializer,
    ReviewCreateSerializer,
    UserSerializer,
)
from .permissions import IsOwnerOrReadOnly, IsSelfOrAdmin

User = get_user_model()


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.select_related('movie', 'user').all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ['movie__title', 'content']
    ordering_fields = ['rating', 'created_at']
    filterset_fields = ['rating']

    def get_serializer_class(self):
        if self.action in ['create']:
            return ReviewCreateSerializer
        return ReviewSerializer

    def perform_create(self, serializer):
        user = getattr(self.request, 'user', None)
        serializer.save(user=user)


class MovieReviewsList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        movie_id = self.kwargs.get('movie_id')
        movie = get_object_or_404(Movie, pk=movie_id)
        return movie.reviews.select_related('user').all()


class ReviewsByTitleList(generics.ListAPIView):
    """List reviews filtered by movie title query param `title`."""
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie__title']
    ordering_fields = ['rating', 'created_at']

    def get_queryset(self):
        title = self.request.query_params.get('title')
        qs = Review.objects.select_related('movie', 'user').all()
        if title:
            qs = qs.filter(movie__title__icontains=title)
        return qs


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSelfOrAdmin]
