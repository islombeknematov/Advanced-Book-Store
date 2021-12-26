from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView, ListView

from book.models import BookModel, GenreModel


def index(request):
    return render(request, 'Main.html')


# def books(request):
#     allBooks = BookModel.objects.all()
#     context = {
#         'books': allBooks
#     }
#     return render(request, 'pages/books.html', context)


class BookListView(ListView):
    template_name = 'pages/books.html'

    def get_queryset(self):
        all_books = BookModel.objects.all()
        return all_books



def book_detail(request, pk):
    # try:
    #     book = BookModel.objects.get(pk=pk)
    # except BookModel.DoesNotExist:
    #     raise Http404
    #           |
    #           OR
    #           |
    book = get_object_or_404(BookModel, pk=pk)
    context = {'book_detail': book}
    return render(request, 'book_detail.html', context)



