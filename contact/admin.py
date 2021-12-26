from django.contrib import admin
from contact.models import ContactModel
# Register your models here.


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone', 'created']
    list_filter = ['created']
    search_fields = ['name']


