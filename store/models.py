from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    description = models.TextField()
    publish_date = models.DateField(default = timezone.now)
    price = models.DecimalField(decimal_places=3, max_digits=8)
    stock = models.IntegerField(default=0)