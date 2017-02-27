from django.test import TestCase
from CheckPoint.apps.subject.models import Subject
from forms import CreatePlan
import datetime
# Create your tests here.
class formTests(TestCase):

    def test_ureatePlan(self):
        valid_subject_pk = u1.pk
        form = CreatePlan(title = 'Title', subject = str(valid_subject_pk), term='Vaar', year=datetime.datetime.now().year)
        self.assertTrue(form.is_valid())
