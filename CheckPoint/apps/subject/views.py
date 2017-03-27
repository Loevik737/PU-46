from django.shortcuts import render
from CheckPoint.apps.subject.models import Subject
from CheckPoint.apps.registration.models import CustomUser
from CheckPoint.apps.plan.models import Plan

# Create your views here.

def subjectView(request):
    #get costumuser
    user =request.user.customuser
    #get subjects the user attends
    all_attending_subjects = user.attendingSubject.all

    #get all plan objects
    plan = Plan.objects.all()
    #make dictionary where key is subjectname in plan and value is planID
    plansubject = {}
    for object in plan:
        plansubject[object.subject.name]=object.pk
    #make user subjects, plan objects and plansubject dictionary usable from template
    args = {'subjects': all_attending_subjects,'plan': plan, 'plansubject':plansubject, }
    if user.role == 'Teacher':
        args['teaching_subjects'] =  user.teachingSubject.all
    #render subjectHome.html
    return render(request, 'subjectHome.html', args)
