from django.core.urlresolvers import resolve
from django.test import TestCase
from authentication.views import index
from authentication.models import UserProfile
from board.models import Event, Musician_Advertisement


class LandingPageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
