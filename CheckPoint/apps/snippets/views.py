from django.http import HttpResponse
from models import User
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
    users_list = User.objects.all()
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    context_dict = {'users': users_list}
    # Render the response and send it back.
    return render_to_response('users/index.html', context_dict, context)
