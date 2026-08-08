from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from books.models import Book
from .forms import OrderForm
from .models import Order


def order_book(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    # User must be logged in to place an order
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":

        form = OrderForm(request.POST)

        if form.is_valid():

            order = form.save(commit=False)

            # Connect order with logged-in user
            order.user = request.user

            order.book = book

            order.save()

            messages.success(
                request,
                "✅ Order Placed Successfully! Thank you for your order. We will contact you soon."
            )

            return redirect('book_list')

    else:

        form = OrderForm()

    return render(request, 'orders/order_form.html', {
        'form': form,
        'book': book
    })


# My Orders
def my_orders(request):

    # User must be logged in
    if not request.user.is_authenticated:
        return redirect('login')

    # Show only the logged-in user's orders
    orders = Order.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(request, 'orders/my_orders.html', {
        'orders': orders
    })