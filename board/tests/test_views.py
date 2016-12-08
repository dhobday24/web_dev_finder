from django.test import TestCase
from django.core.urlresolvers import resolve
from board.forms import *
from board import models
import datetime
from django.utils import timezone
from authentication.views import index


class GigfinderTests(TestCase):
    # homepage underconstruction
    def test_homepage(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_event(self):
        response = self.client.get('/board/events/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/board">Go Back to Boards</a>', status_code=200, html=True)
        self.assertTemplateUsed(response, 'board/event_board.html')

    def test_talent_ads(self):
        response = self.client.get('/board/talent_ads/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/board">Go Back to Boards</a>', status_code=200, html=True)
        self.assertTemplateUsed(response, 'board/musician_ads_board.html')
