from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "book_name",
        "author",
        "publisher",
        "category",
        "price",
        "created_at",
    )

    search_fields = (
        "book_name",
        "author",
        "publisher",
        "category",
    )

    list_filter = (
        "category",
        "publisher",
    )

    ordering = ("-created_at",)