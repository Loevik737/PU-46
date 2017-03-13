from django.shortcuts import render
from CheckPoint.apps.subject.models import Subject
from CheckPoint.apps.plan.models import Plan

# Create your views here.

def subjectView(request):

    all_subjects = Subject.objects.all()
    args = { 'subjects': all_subjects}
    all_plans= Plan.objects.all()
    context = {'plan' : all_plans}
    return render(request, 'subjectHome.html', args, context)