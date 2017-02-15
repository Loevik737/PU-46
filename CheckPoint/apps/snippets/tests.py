from django.test import TestCase
from models import Contact
# Create your tests here.
class ContactTests(TestCase):
    """Contact model tests."""
    def test_str(self):
        contact = Contact(first_name='John', last_name='Smith',email='test@test.com')
        self.assertEquals(
            str(contact),
            'John Smith test@test.com',
        )
