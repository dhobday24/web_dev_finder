"""
Models for the board app
"""
from django.db import models
from django.contrib.auth.models import User

from address.models import AddressField
# Create your models here.


class EventApplication(models.Model):
    """
    Model for all applications to attend an Event
    """
    event_name = models.ForeignKey('Event', null=True)
    user_who_applied = models.ForeignKey(User)
    status = models.NullBooleanField(blank=True, default=None, null=True)

    def __str__(self):
        return self.user_who_applied.username


class AdApplication(models.Model):
    """
    Model for all Ad applications
    """
    ad_name = models.ForeignKey('Musician_Advertisement', null=True)
    user_who_applied = models.ForeignKey(User)
    status = models.NullBooleanField(blank=True, default=None, null=True)

    def __str__(self):
        return self.user_who_applied.username


class Event(models.Model):
    """
    Model for the one-time event postings
    """
    event_name = models.CharField(max_length=200)
    event_description_short = models.CharField(max_length=400, blank=True)
    event_description_long = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField()
    event_time = models.TimeField(null=True)
    event_image = models.ImageField(null=True, blank=True)
    event_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    event_application = models.OneToOneField(EventApplication, null=True, blank=True)
    event_address = AddressField(null=True)
    event_lat = models.DecimalField(null=True, decimal_places=3, max_digits=5)
    event_long = models.DecimalField(null=True, decimal_places=3, max_digits=5)

    def __str__(self):
        return self.event_name


class Musician_Advertisement(models.Model):
    """
    Model for the advertisements for availability by musicians
    """
    #pylint: disable=invalid-name
    posting_name = models.CharField(null=True, max_length=200)
    musician_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ad_description_short = models.CharField(max_length=400, blank=True)
    ad_description_long = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(auto_now_add=True)
    start_availability = models.DateField()
    end_availability = models.DateField()
    ad_image = models.ImageField(null=True, blank=True)
    ad_application = models.OneToOneField(AdApplication, null=True)

    def __str__(self):
        string = str(self.posting_name)
        return string
