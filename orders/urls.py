from django.urls import path
from . import views


urlpatterns = [
    path('buy/<int:book_id>/', views.order_book, name='order_book'),

    path('my-orders/', views.my_orders, name='my_orders'),
]