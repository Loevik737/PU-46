from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from CheckPoint.apps.subject.models import Subject

from CheckPoint.apps.assignment.forms import (CreateAssignment, CreateMultipleChoiseQuestion,
                    CreateOneWordQuestion, CreateTrueFalseQuestion)
from CheckPoint.apps.assignment.models import (Assignment, MultipleChoiseQuestion, OneWordQuestion,
                     TrueFalseQuestion, UserAnswers)


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

def result_assignment(request,assignment_id):
    user = request.user.customuser
    context = {}
    if user.role == "Student" or user.role =="Teacher":
        assignment = Assignment.objects.get(id=assignment_id)
        user_answers,created = assignment.UserAnswers.get_or_create(user = user,assignment=assignment)
        context['user_attempts'] = user_answers.attempts
        context['max_attempts'] = assignment.tries
        context['user_wrongMCQ'] =user_answers.wrongMCQ
        context['user_wrongTFQ'] =user_answers.wrongTFQ
        context['user_wrongOWQ'] =user_answers.wrongOWQ
    else:
        context['decline'] = 1
    if user_answers.attempts < assignment.tries:
        context['retry'] = 1
        context['as_id'] = assignment_id
    return render(request, 'result/resultAssignment.html', context)

def answer_assignment(request,assignment_id):

    user = request.user.customuser
    context = {}
    if user.role == "Student" or user.role =="Teacher":
        assignment = Assignment.objects.get(id=assignment_id)
        user_answers,created = assignment.UserAnswers.get_or_create(user = user,assignment=assignment)
        if user_answers.attempts <= assignment.tries:
            multipleChoiseQuestions = assignment.MultipleChoiseQuestions.all()
            trueFalseQuestions = assignment.TrueFalseQuestions.all()
            oneWordQuestions = assignment.OneWordQuestions.all()
            if request.method == "POST":
                answers = {
                    'MCQ' : {},
                    'TFQ' : {},
                    'OWQ' : {}
                    }
                for elem in request.POST:
                    if 'MCQ' in  elem or 'TFQ' in elem or 'OWQ' in elem:
                        answers[elem[0:3]][str(elem[3:len(elem)])] = request.POST.get(elem)
                for q in multipleChoiseQuestions:
                    if str(q.answear) != answers['MCQ'][str(q.pk)]:
                        user_answers.wrongMCQ.add(q)
                    else:
                        if q in user_answers.wrongMCQ.all():
                            user_answers.wrongMCQ.remove(q)
                for q in trueFalseQuestions:
                    if str(q.answear) != answers['TFQ'][str(q.pk)]:
                        user_answers.wrongTFQ.add(q)
                    else:
                        if q in user_answers.wrongTFQ.all():
                            user_answers.wrongTFQ.remove(q)
                for q in oneWordQuestions:
                    if str(q.answear) != answers['OWQ'][str(q.pk)]:
                        user_answers.wrongOWQ.add(q)
                    else:
                        if q in user_answers.wrongOWQ.all():
                            user_answers.wrongOWQ.remove(q)
                user_answers.attempts +=1
                user_answers.save()
                return HttpResponseRedirect('../'+assignment_id + '/result')

            context = {
                'assignment': assignment,
                'multipleChoiseQuestions': multipleChoiseQuestions,
                'trueFalseQuestions': trueFalseQuestions,
                'oneWordQuestions': oneWordQuestions,
            }
        else:
            context['decline'] = 1
    else:
        context['decline'] = 1
    return render(request,"answer/answerAssignment.html",context)

def create_assignment(request):
    user = request.user
    #the dictionary we will send to the html template
    context={}
    if user.customuser.role == 'Teacher':
        #if we get a POST request jump into the if statement
        if request.method == 'POST':
            #set for to the POST request we got
            form = CreateAssignment(request.POST)
            #if the form was valid,save it and redirect us to the site for the new plan
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('../'+ str(Assignment.objects.latest('id').id)+'/edit')
            else:
                context["form"] = form
        else:
            #if we dont get a POST request, send the form class with the dictionary to the template
            form = CreateAssignment()
            context['form'] = form
    else:
        context['decline'] = 1
    return render(request,'create/createAssignment.html',context)

def edit_assignment(request, assignment_id):
    context={}
    user = request.user.customuser
    assignment = Assignment.objects.get(id=assignment_id)
    if user.role == 'Teacher' and user.teachingSubject.all().filter(id=assignment.subject_id).exists():

        #when we get the id of the assingement from url, we look up if there is an object in the
        #database who has that id
        multipleChoiseQuestions = assignment.MultipleChoiseQuestions.all()
        trueFalseQuestions = assignment.TrueFalseQuestions.all()
        oneWordQuestions = assignment.OneWordQuestions.all()
        #if we get a POST request jump into the if statement
        if request.method == 'POST':
            if "create_mcq_question" in request.POST:
                question = request.POST.get('question')
                answear = request.POST.get('answear')
                choises = request.POST.get('choice_0')+","+request.POST.get('choice_1')+","+request.POST.get('choice_2') +","+request.POST.get('choice_3')
                #Need to find a better way for validation here. All other forms are properly validated
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
            #if we get a POST request with delete<question> we take the id of the question and deletes
            #the corresponding model instance
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
    else:
        context['decline'] = 1
    return render(request, 'edit/editAssignment.html', context)
