from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
# Create your views here.

class homeView(TemplateView):
    template_name = 'home.html'




