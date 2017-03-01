from django.test import TestCase
from CheckPoint.apps.registration.forms import RegistrationForm

# Create your tests here.
class formTests(TestCase):

    def test_registrationRegistration_form_full(self):
        form_data={'username':'per', 'email':'per@per.com', 'password1':'per123', 'password2':'per123'}
        form=RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registrationRegistration_username_invalid(self):
        form_data={'username':'per?', 'email':'per@per.com', 'password1':'per123', 'password2':'per123'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {'username': [u'This value must contain only letters, numbers and underscores.']})

    def test_registrationRegistration_email_invalid(self):
        form_data={'username':'per', 'email':'per.com', 'password1':'per123', 'password2':'per123'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_registrationRegistration_username_and_email_empty(self):
        form_data={'username':'', 'email':'', 'password1':'per123', 'password2':'per123'}
        form=RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': [u'This field is required.'],
            'email': [u'This field is required.']
        })
