from orders.models import Order
from django.shortcuts import render, get_object_or_404
from .models import Book


def home(request):

    latest_books = Book.objects.all().order_by('-created_at')[:6]

    total_books = Book.objects.count()

    total_orders = Order.objects.count()

    happy_readers = Order.objects.values('customer_name').distinct().count()

    return render(request, 'home/home.html', {
        'latest_books': latest_books,
        'total_books': total_books,
        'total_orders': total_orders,
        'happy_readers': happy_readers,
    })


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def book_list(request):

    query = request.GET.get('search')
    category = request.GET.get('category')

    books = Book.objects.all().order_by('-created_at')

    if query:
        books = books.filter(
            book_name__icontains=query
        ) | books.filter(
            author__icontains=query
        ) | books.filter(
            publisher__icontains=query
        )

    if category:
        books = books.filter(category=category)


    categories = Book.objects.values_list(
        'category',
        flat=True
    ).distinct()


    return render(request, 'books/book_list.html', {

        'books': books,
        'query': query,
        'categories': categories,

    })


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, 'books/book_detail.html', {
        'book': book
    })