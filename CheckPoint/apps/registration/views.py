from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from CheckPoint.apps.registration.models import CustomUser
from django.views.decorators.csrf import csrf_protect
from CheckPoint.apps.registration.forms import *

#Cross Site Request Forgery protection
@csrf_protect
#a view for registering
def register(request):
    #sends a post request when you press the register button
    if request.method == 'POST':
        #get the form from the post request
        form = RegistrationForm(request.POST)
        #check if fields in form are valid
        if form.is_valid():
            #create user with the form data
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            CustomUser.objects.create(
            user = user,
            role = form.cleaned_data['role']
            )
            #redirect to 'success' page
            return HttpResponseRedirect('/register/success/')
    else:
        #set form empty
        form = RegistrationForm()
    #render the register template
    return render(request,
        'registration/register.html',
                  {'form': form}
    )


def register_success(request):
    #render the registersuccess template
    return HttpResponseRedirect('../../login/'
    )
