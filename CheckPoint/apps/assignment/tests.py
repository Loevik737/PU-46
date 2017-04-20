
from django.test import TestCase

from CheckPoint.apps.subject.models import Subject
# Create your tests here.
from .forms import (CreateAssignment, CreateMultipleChoiseQuestion,
                   CreateOneWordQuestion, CreateTrueFalseQuestion)
from .models import Assignment
from CheckPoint.apps.registration.models import CustomUser
from django.contrib.auth.models import User


#the tests below should be easy to understand, and contains nothing only tests for assignment
#and question forms
class assignmentFormTest( TestCase):
    subject_pk = 1
    @classmethod
    def setUpTestData(cls):
        subject = Subject.objects.create(code="TDT1000", name="test")
        user =User.objects.create(username = 'per')
        CustomUser.objects.create(user=user,role="Teacher")
        CustomUser.objects.get(pk=1).teachingSubject.add(subject)
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
    @classmethod
    def setUpTestData(cls):
        cls.subject = Subject.objects.create(code="TDT1000", name="test")
        Assignment.objects.create(title="test",subject=cls.subject,term="automn",year=2019)

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

    def test_view_create_teacher(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/assignment/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create/createAssignment.html')

    def test_view_viewSubjectAssignments(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/assignment/allteaching/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewall/viewAssignments.html')

    def test_view_viewSubjectAttendingAssignments(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/assignment/allattending/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewall/viewAttendingAssignments.html')

    def test_view_index(self):
        self.client.login(username='student',password="12345")
        response = self.client.get('/assignment/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view/assignment.html')
