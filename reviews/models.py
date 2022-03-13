from django.db import models
from django.contrib.auth.models import User

from products.models import Product

# Create your models here.


class Review(models.Model):

    rating_options = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        null=True, blank=True, default=1, choices=rating_options)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    review_date = models.DateTimeField(
        null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return self.title
