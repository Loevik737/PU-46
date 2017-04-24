import datetime

from django.test import TestCase

from CheckPoint.apps.plan.models import Lecture, Objectives, Plan, Week
from CheckPoint.apps.subject.models import Subject

from .forms import CreateLectureForm, CreatePlanForm

from CheckPoint.apps.registration.models import CustomUser
from django.contrib.auth.models import User

_test_plan_data = {
        'title': "Plan for digdat.",
        'term': "Host",
        'year': 2017,
        'subject': 1,
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
        self.user = User.objects.create(username='per')
        self.cuser = CustomUser.objects.create(user= self.user,role="Teacher")
        self.cuser.teachingSubject.add(self.sub)

    def test_create_form_valid(self):
        form = CreateLectureForm(data=_test_lecture_data)
        form.objectives = self.obj1
        self.assertTrue(form.is_valid())

    def test_createPlan(self):
        _test_plan_data['subject'] = _test_plan_data['subject'].id
        form = CreatePlanForm(data=_test_plan_data,user=self.cuser)
        self.assertTrue(form.is_valid())

def containsKey(key,context):
    if key in context:
        return True
    return False

def responceOk(self,template,response):
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, template)


class ViewTestCase(TestCase):
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
        self.teacher = User.objects.create(username='teacher')
        self.teacher.set_password('12345')
        self.teacher.save()
        self.cuser = CustomUser.objects.create(user=self.teacher,role='Teacher')
        self.student = User.objects.create(username='student')
        self.student.set_password('12345')
        self.student.save()
        self.cuser2 = CustomUser.objects.create(user=self.student,role='Student')
        self.subject = Subject.objects.create(code="TDT1000",name="abc")
        self.cuser.teachingSubject.add(self.subject)
        self.cuser2.attendingSubject.add(self.subject)


    def test_view_index(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/plan/'+ str(Plan.objects.all()[0].id))
        responceOk(self,'plan/plan.html',response)
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/plan/'+ str(Plan.objects.all()[0].id))
        responceOk(self,'plan/plan.html',response)

    def test_view_show_related_plans(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/plan/all/')
        responceOk(self,'plan/allPlans.html',response)
        self.assertEqual(containsKey('plans',response.context),True)

    def test_view_create_plan_student_decline(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/plan/create/')
        responceOk(self,'plan/createplan.html',response)
        self.assertEqual(response.context['decline'], 1)

    def test_view_create_plan_teacher_loads(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/plan/create/')
        responceOk(self,'plan/createplan.html',response)
        self.assertEqual(response.context['decline'], 0)
        self.assertEqual(containsKey('form',response.context),True)

    def test_view_edit_loads(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/plan/edit/'+str(Lecture.objects.all()[0].id))
        responceOk(self,'plan/editlecture.html',response)
        self.assertEqual(response.context['decline'],0)
        self.assertEqual(containsKey('lecture',response.context),True)
        self.assertEqual(containsKey('edit_form',response.context),True)

    def test_view_edit_decline(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/plan/edit/'+str(Lecture.objects.all()[0].id))
        responceOk(self,'plan/editlecture.html',response)
        self.assertEqual(response.context['decline'],1)

    def test_view_create_lecture_loads(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.post('/plan/'+str(Plan.objects.all()[0].id) + '/addLecture/' + str(1),follow=True)
        self.assertEqual(response.status_code,200)

    def test_view_create_lecture_decline(self):
        self.client.login(username='student',password="12345")
        response = self.client.post('/plan/'+str(Plan.objects.all()[0].id) + '/addLecture/' + str(1),follow=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['decline'],1)


    def test_view_edit_lecture_loads(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.post('/plan/editLecture/'+str(Lecture.objects.all()[0].id),follow=True)
        self.assertEqual(response.status_code,200)

    def test_view_edit_lecture_decline(self):
        self.client.login(username='student',password="12345")
        response = self.client.post('/plan/editLecture/'+str(Lecture.objects.all()[0].id),follow=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['decline'],1)

    def test_view_create_week_loads(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.post('/plan/'+str(Plan.objects.all()[0].id)+'/createWeek/',follow=True)
        self.assertEqual(response.status_code,200)

    def test_view_create_week_decline(self):
        self.client.login(username='student',password="12345")
        response = self.client.post('/plan/'+str(Plan.objects.all()[0].id)+'/createWeek/',follow=True)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['decline'],1)
