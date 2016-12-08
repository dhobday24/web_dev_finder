from django.test import TestCase
from django.contrib.auth.models import User
from board.forms import *
import unittest
from board import models
from board.models import EventApplication, AdApplication
from datetime import date
from django.utils import timezone
from authentication.models import UserProfile


# testing models
class EventTestCase(TestCase):
    def setUp(self):
        user = User(username='felipe', email='something@aol.com')
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
        user2 = User(username='joe', email='something@gmail.com')
        self.vprofile = UserProfile(user=user2,
                                    type_user='Musician',
                                    address='35W 67th st, New York, NY',
                                    bio='Hello There',
                                    website='www.google.com',
                                    phonenumber='9999999999',
                                    genre='Rock',
                                    soundcloud_username='tfloud',
                                    )

        self.ads1 = Musician_Advertisement.objects.create(posting_name='Hello',
                                                          ad_description_short='short ad description',
                                                          ad_description_long='long ad description',
                                                          start_availability=date(2017, 1, 1),
                                                          end_availability=date(2017, 1, 7)
                                                          )

        self.musician_app = AdApplication(ad_name=self.ads1,
                                          user_who_applied=self.vprofile.user,
                                          )

    def test_musician_ads(self):
        self.assertEquals(self.ads1.ad_description_short, 'short ad description')
        self.assertEquals(self.ads1.ad_description_long, 'long ad description')
        self.assertEquals(self.ads1.start_availability, date(2017, 1, 1))
        self.assertEquals(self.ads1.end_availability, date(2017, 1, 7))
        self.assertEquals(self.ads1.__str__(), self.ads1.posting_name)

    def test_ad_application(self):
        self.assertEquals(self.musician_app.ad_name, self.ads1)
        self.assertEquals(self.musician_app.__str__(), self.vprofile.user.username)
