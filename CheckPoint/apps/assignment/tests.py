from django.test import TestCase

from CheckPoint.apps.subject.models import Subject
# Create your tests here.
from .forms import (CreateAssignment, CreateMultipleChoiseQuestion,
                   CreateOneWordQuestion, CreateTrueFalseQuestion)
from .models import Assignment
from CheckPoint.apps.registration.models import CustomUser
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, reverse


#the tests below should be easy to understand, and contains nothing only tests for assignment
#and question forms
class assignmentFormTest( TestCase):
    subject_pk = 1
    def setUp(self):
        self.subject = Subject.objects.create(code="TDT1000", name="test")
        self.user =User.objects.create(username = 'per')
        CustomUser.objects.create(user=self.user,role="Teacher")
        CustomUser.objects.get(pk=1).teachingSubject.add(self.subject)
    def test_createAssignment_acccept(self):
        data = {'title':'abc','subject':self.subject_pk,'term':'automn' ,'year':2019,'tries':3}
        form = CreateAssignment(data,user=CustomUser.objects.get(pk=1))
        self.assertTrue(form.is_valid())
    def test_createAssignment_decline_term(self):
        data = {'title':'fnhhd','subject':self.subject_pk,'term':'aaaaaaaaaaaa' ,'year':2019,'tries':3}
        form = CreateAssignment(data,user=CustomUser.objects.get(pk=1))
        self.assertFalse(form.is_valid())
    def test_createAssignment_decline_subject(self):
        data = {'title':'fnhhd','subject':self.subject_pk+1,'term':'automn' ,'year':2019,'tries':3}
        form = CreateAssignment(data,user=CustomUser.objects.get(pk=1))
        self.assertFalse(form.is_valid())

class questionsFormTest( TestCase):

    def setUp(self):
        self.subject = Subject.objects.create(code="TDT1000", name="test")
        Assignment.objects.create(title="test",subject=self.subject,term="automn",year=2019)

    def test_createTFQ_acccept(self):
        data = {'question':'aaa','answear':True}
        form = CreateTrueFalseQuestion(data= data)
        self.assertTrue(form.is_valid())

    def test_createTFQ_decline_question_none(self):
        data = {'question':None,'answear':True}
        form = CreateTrueFalseQuestion(data= data)
        self.assertFalse(form.is_valid())


    def test_createOWQ_acccept(self):
        data = {'question':'aaa?','answear':'ja'}
        form = CreateOneWordQuestion(data= data)
        self.assertTrue(form.is_valid())

    def test_createOWQ_decline_answear_none(self):
        data = {'question':'aaa?','answear':None}
        form = CreateOneWordQuestion(data= data)
        self.assertFalse(form.is_valid())

    def test_createOWQ_decline_question_none(self):
        data = {'question':None,'answear':'ja'}
        form = CreateOneWordQuestion(data= data)
        self.assertFalse(form.is_valid())

    def test_createOWQ_decline_answear_space(self):
        data = {'question':None,'answear':'ja da'}
        form = CreateOneWordQuestion(data= data)
        self.assertTrue(form.has_error('answear', code='contained space'))


def responceOk(self,template,response):
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, template)

class assignmentViewTest( TestCase):

    def setUp(self):
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
        self.assignment = Assignment.objects.create(title="abc",subject=self.subject,term="abc",year=2017,tries=1)

    def test_view_create_teacher_load_accept(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/assignment/create/')
        responceOk(self,'create/createAssignment.html',response)
        self.assertEqual(response.context['decline'],0)

    def test_view_create_student_decline(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/assignment/create/')
        responceOk(self,'create/createAssignment.html',response)
        self.assertEqual(response.context['decline'],1)

    def test_view_viewSubjectAssignments(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/assignment/allteaching/')
        responceOk(self,'viewall/viewAssignments.html',response)

    def test_view_viewSubjectAttendingAssignments(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/assignment/allattending/')
        responceOk(self,'viewall/viewAttendingAssignments.html',response)

    def test_view_assignments_teacher(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/assignment/'+ str(Assignment.objects.all()[0].id) +'/edit')
        responceOk(self,'edit/editAssignment.html',response)
        self.assertEqual(response.context['decline'], 0)

    def test_view_edit_assignments_teacher_post(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.post('/assignment/'+ str(Assignment.objects.all()[0].id) +'/edit')
        responceOk(self,'edit/editAssignment.html',response)
        self.assertEqual(response.context['decline'], 0)

    def test_view_edit_assignments_student_decline(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/assignment/'+ str(Assignment.objects.all()[0].id) +'/edit')
        responceOk(self,'edit/editAssignment.html',response)
        self.assertEqual(response.context['decline'], 1)


    def test_view_index(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/assignment/'+ str(Assignment.objects.all()[0].id))
        responceOk(self,'view/assignment.html',response)
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/assignment/'+ str(Assignment.objects.all()[0].id))
        responceOk(self,'view/assignment.html',response)

    def test_view_result_assignment(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/assignment/'+ str(Assignment.objects.all()[0].id)+ '/result')
        responceOk(self, 'result/resultAssignment.html',response)

    def test_view_answer_assignment_get(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/assignment/'+ str(Assignment.objects.all()[0].id)+ '/answer')
        responceOk(self, 'answer/answerAssignment.html',response)
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/assignment/'+ str(Assignment.objects.all()[0].id)+ '/answer')
        responceOk(self, 'answer/answerAssignment.html',response)

    def test_view_answer_assignment_post(self):
        self.client.login(username='student',password="12345")
        response = self.client.post('/assignment/'+ str(Assignment.objects.all()[0].id)+ '/answer',follow=True)
        responceOk(self, 'result/resultAssignment.html',response)
        self.client.login(username='teacher',password="12345")
        response = self.client.post('/assignment/'+ str(Assignment.objects.all()[0].id)+ '/answer',follow=True)
        responceOk(self, 'result/resultAssignment.html',response)

    def test_view_answer_assignment_post_tries_decline(self):
        self.client.login(username='student',password="12345")
        response = self.client.post('/assignment/'+ str(Assignment.objects.all()[0].id)+ '/answer',follow=True)
        responceOk(self, 'result/resultAssignment.html',response)
        response = self.client.post('/assignment/'+ str(Assignment.objects.all()[0].id)+ '/answer',follow=True)
        responceOk(self, 'answer/answerAssignment.html',response)
        self.assertEqual(response.context['decline'], 1)

    def test_create_assignment_loads(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.post('/assignment/create/')
        self.assertEqual(response.context['decline'], 0)
        responceOk(self, 'create/createAssignment.html',response)

    def test_createAssignment_decline(self):
        self.client.login(username='student',password="12345")
        response = self.client.post('/assignment/create/')
        self.assertEqual(response.context['decline'], 1)
        responceOk(self, 'create/createAssignment.html',response)
