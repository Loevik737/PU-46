
from django.test import TestCase
# Create your tests here.
from forms import CreateAssignment,CreateMultipleChoiseQuestion,CreateTrueFalseQuestion
from models import Assignment
from CheckPoint.apps.subject.models import Subject

class assignmentTest( TestCase):
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

class questionsTest( TestCase):
    assignment_pk = 1
    @classmethod
    def setUpTestData(cls):
        cls.subject = Subject.objects.create(code="TDT1000", name="test")
        Assignment.objects.create(title="test",subject=cls.subject,term="automn",year=2019)

    def test_createTFQ_acccept(self):
        data = {'question':'aaa','answear':True,'assignment':self.assignment_pk}
        form = CreateTrueFalseQuestion(data= data)
        self.assertTrue(form.is_valid())
    def test_createTFQ_decline_assignment(self):
        data = {'question':'aaa','answear':True,'assignment':'fjdsiafn'}
        form = CreateTrueFalseQuestion(data= data)
        self.assertFalse(form.is_valid())
