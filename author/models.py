from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class AuthorModel(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
