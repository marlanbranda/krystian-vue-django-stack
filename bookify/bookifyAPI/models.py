from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class BookToRate(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def quantity_ratings(self):
        return Rating.objects.filter(book=self).count()
    
    def average_rating(self):
        ratings_stars = [rating.stars for rating in Rating.objects.filter(book=self)]
        if len(ratings_stars) == 0:
            return 0
        else:
            return sum(ratings_stars) / len(ratings_stars)

    def __str__(self):
        return self.title


class Rating(models.Model):
    book = models.ForeignKey(BookToRate, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'book'))
        index_together = (('user', 'book'))
