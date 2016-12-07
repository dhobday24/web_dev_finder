from model_mommy import mommy
from django.test import TestCase
from authentication.models import UserProfile


from authentication.models import UserProfile, create_profile

class UserProfileTestMommy(TestCase):

    def test_userprofile_creation_mommy(self):
        new_userprofile = mommy.make('authentication.UserProfile')
        self.assertTrue(isinstance(new_userprofile, UserProfile))
        self.assertEqual(new_userprofile.__str__(),new_userprofile.user.username)