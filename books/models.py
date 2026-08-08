from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
    source = models.CharField(max_length=150)
    total_pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(max_length=100, default="General")
    description = models.TextField(default="")

    photo = models.ImageField(upload_to="books/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name