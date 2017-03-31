from django.shortcuts import render
from CheckPoint.apps.assignment.models import *
from CheckPoint.apps.subject.models import Subject


def stats_view(request):
    user = request.user.customuser
    user_answers = UserAnswers.objects.filter(user_id=user.id)
    attending = user.attendingSubject
    args = {'drawData': {}}
    args['average'] = [0,0]
    for ans in user_answers:
        title = Assignment.objects.get(id=ans.assignment_id).title
        subject = str(Subject.objects.get(id =Assignment.objects.get(id=ans.assignment_id).subject_id).code)
        if attending.filter(code=subject).exists():
            if  subject not in args['drawData'].keys():
                args['drawData'][subject] = []
            args['drawData'][subject].append(str(title))
            qCount = MultipleChoiseQuestion.objects.filter(assignment_id=ans.assignment_id).count()+TrueFalseQuestion.objects.filter(assignment_id=ans.assignment_id).count()+OneWordQuestion.objects.filter(assignment_id=ans.assignment_id).count()
            wCount = ans.wrongTFQ.count()+ans.wrongOWQ.count()+ans.wrongMCQ.count()
            persentage = float(float((qCount-wCount))/qCount)*100
            args['average'][0] += persentage
            args['average'][1] +=1
            args['drawData'][subject].append(persentage)
    if args['average'][1]>0:
        args['average'] = round(args['average'][0]/args['average'][1],2)
    return render(request, 'stats.html', args)
