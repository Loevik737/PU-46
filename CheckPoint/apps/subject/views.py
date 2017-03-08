from django.shortcuts import render

# Create your views here.

def subjectView(request):
    return render(request, 'subjectHome.html',)
