from django.shortcuts import render
from CheckPoint.apps.assignment.models import *
from CheckPoint.apps.subject.models import Subject


def stats_view(request):
    user = request.user.customuser
    user_answers = UserAnswers.objects.filter(user_id=user.id)
    print(user_answers)
    args = {'drawData': {}}
    for ans in user_answers:
        title = Assignment.objects.get(id=ans.assignment_id).title
        subject = Subject.objects.get(id =Assignment.objects.get(id=ans.assignment_id).subject_id).code
        args['drawData'][subject] = []
        args['drawData'][subject].append(str(title))
        args['drawData'][subject].append(MultipleChoiseQuestion.objects.filter(assignment_id=ans.assignment_id).count()+TrueFalseQuestion.objects.filter(assignment_id=ans.assignment_id).count()+OneWordQuestion.objects.filter(assignment_id=ans.assignment_id).count())
        args['drawData'][subject].append(ans.wrongTFQ.count()+ans.wrongOWQ.count()+ans.wrongMCQ.count())

    return render(request, 'stats.html', args)
