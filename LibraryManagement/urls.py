from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from books import views
from . import admin_dashboard


admin.site.site_header = "📚 Online Library Administration"
admin.site.site_title = "Online Library Admin"
admin.site.index_title = "Welcome to Online Library Admin Panel"


urlpatterns = [

    # Custom Admin Dashboard
    path(
        'admin/dashboard/',
        admin_dashboard.admin_dashboard,
        name='admin_dashboard'
    ),

    # Django Admin Panel
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # About
    path('about/', views.about, name='about'),

    # Books
    path('books/', views.book_list, name='book_list'),

    # Book Details
    path(
        'book/<int:pk>/',
        views.book_detail,
        name='book_detail'
    ),

    # Contact
    path('contact/', views.contact, name='contact'),

    # Orders
    path('orders/', include('orders.urls')),

    # Accounts
    path('accounts/', include('accounts.urls')),
    
    path('ai/', include('ai_chat.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )