from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response,render
from forms import UpdateUser

#a default index view
def index(request):
    return HttpResponse("Hello, world. You're at the snippets index.")

#a view that shows the user info and form for editing
def user_info(request):
    #if the user clicks the submit button a POST request is sent
    if request.method == 'POST':
        #user is the user you are loged in with
        user = request.user
        #get the fom from the post request
        form = UpdateUser(request.POST)
        #if the form is valid go into the if statement
        if form.is_valid():
            #set user.username to the post we got
            user.username = request.POST['username']
            #set user.email to the post we got
            user.email = request.POST['email']
            #save teh user
            user.save()
            #rederect to the same page but now with updated info
            return HttpResponseRedirect('../users')
    else:
        #the form is the form class from forms.spy
        form = UpdateUser()
    args = {}
    args['form'] = form
    return render(request, 'users/user.html', args)
