from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def movie_count(self):
        return len(self.movies.all())


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.title
    def rating(self):
        list_ = [review.stars for review in self.reviews.all()]
        return sum(list_) / len(list_) if len(list_) != 0 else "No reviews"

STARS = (
    (1, '*'),
    (2, '* *'),
    (3, '* * *'),
    (4, '* * * *'),
    (5, '* * * * *')
)
class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=0, choices=STARS)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    def __str__(self):
        return self.text

    def stars_str(self):
        return self.stars * '* '

