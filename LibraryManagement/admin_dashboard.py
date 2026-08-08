from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from books.models import Book
from orders.models import Order
from django.contrib.auth.models import User


@staff_member_required
def admin_dashboard(request):

    total_books = Book.objects.count()

    total_users = User.objects.count()

    total_orders = Order.objects.count()

    pending_orders = Order.objects.filter(
        status='Pending'
    ).count()

    processing_orders = Order.objects.filter(
        status='Processing'
    ).count()

    completed_orders = Order.objects.filter(
        status='Completed'
    ).count()

    cancelled_orders = Order.objects.filter(
        status='Cancelled'
    ).count()

    return render(request, 'admin/dashboard.html', {

        'total_books': total_books,

        'total_users': total_users,

        'total_orders': total_orders,

        'pending_orders': pending_orders,

        'processing_orders': processing_orders,

        'completed_orders': completed_orders,

        'cancelled_orders': cancelled_orders,

    })