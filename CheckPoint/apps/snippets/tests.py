from django.test import TestCase
from models import User
# Create your tests here.
class UserTests(TestCase):
    """User model tests."""
    def test_str(self):
        user = User(first_name='John', last_name='Smith',email='test@test.com')
        self.assertEquals(
            str(user),
            'John Smith test@test.com',
        )
