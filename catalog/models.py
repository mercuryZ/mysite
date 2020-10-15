from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    """
    Model representign a book (but not a specific copy of a book)
    """
    title = models.CharField(max_length = 200)
    author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
    summary =
    isbn =
    genre = 

    def __