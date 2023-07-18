from django.db import models


# Create your models here.

class Book(models.Model):
    """
     Represents a book.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    # コメント
