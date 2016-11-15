import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length = 200)
    event_description_short = models.CharField(max_length = 400, blank = True)
    event_description_long = models.CharField(max_length = 2000)
    pub_date = models.DateTimeField('date published')
    event_date = models.DateTimeField()
    def __str__(self):
        return self.event_name

class Job_Posting(models.Model):
    posting_name = models.CharField(max_length = 200)
    job_description_short = models.CharField(max_length = 400, blank = True)
    job_description_long = models.CharField(max_length = 2000)
    pub_date = models.DateTimeField('date published')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    pay = models.IntegerField(default = 0)
    def __str__(self):
        return self.posting_name

class Musician_Advertisement(models.Model):
    musician_name = models.CharField(max_length = 200)
    ad_description_short = models.CharField(max_length = 400, blank = True)
    ad_description_long = models.CharField(max_length = 2000)
    pub_date = models.DateTimeField('date published')
    start_availability = models.DateTimeField()
    end_availability = models.DateTimeField()
    def __str__(self):
        return self.musician_name
