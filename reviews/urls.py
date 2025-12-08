from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('movies', views.MovieViewSet, basename='movie')
router.register('reviews', views.ReviewViewSet, basename='review')
router.register('users', views.UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:movie_id>/reviews/', views.MovieReviewsList.as_view(), name='movie-reviews'),
    path('reviews-by-title/', views.ReviewsByTitleList.as_view(), name='reviews-by-title'),
]
