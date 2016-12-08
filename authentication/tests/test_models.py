from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from authentication.models import UserProfile, create_profile


class UserProfileTest(TestCase):
    def setUp(self):
        user = User(username='felipe', email='something@aol.com')
        self.venue_profile = UserProfile(user=user,
                                         type_user='Venue',
                                         address='35W 67th st, New York, NY',
                                         bio='Hello There',
                                         website='www.google.com',
                                         phonenumber='9999999999',
                                         genre='Rock',
                                         soundcloud_username='tfloud',
                                         )

    def test_userprofile(self):
        self.assertEqual(self.venue_profile.user.username, 'felipe')
        self.assertEqual(self.venue_profile.type_user, 'Venue')
        self.assertEqual(self.venue_profile.address, '35W 67th st, New York, NY')
        self.assertEqual(self.venue_profile.bio, 'Hello There')
        self.assertEqual(self.venue_profile.website, 'www.google.com')
        self.assertEqual(self.venue_profile.phonenumber, '9999999999')
        self.assertEqual(self.venue_profile.genre, 'Rock')
        self.assertEqual(self.venue_profile.soundcloud_username, 'tfloud')
        self.assertEqual(self.venue_profile.__str__(), self.venue_profile.user.username)


# class UserProfileTestMommy(TestCase):
#     def test_userprofile_creation_mommy(self):
#         new_userprofile = mommy.make('authentication.UserProfile')
#         self.assertTrue(isinstance(new_userprofile, UserProfile))
#         self.assertEqual(new_userprofile.__str__(), new_userprofile.user.username)

    def test_registration_userprofile_created_mommy(self):
        """
        Test that a ``UserProfile`` is created for a new user.
        """
        new_userprofile1 = mommy.make('authentication.UserProfile')
        new_userprofile2 = mommy.make('authentication.UserProfile')
        self.assertTrue(isinstance(new_userprofile1, UserProfile))
        self.assertEqual(UserProfile.objects.count(), 2)
