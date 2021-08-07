from django.db import models
from isbn_field import ISBNField


# Create your models here.


class Book(models.Model):
    isbn = ISBNField()
    name = models.CharField(max_length=50, null=False, blank=False)
    author = models.CharField(max_length=50, null=False, blank=False)
    publish_year = models.IntegerField(null=False, blank=False, default=1000)
    edition = models.IntegerField(null=True, blank=True, default=1)
    genre = models.CharField(max_length=50, null=False, blank=False)
    origin = models.CharField(max_length=100, null=False, blank=False)


    def __str__(self):
        return self.name
