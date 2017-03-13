from django.shortcuts import render

# Create your views here.
from CheckPoint.apps.registration.forms import *
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import CostumUser

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            CostumUser.objects.create(
            user = user,
            role = form.cleaned_data['role']
            )

            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    return render(request,
        'registration/register.html',
                  {'form': form}
    )


def register_success(request):
    return render(request,
        'registration/registersuccess.html',
    )
