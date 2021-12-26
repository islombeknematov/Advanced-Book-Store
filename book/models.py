from django.db import models
from django.utils.translation import gettext as _
from author.models import AuthorModel


class GenreModel(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')


class BookModel(models.Model):
    title = models.CharField(max_length=60, verbose_name=_('title'), null=True, blank=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.PROTECT, related_name='books', verbose_name=_('author'))
    genre = models.ManyToManyField(GenreModel, related_name='books', verbose_name=_('genre'))
    cover = models.ImageField(upload_to='media', verbose_name=_('cover'))
    isbn = models.CharField(max_length=13, unique=True, verbose_name='ISBN', null=True, blank=True)
    page_count = models.IntegerField(null=True, blank=True)
    summary = models.CharField(max_length=300, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')


