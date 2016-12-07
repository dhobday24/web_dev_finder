from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from authentication.forms import RegistrationForm, UserForm
from authentication.models import UserProfile


class RegistrationFormTest(TestCase):
    """
    Tests for the forms and custom validation logic included in
    django-registration.
    """
    form_data_dict = [
        # Non-alphanumeric username.
        {'data': {'username': 'alice/bob',
                  'email': 'alice@example.com',
                  'first_name': 'alice',
                  'last_name': 'bob',
                  'password1': 'secret',
                  'password2': 'secret',
                  'address': '35W 67TH st, New York, NY'
                  },
         'error': ('username', [u"Enter a valid value."])},
         # Already-existing username
        {'data': {'username': 'alice',
                  'email': 'alice@example.com',
                  'first_name': 'alice',
                  'last_name': 'bob',
                  'password1': 'secret',
                  'password2': 'secret',
                  'address': '35W 67TH st, New York, NY'
                  },
         'error': ('username', [u"This username is already taken. Please choose another one."])
         },
        # Mismatched Password
        {'data': {'username': 'alice',
                  'email': 'alice@example.com',
                  'first_name': 'alice',
                  'last_name': 'bob',
                  'password1': 'secret',
                  'password2': 'password',
                  'address': '35W 67TH st, New York, NY'
                  },
         'error': ('__all__', [u"Passwords do not match"])
         },
    ]

    def test_registration_form_valid_username_syntax(self):
        """
        Test that ``RegistrationForm`` enforces username syntax constraints
        """
        form_data = RegistrationFormTest.form_data_dict[0]
        form = RegistrationForm(data=form_data['data'])
        self.assert_(not form.is_valid())


    def test_registration_form_valid_existing_username(self):
        """
        Test that ``RegistrationForm`` enforces username length constraints
        """
        self.user = User.objects.create(username='alice', password='secret', email='alice@example.com',)
        form_data = RegistrationFormTest.form_data_dict[1]
        form = RegistrationForm(data=form_data['data'])
        self.assert_(not form.is_valid())

    def test_registration_form_matching_passwords(self):
        """
        Test that ``RegistrationForm`` has matching passwords
        """
        form_data = RegistrationFormTest.form_data_dict[2]
        form = RegistrationForm(data=form_data['data'])
        self.assert_(not form.is_valid())