from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Customize the fields shown in the list view
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    list_filter = ('author', 'publication_year')  # Add filters by author and publication year
    search_fields = ('title', 'author')  # Enable searching by title and author

# Register the Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)