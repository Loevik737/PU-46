from django.test import TestCase
from CheckPoint.apps.registration.forms import RegistrationForm

class registrationForm(TestCase):

    def test_createUser_acccept_role(self):
        form_data={'username':'per', 'email':'per@per.com', 'password1':'per123', 'password2':'per123','role':'Student'}
        form=RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_createUser_decline_role_null(self):
        form_data={'username':'per', 'email':'per@per.com', 'password1':'per123', 'password2':'per123','role':None}
        form=RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
    def test_createUser_decline_role_not_predefined(self):
        form_data={'username':'per', 'email':'per@per.com', 'password1':'per123', 'password2':'per123','role':'jfdsifdni'}
        form=RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
