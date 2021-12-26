from django.urls import path

from book.views import index, BookListView, book_detail

app_name = 'book'

urlpatterns = [
    path('', index, name='my_book'),
    # path('books/', books, name='book_page'),
    path('books/', BookListView.as_view(), name='book_page'),

    path('bookdetail/', book_detail, name='book_detail'),

]