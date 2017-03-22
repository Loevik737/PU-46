from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import loader
# Create your views here.

#def index(request):
 #   return render(request, 'myApp/login.html', {})

def login_success(request):
    return HttpResponseRedirect('home/')
