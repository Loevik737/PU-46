# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from CheckPoint.apps.subject.models import Subject
from CheckPoint.apps.registration.models import CustomUser
from CheckPoint.apps.plan.models import Plan
import json
import os

"""
This first bit takes in all the assignments from the ssubjects.json file with all subjects form NTNU's servers and
makes it a dict with the code for all the subjects as key and the name as value
"""
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, './static/json/subjects.json')
subjectDict = {}
with open(file_path) as json_data:
    d = json.load(json_data)
    for sub in d['emne']:
        temp = sub[0]['entityKeys'][0]['entityKeyId']
        temp = temp[13:len(temp)-2]
        subjectDict[temp] = ''.join(sub[0]['hasName'][0]['value']).encode('utf-8').strip()

"""
The subject view view returns the dictionary with subject so you can search them in the subjects template, and if
a user sends a post request with a subject it creates a subject object and adds it to attending.
It can also delete a subject from your teaching or attendign list
"""
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
        if 'delete_attending_subject' in request.POST:
            user.attendingSubject.remove(int(request.POST['delete_attending_pk']))
        if 'delete_teaching_subject' in request.POST:
            user.teachingSubject.remove(int(request.POST['delete_teaching_pk']))
        if 'subjectInfo' in request.POST:
            if ' ' in request.POST['subjectInfo']:
                subject_info = request.POST['subjectInfo'].split(' ',1)
                if subject_info[0] in subjectDict.keys():
                    subject = Subject.objects.get_or_create(code = subject_info[0],name=subject_info[1])
                    user.attendingSubject.add(subject[0].pk)
                    return HttpResponseRedirect('../home/')
                else:
                    args['invalid_subject'] = 1
            else:
                args['invalid_subject'] = 1

    #render subjectHome.html
    return render(request, 'subjectHome.html', args)
