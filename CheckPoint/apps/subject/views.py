from django.shortcuts import render
from CheckPoint.apps.subject.models import Subject
from CheckPoint.apps.plan.models import Plan

# Create your views here.

def subjectView(request):
    user = request.user.costumuser
    all_subjects = user.attendingSubject.all
    plan = Plan.objects.all()
    plansubject = {}
    for object in plan:
        plansubject[object.subject.name]=object.pk
    args = {'subjects': all_subjects, 'plan': plan, 'plansubject':plansubject, }
    #all_plans = Plan.objects.all()
    #context = {'plans' : all_plans }
    return render(request, 'subjectHome.html', args)
