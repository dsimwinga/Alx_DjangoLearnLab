from django.urls import path
from .views import list_books, LibraryDetailView
from .views import login_view, logout_view, register_view, list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view for listing books
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('books/', list_books, name='list_books'),
]
