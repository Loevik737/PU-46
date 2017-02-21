from django.test import TestCase
from forms import UpdateUser
# Create your tests here.
class formTests(TestCase):

    def test_userUpdate_form_full(self):
        form_data = {'username': 'hei','email':'per@per.com'}
        form = UpdateUser(data=form_data)
        self.assertTrue(form.is_valid())

    def test_userUpdate_form_empty(self):
        form_data = {}
        form = UpdateUser(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': [u'This field is required.'],
            'email': [u'This field is required.']
        })

class viewTests(TestCase):

    def test_userInfo_view_template(self):
        response = self.client.get('/users/')
        self.assertTemplateUsed(response, 'users/user.html','users/base.html')
