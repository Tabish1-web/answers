from django.shortcuts import render
from .models import Book, Author
from django.db.models import Count

def Books(request):
    books = Book.objects.all()
    context = { "books" : books }
    return render(request, "books.html", context)

def Authors(request):
    authors = Author.objects.all()
    context = { "authors" : authors }
    return render(request, "authors.html", context)

def AuthorTotalBooks(request):
    authors = Author.objects.annotate(total_books=Count('books'))
    context = { "authors" : authors }
    return render(request, "authorbooks.html", context)