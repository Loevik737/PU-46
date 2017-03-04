from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Assignment, MultipleChoiseQuestion, TrueFalseQuestion, OneWordQuestion
from CheckPoint.apps.subject.models import Subject
from forms import CreateAssignment,CreateMultipleChoiseQuestion,CreateTrueFalseQuestion,CreateOneWordQuestion
import six

def index(request, assignment_id):
    #when we get the id of the assingement from url, we look up if there is an object in the
    #database who has that id
    assignment = Assignment.objects.get(id=assignment_id)
    multipleChoiseQuestions = assignment.MultipleChoiseQuestions.all()
    trueFalseQuestions = assignment.TrueFalseQuestions.all()
    oneWordQuestions = assignment.OneWordQuestions.all()
    #all the questions that are connectet to the assingement gets sent off with
    #the dictionary to the assingement.html page
    context = {
        'assignment': assignment,
        'multipleChoiseQuestions': multipleChoiseQuestions,
        'trueFalseQuestions': trueFalseQuestions,
        'oneWordQuestions': oneWordQuestions,

    }
    return render(request, 'view/assignment.html', context)

def create_assignment(request):
    #the dictionary we will send to the html template
    context={}
    #if we get a POST request jump into the if statement
    if request.method == 'POST':
        #set for to the POST request we got
        form = CreateAssignment(request.POST)
        #if the form was valid,save it and redirect us to the site for the new plan
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../'+ str(Assignment.objects.latest('id').id))
    else:
        #if we dont get a POST request, send the form class with the dictionary to the template
        form = CreateAssignment()
        context['form'] = form
    return render(request,'make/createAssignment.html',context)

def edit_assignment(request, assignment_id):
    context={}
    #when we get the id of the assingement from url, we look up if there is an object in the
    #database who has that id
    assignment = Assignment.objects.get(id=assignment_id)
    multipleChoiseQuestions = assignment.MultipleChoiseQuestions.all()
    trueFalseQuestions = assignment.TrueFalseQuestions.all()
    oneWordQuestions = assignment.OneWordQuestions.all()
    #if we get a POST request jump into the if statement
    if request.method == 'POST':
        if "create_mcq_question" in request.POST:
            question = request.POST.get('question')
            answear = request.POST.get('answear')
            choises = request.POST.get('choice_0')+","+request.POST.get('choice_1')+","+request.POST.get('choice_2') +","+request.POST.get('choice_3')
            #Need to find a better way
            mcq = MultipleChoiseQuestion()
            mcq.assignment = Assignment.objects.get(id=assignment_id)
            mcq.question = question
            mcq.answear = answear
            mcq.choises = choises
            mcq.save()
            return HttpResponseRedirect('../'+assignment_id +"/edit")
        if "create_tfq_question" in request.POST:
            form= CreateTrueFalseQuestion(request.POST)
            if form.is_valid():
                tfq = TrueFalseQuestion()
                tfq.assignment = Assignment.objects.get(id=assignment_id)
                tfq.question = form.cleaned_data['question']
                tfq.answear = form.cleaned_data['answear']
                tfq.save()
                return HttpResponseRedirect('../'+assignment_id+"/edit")
        if "create_owq_question" in request.POST:
            form= CreateOneWordQuestion(request.POST)
            if form.is_valid() and  " " not in request.POST['answear']:
                owq = OneWordQuestion()
                owq.assignment = Assignment.objects.get(id=assignment_id)
                owq.question = form.cleaned_data['question']
                owq.answear = form.cleaned_data['answear']
                owq.save()
                return HttpResponseRedirect('../'+assignment_id+"/edit")
        if "delete_mcq_question" in request.POST:
            id = request.POST['mcq_id']
            multipleChoiseQuestions.filter(id=id).delete()
            return HttpResponseRedirect('../'+assignment_id +"/edit")
        if "delete_tfq_question" in request.POST:
            id = request.POST['tfq_id']
            trueFalseQuestions.filter(id=id).delete()
            return HttpResponseRedirect('../'+assignment_id +"/edit")
        if "delete_owq_question" in request.POST:
            id = request.POST['owq_id']
            oneWordQuestions.filter(id=id).delete()
            return HttpResponseRedirect('../'+assignment_id +"/edit")


    #all the questions that are connectet to the assingement gets sent off with
    #the dictionary to the assingement.html page
    mcq_form = CreateMultipleChoiseQuestion()
    tfq_form = CreateTrueFalseQuestion()
    owq_form = CreateOneWordQuestion()
    context = {
        'mcq_form': mcq_form,
        'tfq_form': tfq_form,
        'owq_form': owq_form,
        'assignment': assignment,
        'multipleChoiseQuestions': multipleChoiseQuestions,
        'trueFalseQuestions': trueFalseQuestions,
        'oneWordQuestions': oneWordQuestions,

    }
    return render(request, 'view/assignment.html', context)
