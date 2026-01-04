from django.db import models
from django.conf import settings


class Movie(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	release_date = models.DateField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class Review(models.Model):
	movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
	rating = models.IntegerField()
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Review {self.pk} for {self.movie}"

