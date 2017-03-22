
from django.test import TestCase

from CheckPoint.apps.subject.models import Subject
# Create your tests here.
from .forms import (CreateAssignment, CreateMultipleChoiseQuestion,
                   CreateOneWordQuestion, CreateTrueFalseQuestion)
from .models import Assignment


#the tests below should be easy to understand, and contains nothing only tests for assignment
#and question forms
class assignmentFormTest( TestCase):
    subject_pk = 1
    @classmethod
    def setUpTestData(cls):
        Subject.objects.create(code="TDT1000", name="test")
    def test_createAssignment_acccept(self):
        data = {'title':'fnd','subject':self.subject_pk,'term':'automn' ,'year':2019}
        form = CreateAssignment(data= data)
        self.assertTrue(form.is_valid())
    def test_createAssignment_decline_term(self):
        data = {'title':'fnhhd','subject':self.subject_pk,'term':'aaaaaaaaaaaa' ,'year':2019}
        form = CreateAssignment(data= data)
        self.assertFalse(form.is_valid())
    def test_createAssignment_decline_subject(self):
        data = {'title':'fnhhd','subject':self.subject_pk+1,'term':'automn' ,'year':2019}
        form = CreateAssignment(data= data)
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

    def test_createTFQ_decline_answear_none(self):
        data = {'question':'aaa','answear':None}
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
