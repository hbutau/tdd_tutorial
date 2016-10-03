# from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from contacts.models import Contact
from django.core.urlresolvers import reverse
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('<h1>Welcome to Addressbook</h1>')
# class Home(TemplateView):

#     template_name = 'home.html'

#     # def get(self, request, *args, **kwargs):
#         # return HttpResponse('<title>AdressBook</title>')

# class CreateContactView(CreateView):

#         model = Contact
#         template_name = 'edit_contact.html'
#         fields = ("first_name", "email", "last_name",)

#         def get_success_url(self):
#             return reverse('home_page')
