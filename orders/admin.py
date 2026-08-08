from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'customer_name',
        'book',
        'mobile',
        'status',
        'order_date',
    )

    list_filter = (
        'status',
        'order_date',
    )

    search_fields = (
        'customer_name',
        'mobile',
        'book__book_name',
    )

    list_editable = (
        'status',
    )

    ordering = (
        '-order_date',
    )