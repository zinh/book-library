import uuid
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter a book genre(e.g. Science Fiction)")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief summary of the book")
    isbn = models.CharField("ISBN", max_length=13,
                            unique=True, help_text="13 characters")
    genre = models.ManyToManyField(
        'Genre', help_text="Select a genre for this book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()])

    display_genre.short_description = 'genre'


class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    language = models.ForeignKey(
        'Language', on_delete=models.RESTRICT, null=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default='m',
                              help_text="Book's availability")

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} {self.book.title}'


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
