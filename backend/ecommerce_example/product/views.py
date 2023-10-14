from django.shortcuts import render
from .algorithms import get_similar_books, get_or_return_any


def home(request):

    """Default home view, it renders the book details with id 1 and with similar category
       books"""

    book = get_or_return_any(1)
    similar_books, same_author = get_similar_books(1)
    book_genre = book.genre.split(',')

    context = {
        'book': book,
        'similar_books': similar_books,
        'same_author': same_author,
        'book_genre': book_genre
    }
    return render(request, 'index.html', context)


def view_product(request, pk):

    """View to render given book using primary key.
       Also, it returns similar category and same
       author books as well."""

    book = get_or_return_any(pk)
    similar_books, same_author = get_similar_books(pk)
    book_genre = book.genre.split(',')

    context = {
        'book': book,
        'similar_books': similar_books,
        'same_author': same_author,
        'book_genre': book_genre
    }
    return render(request, 'index.html', context)


