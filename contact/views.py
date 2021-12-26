from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from contact.forms import ContactModelForm
from contact.models import ContactModel


# class ContactTemplateView(TemplateView):
#     template_name = 'contact.html'


# class ContactCreateView(CreateView):
#     template_name = 'contact.html'
#     form_class = ContactModelForm
#
#     def get_success_url(self):
#         return reverse('contact:contact_create')


#                       FBV

def contact_create(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form Submitted Successfully')
        return redirect('/contact/')
    else:
        form = ContactModelForm()
    context = {
        'form': form
    }

    return render(request, 'contact.html', context)


# ------------------------------------------------------


# class ContactUpdateView(UpdateView):
#     template_name = 'form.html'
#     form_class = ContactModelForm
#     model = ContactModel
#     success_url = '/contact/'

#                   FBV

# def contact_update(request, pk):
#     contact = get_object_or_404(ContactModel, pk=pk)
#
#     if request.method == 'POST':
#         form = ContactModelForm(request.POST, instance=contact)
#         if form.is_valid():
#             form.save()
#         return redirect('/contact/')
#     else:
#         form = ContactModelForm(instance=contact)
#
#         context = {
#             'form': form
#         }
#
#         return render(request, 'form.html', context)


# ---------------------------------------------------------------



