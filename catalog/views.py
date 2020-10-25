from django.shortcuts import render, Http404
from django.views import generic

# Create your views here.
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context = context)
    

class BookListView(generic.ListView):
    model = Book
    # context_object_name = 'my_book_list'
    # queryset = Book.objects.filter(title__icontains = 'Harry')[0]
    template_name = 'books/my_arbitrary_template_name_list.html'


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk = primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
        
        return render(request, 'catalog/book_detail.html', context = {'book': book})
    

class AuthorListView(generic.ListView):
    model = Author
    # context_object_name = 'my_book_list'
    # template_name = 'authors/my_arbitrary_template_name_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author

    def book_detail_view(request, primary_key):
        try:
            book = Book.objects.get(pk = primary_key)
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
        
        return render(request, 'catalog/book_detail.html', context = {'book': book})