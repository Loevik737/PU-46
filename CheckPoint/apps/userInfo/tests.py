from django.test import TestCase

from .forms import UpdateUser
from CheckPoint.apps.registration.models import CustomUser
from django.contrib.auth.models import User


# Create your tests here.
class formTests(TestCase):

    def test_userUpdate_form_full(self):
        form_data = {'username': 'heiPaDeg','email':'per@persen.com','first_name':'Ola', 'last_name':'Person'}
        form = UpdateUser(data=form_data)
        self.assertTrue(form.is_valid())

    def test_userUpdate_form_emailError(self):
        form_data = {'username': 'heiPaDeg','email':'per@persencom','first_name':'Ola', 'last_name':'Person'}
        form = UpdateUser(data=form_data)
        self.assertFalse(form.is_valid())

class viewTests(TestCase):

    def setUp(self):
        self.teacher = User.objects.create(username='teacher')
        self.teacher.set_password('12345')
        self.teacher.save()
        self.cuser = CustomUser.objects.create(user=self.teacher,role='Teacher')
        self.student = User.objects.create(username='student')
        self.student.set_password('12345')
        self.student.save()
        self.cuser2 = CustomUser.objects.create(user=self.student,role='Student')

    def test_userInfo_view_template_loads(self):
        self.client.login(username='teacher', password='12345')
        response = self.client.post('/user/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user.html')


        self.client.login(username='teacher', password='12345')
        response = self.client.post('/user/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/user.html')
