from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):
    """create a class for our movie objects"""
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=360)

    def no_of_ratings(self):
        """let's get each rate for the movie and store it in an array"""
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        """get the average ratings for each movie"""
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        return 0

class Rating(models.Model):
    """create a class for our rating"""
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=
            [MinValueValidator(1), MaxValueValidator(5)]
        )
    class Meta:
        unique_together = (('user', 'movie'),)
        index_together = (('user', 'movie'),)
