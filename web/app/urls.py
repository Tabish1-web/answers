from unicodedata import name
from django.urls import path
from .views import Books, Authors, AuthorTotalBooks

urlpatterns = [
    path("books/", Books, name="books"),
    path("authors/", Authors, name="authors"),
    path("authorbooks/", AuthorTotalBooks, name="authorbooks")
]