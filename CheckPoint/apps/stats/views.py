from django.shortcuts import render
from CheckPoint.apps.assignment.models import *
from CheckPoint.apps.subject.models import Subject


def stats_view(request):
    user = request.user.customuser
    user_answers = UserAnswers.objects.filter(user_id=user.id)
    attending = user.attendingSubject
    print(attending)
    args = {'drawData': {}}
    for ans in user_answers:
        title = Assignment.objects.get(id=ans.assignment_id).title
        subject = str(Subject.objects.get(id =Assignment.objects.get(id=ans.assignment_id).subject_id).code)
        if attending.filter(code=subject).exists():
            if  subject not in args['drawData'].keys():
                args['drawData'][subject] = []
            args['drawData'][subject].append(str(title))
            qCount = MultipleChoiseQuestion.objects.filter(assignment_id=ans.assignment_id).count()+TrueFalseQuestion.objects.filter(assignment_id=ans.assignment_id).count()+OneWordQuestion.objects.filter(assignment_id=ans.assignment_id).count()
            wCount = ans.wrongTFQ.count()+ans.wrongOWQ.count()+ans.wrongMCQ.count()
            args['drawData'][subject].append(float(float((qCount-wCount))/qCount)*100)
    return render(request, 'stats.html', args)
