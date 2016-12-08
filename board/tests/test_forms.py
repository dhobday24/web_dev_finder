from django.test import TestCase
from board.forms import *
import unittest
from board import models
import datetime
from django.utils import timezone

class gigfinderTests(TestCase):

	def test_forms(self):
		event_form = EventForm()
		ad_form = AdForm()
		self.assertFalse(event_form.is_valid())
		self.assertFalse(ad_form.is_valid())