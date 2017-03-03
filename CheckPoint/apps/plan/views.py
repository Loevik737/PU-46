from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Plan, Week, Lecture, Objectives
from CheckPoint.apps.subject.models import Subject
from .forms import CreatePlan, CreateLectureForm


def index(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    weeks = plan.weeks.all()
    lectures = plan.lectures.all()
    subject = plan.subject
    objectives = subject.learning_objectives.all()

    context = {
        'plan': plan,
        'weeks': weeks,
        'lectures': lectures,
        'subject': subject,
        'objectives': objectives,
        'create_lecture_form': CreateLectureForm(),
    }
    return render(request, 'plan/plan.html', context)

def create_plan(request):
    #the dictionary we will send to the html template
    context={}
    #if we get a POST request jump into the if statement
    if request.method == 'POST':
        #set for to the POST request we got
        form = CreatePlan(request.POST)
        #if the form was valid,save it and redirect us to the site for the new plan
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../'+ str(Plan.objects.latest('id').id))
    else:
        #if we dont get a POST request, send the form class with the dictionary to the template
        form = CreatePlan()
        context['form'] = form
    return render(request,'plan/createplan.html',context)


def create_lecture(request):
    if request.method == 'POST':
        plan_id = request.POST.get('plan_id', None)
        week_id = request.POST.get('week_id', None)
        plan = Plan.objects.get(id=plan_id)
        week = Week.objects.get(id=week_id)
        # if we get a POST request jump into the if statemen
        form = CreateLectureForm(request.POST)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.plan = plan
            lecture.week = week
            lecture.save_m2m()
            objectives = form.cleaned_data.pop('objectives_form_field').split(';')
            lecture_objectives = []
            for objective in objectives:
                lecture_objective, exists = Objectives.objects.get_or_create(learning_objective=objective, subject=plan.subject)
                lecture_objectives.append(lecture_objective)
            lecture.objectives = lecture_objectives
            lecture.save()