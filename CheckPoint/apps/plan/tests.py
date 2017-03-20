from django.test import TestCase
from CheckPoint.apps.subject.models import Subject
from CheckPoint.apps.plan.models import Plan, Week, Lecture, Objectives
from .forms import CreatePlanForm, CreateLectureForm
import datetime


_test_plan_data = {
        'title': "Plan for digdat.",
        'term': "Host",
        'year': 2017,
        'subject': 1
}

_test_week_data = {
    'week_number': 1,
}

_test_subject_data = {
        'code': "TDT4140",
        'name': "Software Engenering"
}

_test_lecture_data = {
    'title': "Tittel",
    'comment': "Kommentar1",
}

_test_objectives_data = [
    {
        'learning_objective': "Learn something."
    },
    {
        'learning_objective': "Learn something else."
    }
]


class CreateTestCase(TestCase):
    def setUp(self):
        self.sub = Subject.objects.create(**_test_subject_data)
        _test_plan_data['subject'] = self.sub
        self.plan = Plan.objects.create(**_test_plan_data)
        _test_week_data['plan'] = self.plan
        self.week = Week.objects.create(**_test_week_data)
        _test_objectives_data[0]['subject'] = self.sub
        _test_objectives_data[1]['subject'] = self.sub
        self.obj1 = Objectives.objects.create(**_test_objectives_data[0])
        self.obj2 = Objectives.objects.create(**_test_objectives_data[1])
        _test_lecture_data['plan'] = self.plan
        _test_lecture_data['week'] = self.week
        self.lecture = Lecture.objects.create(**_test_lecture_data)
        self.lecture.objectives = [self.obj1, self.obj2]

    def test_create_form_valid(self):
        form = CreateLectureForm(data=_test_lecture_data)
        self.assertTrue(form.is_valid())

    def test_createPlan(self):
        form = CreatePlanForm(data=_test_plan_data)
        self.assertTrue(form.is_valid())

    def test_createLecture(self):
        pass




