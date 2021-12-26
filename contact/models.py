from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class ContactModel(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('name'))
    surname = models.CharField(max_length=20, verbose_name=_('surname'))
    phone = models.CharField(max_length=13, verbose_name=_('phone'))
    message = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    email = models.EmailField(verbose_name=_('email'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

