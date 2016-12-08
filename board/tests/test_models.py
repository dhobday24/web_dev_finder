from django.test import TestCase
from django.contrib.auth.models import User
from board.forms import *
import unittest
from board import models
from board.models import EventApplication
from datetime import date
from django.utils import timezone
from authentication.models import UserProfile


# testing models
class EventTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='felipe', email='something@aol.com')
        self.profile = UserProfile(user=user,
                                         type_user='Venue',
                                         address='35W 67th st, New York, NY',
                                         bio='Hello There',
                                         website='www.google.com',
                                         phonenumber='9999999999',
                                         genre='Rock',
                                         soundcloud_username='tfloud',
                                         )

        self.event1 = Event.objects.create(event_name="Event1",
                                           event_description_short="short description of the event",
                                           event_description_long="long description of the event test",
                                           event_date=date(2016, 12, 11)
                                           )

        self.event_app = EventApplication(event_name=self.event1,
                                          user_who_applied=self.profile.user,
                                         )

    def test_event(self):
        self.assertEquals(self.event1.event_name, 'Event1')
        self.assertEquals(self.event1.event_description_short, 'short description of the event')
        self.assertEquals(self.event1.event_description_long, 'long description of the event test')
        self.assertEquals(self.event1.event_date, date(2016, 12, 11))
        self.assertEquals(self.event1.__str__(), self.event1.event_name)

    def test_event_application(self):
        self.assertEquals(self.event_app.event_name, self.event1)
        self.assertEquals(self.event_app.__str__(), self.profile.user.username)


class Musician_adTestCase(unittest.TestCase):
    def setUp(self):
        user = User.objects.create(username='felipe', email='something@aol.com')
        self.venue_profile = UserProfile(user=user,
                                         type_user='Venue',
                                         address='35W 67th st, New York, NY',
                                         bio='Hello There',
                                         website='www.google.com',
                                         phonenumber='9999999999',
                                         genre='Rock',
                                         soundcloud_username='tfloud',
                                         )

        self.musicians_ads = Musician_Advertisement.objects.create(
            musician_name=user,
            ad_description_short='short ad description',
            ad_description_long='long ad description',
            start_availability=date(2017, 1, 1),
            end_availability=date(2017, 1, 7)
        )

    def test_musician_ads(self):
        self.assertEquals(self.musicians_ads.ad_description_short, 'short ad description')
        self.assertEquals(self.musicians_ads.ad_description_long, 'long ad description')
        self.assertEquals(self.musicians_ads.start_availability, date(2017, 1, 1))
        self.assertEquals(self.musicians_ads.end_availability, date(2017, 1, 7))
        self.assertEquals(self.musicians_ads.musician_name.username, 'felipe')
        self.assertEquals(self.musicians_ads.__str__(), str(self.musicians_ads.posting_name))
