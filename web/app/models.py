from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    
    @property
    def all_books(self):
        books_string = ''
        for book in self.books.all():
            books_string += f"{book.title}, "
        return books_string

    def __str__(self) -> str:
        return self.name 

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self) -> str:
        return self.title


# Author.objects.all().values('name').annotate(books=Count('books')).order_by('name')
# Author.objects.annotate(total_books=Count('books'))
# Author.objects.annotate(Count('books'))  books__count
