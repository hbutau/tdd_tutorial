# from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

# def home(request):
#     return HttpResponse('<h1>Welcome to Addressbook</h1>')


class Home(TemplateView):
        template_name = 'home.html'
