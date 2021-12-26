from django.contrib import admin

# Register your models here.
from book.models import BookModel
from contact.models import ContactModel


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'created']
    search_fields = ['title']








