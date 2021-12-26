from django.contrib import admin

# Register your models here.
from author.models import AuthorModel
from book.models import GenreModel


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'birth_date', 'created']
    list_filter = ['created']
    search_fields = ['name']


@admin.register(GenreModel)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    search_fields = ['title']

