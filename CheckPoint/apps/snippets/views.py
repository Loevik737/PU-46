from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response

#a default index view
def index(request):
    return HttpResponse("Hello, world. You're at the snippets index.")
#a view that shows the users in the database
def show_users(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    # Query the database for a list of ALL users currently stored.
    if request.user.is_authenticated:
        context_dict = {'user': request.user}
    else:
        context_dict = {'user': 'you are not authenticated'}
    # Place the list in our context_dict dictionary which will be passed to the template engine.

    # Render the response and send it back.
    return render_to_response('users/user.html', context_dict, context)
