from django.test import TestCase

from CheckPoint.apps.subject.models import Subject
from CheckPoint.apps.registration.models import CustomUser
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, reverse


def responceOk(self,template,response):
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, template)

class subjectPageTest( TestCase):

    def setUp(self):
        self.subject = Subject.objects.create(code="TDT1000", name="test")
        self.user =User.objects.create(username = 'teacher')
        self.user.set_password("12345")
        self.user.save()
        CustomUser.objects.create(user=self.user,role="Teacher")
        CustomUser.objects.all()[0].teachingSubject.add(self.subject)

    def test_subjectView(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.get('/home/')
        responceOk(self,'subjectHome.html',response)

    def test_subjectView_post(self):
        self.client.login(username='teacher',password="12345")
        response = self.client.post('/home/')
        responceOk(self,'subjectHome.html',response)
