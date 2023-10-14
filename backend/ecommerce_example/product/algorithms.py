from .models import Book
from django.db.models import Q


def get_similar_books(pk):

    """Returns similar related and same author books for given book."""

    current_book = Book.objects.get(pk=pk)

    # Query and filter with related fields
    similar_books = Book.objects.filter(
        Q(name__icontains=current_book.name) | Q(category=current_book.category) |
        Q(genre__icontains=current_book.genre) | Q(author=current_book.author)
    ).exclude(pk=pk)

    # Filter same author books
    same_author = similar_books.filter(author=current_book.author)[:5]

    return similar_books[:5], same_author


def get_or_return_any(pk):

    """Gets a book from the database or returns default one
       having primary_key 1"""

    try:
        book = Book.objects.get(pk=pk)
    except:
        book = Book.objects.all()[0]

    return book