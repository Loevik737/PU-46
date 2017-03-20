from django.test import TestCase
from .forms import UpdateUser
# Create your tests here.
class formTests(TestCase):

    def test_userUpdate_form_full(self):
        form_data = {'username': 'heiPaDeg','email':'per@persen.com','first_name':'Per', 'last_name':'Person'}
        form = UpdateUser(data=form_data)
        self.assertTrue(form.is_valid())

    def test_userUpdate_form_emailError(self):
        form_data = {'username': 'heiPaDeg','email':'per@persencom','first_name':'Per', 'last_name':'Person'}
        form = UpdateUser(data=form_data)
        self.assertFalse(form.is_valid())

class viewTests(TestCase):

    def test_userInfo_view_template(self):
        response = self.client.get('/user/edit/')
        self.assertTemplateUsed(response, 'user/user.html')
