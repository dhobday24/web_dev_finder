from django.test import TestCase
from board.forms import *
import unittest
from . import models
import datetime
from django.utils import timezone
# Create your tests here.

class gigfinderTests(TestCase):
    # homepage underconstruction
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_board(self):
        response = self.client.get('/board/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/board/events">Events Board</a>', status_code=200, html=True)
        self.assertContains(response, '<a href="/board/job_posts">Open Jobs</a>', status_code=200, html=True)
        self.assertContains(response, '<a href="/board/talent_ads">Talent Ads</a>', status_code=200, html=True)
        self.assertTemplateUsed(response, 'board/board.html')

    def test_event(self):
        response = self.client.get('/board/events/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/board">Go Back to Boards</a>', status_code=200, html=True)
        self.assertTemplateUsed(response, 'board/event_board.html')


    def test_job_posts(self):
        response = self.client.get('/board/job_posts/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/board">Go Back to Boards</a>', status_code=200, html=True)
        self.assertTemplateUsed(response, 'board/job_posts_board.html')

    def test_talent_ads(self):
        response = self.client.get('/board/talent_ads/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/board">Go Back to Boards</a>', status_code=200, html=True)
        self.assertTemplateUsed(response, 'board/musician_ads_board.html')

    def test_forms(self):
        event_form = EventForm()
        job_form = JobForm()
        ad_form = AdForm()
        self.assertFalse(event_form.is_valid())
        self.assertFalse(job_form.is_valid())
        self.assertFalse(ad_form.is_valid())

#testing models
class EventTestCase(unittest.TestCase):
    def setUp(self):
        self.event1 = Event.objects.create(event_name="Event1", 
                    event_description_short = "short description of the event", 
                    event_description_long="long description of the event test",
                    pub_date = datetime.date(2016, 11, 11),
                    event_date = datetime.date(2016, 12, 11)
                    )

    def test_event(self):

        self.assertEquals(self.event1.event_name, 'Event1')
        self.assertEquals(self.event1.event_description_short, 'short description of the event')
        self.assertEquals(self.event1.event_description_long,'long description of the event test')
        self.assertEquals(self.event1.pub_date, datetime.date(2016,11,11))
        self.assertEquals(self.event1.event_date, datetime.date(2016,12,11))
    

class Job_PostingTestCase(unittest.TestCase):
    def setUp(self):
        self.JobPosting = Job_Posting.objects.create(
            posting_name = 'posting name',
            job_description_short= 'short job description',
            job_description_long = 'long job description',
            pub_date = datetime.date(2016, 11, 11),
            start_date = datetime.date(2016,11,11),
            end_date  = datetime.date(2016, 12, 11),
            pay = '200',
            )

    def test_job_posting(self):
        self.assertEquals(self.JobPosting.posting_name, 'posting name')
        self.assertEquals(self.JobPosting.job_description_short, 'short job description')
        self.assertEquals(self.JobPosting.job_description_long, 'long job description')
        self.assertEquals(self.JobPosting.pub_date, datetime.date(2016,11,11))
        self.assertEquals(self.JobPosting.start_date, datetime.date(2016,11,11))
        self.assertEquals(self.JobPosting.end_date, datetime.date(2016,12,11))
        self.assertEquals(self.JobPosting.pay, '200')

class Musician_adTestCase(unittest.TestCase):
    def setUp(self):
        self.musicians_ads = Musician_Advertisement.objects.create(
            musician_name = 'Musician Name',
            ad_description_short = 'short ad description',
            ad_description_long = 'long ad description',
            pub_date = datetime.date(2016,11,11),
            start_availability = datetime.date(2017,1,1),
            end_availability = datetime.date(2017, 1, 7)
            )
    def test_musician_ads(self):
        self.assertEquals(self.musicians_ads.musician_name, 'Musician Name')
        self.assertEquals(self.musicians_ads.ad_description_short, 'short ad description')
        self.assertEquals(self.musicians_ads.ad_description_long, 'long ad description')
        self.assertEquals(self.musicians_ads.pub_date, datetime.date(2016,11,11))
        self.assertEquals(self.musicians_ads.start_availability, datetime.date(2017,1,1))
        self.assertEquals(self.musicians_ads.end_availability, datetime.date(2017,1,7))










