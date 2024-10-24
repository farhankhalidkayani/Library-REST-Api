from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    publication_year = models.DateField()
    availability_status = models.BooleanField()
