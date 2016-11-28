import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length = 200)
    event_description_short = models.CharField(max_length = 400, blank = True)
    event_description_long = models.CharField(max_length = 2000)
    pub_date = models.DateTimeField('date published', auto_now_add = True)
    event_date = models.DateField()
    event_time = models.TimeField(null = True)
    def __str__(self):
        return self.event_name

class Job_Posting(models.Model):
    posting_name = models.CharField(max_length = 200)
    job_description_short = models.CharField(max_length = 400, blank = True)
    job_description_long = models.CharField(max_length = 2000)
    pub_date = models.DateTimeField('date published', auto_now_add = True)
    start_date = models.DateField()
    end_date = models.DateField()
    pay = models.IntegerField(default = 0)
    def __str__(self):
        return self.posting_name

class Musician_Advertisement(models.Model):
    musician_name = models.CharField(max_length = 200)
    ad_description_short = models.CharField(max_length = 400, blank = True)
    ad_description_long = models.CharField(max_length = 2000)
    pub_date = models.DateTimeField('date published', auto_now_add = True)
    start_availability = models.DateField()
    end_availability = models.DateField()
    def __str__(self):
        return self.musician_name
