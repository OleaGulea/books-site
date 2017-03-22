from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from books_site.books.models import Book
from books_site.books.forms import ChapterForm


def books_list(request):
    books = Book.objects.all()[:5]
    return render(request, '../templates/pages/home.html', {'books': books})


def books_list_editor(request):
    books = Book.objects.all()
    return render(request, '../templates/pages/books_list_editor.html', {'books': books})


def book_editor(request, book_id):
    book = Book.objects.get(pk=int(book_id))
    return render(request, '../templates/pages/book_editor.html', {'book': book})


# def chapter_editor(request, book_id, chapter_id):
#     book = Book.objects.get(pk=int(book_id))
#     chapter = book.chapters.get(pk=int(chapter_id))
#
#     chapter_form = ChapterForm()
#     return render(request, '../templates/pages/chapter_editor.html', {'book': book, 'chapter': chapter,
#                                                                    'form': chapter_form})


def chapter_editor(request, book_id, chapter_id=None):
    book = Book.objects.get(pk=int(book_id))
    if chapter_id is not None:
        chapter = book.chapters.get(pk=int(chapter_id))

        if request.method == 'POST':
            form = ChapterForm(request.POST, instance=chapter)
            if form.is_valid():
                chapter_form = form.save(commit=False)
                chapter_form.book = book
                chapter_form.save()
                messages.success(request, "Chapter was successfully updated!")
                return HttpResponseRedirect('/editor/' + book_id)
        else:
            form = ChapterForm(instance=chapter)
    else:
        if request.method == 'POST':
            form = ChapterForm(request.POST)
            if form.is_valid():
                chapter_form = form.save(commit=False)
                chapter_form.book = book
                chapter_form.save()
                messages.success(request, "New chapter was created!")
                return HttpResponseRedirect('/editor/' + book_id)

        else:
            form = ChapterForm()

    return render(request, '../templates/pages/chapter_editor.html', {'form': form})
