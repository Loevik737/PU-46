from django.shortcuts import render
from CheckPoint.apps.subject.models import Subject

# Create your views here.

def subjectView(request):

    all_subjects = Subject.objects.all()
    return render(request, 'subjectHome.html',)
