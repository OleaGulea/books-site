from django.contrib import admin

from books_site.books.models import Book, Chapter, Author

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Author)
