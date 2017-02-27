from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Plan, Week, Lecture, Objectives
from CheckPoint.apps.subject.models import Subject


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

    }
    return render(request, 'plan/plan.html', context)

#weeks = plans.weeks.all()
#    lectures = plans.weeks.lecturs.all()
#    user = request.user
#'week': weeks,
#        'lectures': lectures,*/