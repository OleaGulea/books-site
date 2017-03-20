from django.shortcuts import render

from books_site.books.models import Book


def books_list(request):
    books = Book.objects.all()[:5]
    return render(request, '../templates/pages/home.html', {'books': books})
