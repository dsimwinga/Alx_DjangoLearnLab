user@USERs-MacBook-Pro LibraryProject % python3 manage.py shell
Python 3.13.2 (v3.13.2:4f8bb3947cf, Feb  4 2025, 11:51:10) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book.save()
>>> print(book)
1984 by George Orwell (1949)
>>> book = Book.objects.get(title="Animal Farm")
>>> print(book.title, book.author, book.publication_year)
1984 George Orwell 1949
>>> book.title="Nineteen Eight-Four"
>>> book.save()
>>> print(book)
Nineteen Eight-Four by George Orwell (1949)
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> print(book)
Nineteen Eight-Four by George Orwell (1949)
book.delete()
(1, {'bookshelf.Book': 1})
>>> print(Book.objects.all())
<QuerySet []>
>>> 