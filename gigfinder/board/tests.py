from django.test import TestCase
from board.forms import *
# Create your tests here.
class gigfinderTests(TestCase):
    # homepage underconstruction
    # def test_homepage(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)

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
