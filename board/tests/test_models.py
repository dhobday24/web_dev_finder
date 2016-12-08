from django.test import TestCase
from board.forms import *
import unittest
from board import models
from datetime import date
from django.utils import timezone

#testing models
class EventTestCase(unittest.TestCase):
    def setUp(self):
        self.event1 = Event.objects.create(event_name="Event1", 
                    event_description_short = "short description of the event", 
                    event_description_long="long description of the event test",
                    pub_date = date(2016, 11, 11),
                    event_date = date(2016, 12, 11)
                    )

    def test_event(self):

        self.assertEquals(self.event1.event_name, 'Event1')
        self.assertEquals(self.event1.event_description_short, 'short description of the event')
        self.assertEquals(self.event1.event_description_long,'long description of the event test')
        self.assertEquals(self.event1.pub_date, date(2016,11,11))
        self.assertEquals(self.event1.event_date, date(2016,12,11))


class Musician_adTestCase(unittest.TestCase):
    def setUp(self):
        self.musicians_ads = Musician_Advertisement.objects.create(
            musician_name = 'Musician Name',
            ad_description_short = 'short ad description',
            ad_description_long = 'long ad description',
            pub_date = date(2016,11,11),
            start_availability = date(2017,1,1),
            end_availability = date(2017, 1, 7)
            )
    def test_musician_ads(self):
        self.assertEquals(self.musicians_ads.musician_name, 'Musician Name')
        self.assertEquals(self.musicians_ads.ad_description_short, 'short ad description')
        self.assertEquals(self.musicians_ads.ad_description_long, 'long ad description')
        self.assertEquals(self.musicians_ads.pub_date, date(2016,11,11))
        self.assertEquals(self.musicians_ads.start_availability, date(2017,1,1))
        self.assertEquals(self.musicians_ads.end_availability, date(2017,1,7))

# class Job_PostingTestCase(unittest.TestCase):
#     def setUp(self):
#         self.JobPosting = Job_Posting.objects.create(
#             posting_name = 'posting name',
#             job_description_short= 'short job description',
#             job_description_long = 'long job description',
#             pub_date = date(2016, 11, 11),
#             start_date = date(2016,11,11),
#             end_date  = date(2016, 12, 11),
#             pay = '200',
#             )
#
#     def test_job_posting(self):
#         self.assertEquals(self.JobPosting.posting_name, 'posting name')
#         self.assertEquals(self.JobPosting.job_description_short, 'short job description')
#         self.assertEquals(self.JobPosting.job_description_long, 'long job description')
#         self.assertEquals(self.JobPosting.pub_date, date(2016,11,11))
#         self.assertEquals(self.JobPosting.start_date, date(2016,11,11))
#         self.assertEquals(self.JobPosting.end_date, date(2016,12,11))
#         self.assertEquals(self.JobPosting.pay, '200')