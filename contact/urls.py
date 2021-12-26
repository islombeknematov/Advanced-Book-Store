from django.urls import path

from contact.views import contact_create

app_name = 'contact'

urlpatterns = [
    # path('template/', ContactTemplateView.as_view(), name='contact_view'),
    # path('', ContactCreateView.as_view(), name='contact_create'),
    path('', contact_create, name='contact_create'),
]


