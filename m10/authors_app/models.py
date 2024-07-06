from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Author(models.Model):
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255)
    born_location = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.fullname}"


class Tag(models.Model):
    name=models.CharField(max_length=255)


class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()
