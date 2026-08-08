from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Order(models.Model):

    STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='orders'
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    customer_name = models.CharField(
        max_length=100
    )

    mobile = models.CharField(
        max_length=20
    )

    address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    order_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.customer_name} - {self.book.book_name}"