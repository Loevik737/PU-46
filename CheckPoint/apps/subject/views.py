from django.shortcuts import render
from CheckPoint.apps.subject.models import Subject
from CheckPoint.apps.plan.models import Plan

# Create your views here.

def subjectView(request):

    all_subjects = Subject.objects.all()
    plan = Plan.objects.all()
    args = { 'subjects': all_subjects, 'plan' : plan}
    #all_plans = Plan.objects.all()
    #context = {'plans' : all_plans }
    return render(request, 'subjectHome.html', args)