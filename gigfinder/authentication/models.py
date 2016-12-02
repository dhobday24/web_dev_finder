from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PROFILE_TYPES = (
    ('Musician', 'Musician'),
    ('Venue', 'Venue'),
)
AVALABILITY = (
    ('LFG', 'Looking For Gig'),
    ('AB', 'Already Booked'),
)

class MusicianUserProfile(models.Model):
    user = models.ForeignKey(User)
    type_user = models.CharField(max_length=20, default='Musician',choices=PROFILE_TYPES)
    location = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=400, blank=True)
    website = models.CharField(max_length=50, blank='user@example.com')
    phonenumber = models.CharField(max_length=13,default='999-999-9999')
    profile_pic = models.ImageField(null=True, blank=True)
    genre = models.CharField(max_length=30, blank=True)
    available=models.CharField(choices=AVALABILITY, max_length=20, blank=True)

class VenueUserProfile(models.Model):
    user = models.ForeignKey(User)
    type_user = models.CharField(max_length=20, default='Venue',choices=PROFILE_TYPES)
    location = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=400, blank=True)
    website = models.CharField(max_length=50, blank='user@example.com')
    phonenumber = models.CharField(max_length=13,default='999-999-9999')
    profile_pic = models.ImageField(null=True, blank=True)
