from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author

# Create your views here.


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(
        status__exact='a').count()
    num_authors = Author.objects.all().count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_instance_available': num_instance_available
    }
    return render(request, 'index.html', context)


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book
