from django.shortcuts import get_object_or_404, render, reverse
from django.test import TestCase
from CheckPoint.apps.registration.models import CustomUser
from django.contrib.auth.models import User

class TestStats(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user')
        self.user.set_password('12345')
        self.user.save()
        self.cuser = CustomUser.objects.create(user=self.user,role='Teacher')

    def test_view_student_loads(self):
        self.client.login(username='user',password="12345")
        response = self.client.get('/stats/student')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stats.html')

    def test_view_teacher_loads(self):
        self.client.login(username='user',password="12345")
        response = self.client.get('/stats/teacher')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stats.html')

    def test_view_declined(self):
        self.client.login(username='user',password="")
        response = self.client.get('/stats/student')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/stats/teacher')
        self.assertEqual(response.status_code, 302)

    #def test_call_view_fails_blank(self):
        #self.client.login(username='user', password='test')
        #response = self.client.post('/url/to/view', {}) # blank data dictionary
        #self.assertFormError(response, 'form', 'some_field', 'This field is required.')
        # etc. ...

    #def test_call_view_fails_invalid(self):
        # as above, but with invalid rather than blank data in dictionary

    #def test_call_view_fails_invalid(self):
        # same again, but with valid data, then
    #    self.assertRedirects(response, '/contact/1/calls/')
