from django.core.urlresolvers import resolve
from django.test import TestCase, Client
from django.contrib.auth.models import User
from authentication.views import index
from authentication.models import UserProfile
from authentication.forms import UserForm, RegistrationForm
from board.models import Event, Musician_Advertisement


class LandingPageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)


class AuthenticateTest(TestCase):
    def setUp(self):
        user_venue = User.objects.create(
            username="test_venue_user",
            email="test_venue@test.com",
            password="password"
        )

        self.venue_profile = UserProfile(
            user=user_venue,
            type_user='Venue',
            address='35W 67th st, New York, NY',
            bio='Hello There',
            website='www.google.com',
            phonenumber='9999999999',
            genre='Rock',
            soundcloud_username='tfloud',
        )

        user_musician = User.objects.create(
            username="test_musician_user",
            email="test_musician@test.com",
            password="password"
        )

        self.musician_profile = UserProfile(
            user=user_musician,
            type_user='Musician',
            address='35W 67th st, New York, NY',
            bio='Hello There',
            website='www.google.com',
            phonenumber='9999999999',
            genre='Rock',
            soundcloud_username='tfloud',
        )

        self.c = Client()

    def test_login_venue(self):
        response = self.c.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        response = self.c.post('/accounts/login/', {
            'username': 'test_venue_user',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 200)

    def test_register_therapist(self):
        response = self.c.get('/register/')
        self.assertEqual(response.status_code, 200)

        # Below test is commented due to bug in register view
        # (MultiValueDictKeyError: "'type'").

        response = self.c.post('/register/',
                               {'username': 'test_venue_user',
                                'email': 'test_venuer_user@test.com',
                                'first_name': 'Philip',
                                'last_name': 'Joseph',
                                'password': 'password',
                                }
                               )
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        response = self.c.get('/logout/')
        self.assertEqual(response.status_code, 200)
