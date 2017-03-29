# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from CheckPoint.apps.subject.models import Subject
from CheckPoint.apps.registration.models import CustomUser
from CheckPoint.apps.plan.models import Plan
import json
import os

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, './static/json/subjects.json')
subjectDict = {}
with open(file_path) as json_data:
    d = json.load(json_data)
    for sub in d['emne']:
        temp = sub[0]['entityKeys'][0]['entityKeyId']
        temp = temp[13:len(temp)-2]
        subjectDict[temp] = ''.join(sub[0]['hasName'][0]['value']).encode('utf-8').strip()

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
    args["subjectDict"] = subjectDict
    if request.method == 'POST':
        if 'subjectInfo' in request.POST:
            subject_info = request.POST['subjectInfo'].split(' ')
            subject = Subject.objects.get_or_create(code = subject_info[0],name=subject_info[1])
            user.attendingSubject.add(subject[0].pk)
            return HttpResponseRedirect('../subjects/')


    #render subjectHome.html
    return render(request, 'subjectHome.html', args)
