from django.db import models


# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.ImageField()
