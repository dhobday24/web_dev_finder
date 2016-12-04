"""
Models for the Authentication app
"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
PROFILE_TYPES = (
    ('Musician', 'Musician'),
    ('Venue', 'Venue'),
)
AVALABILITY = (
    ('Looking For Gig', 'Looking For Gig'),
    ('Already Booked', 'Already Booked'),
)

class UserProfile(models.Model):
    """
    Model for the Musician Profile
    """
    user = models.OneToOneField(User, primary_key = True, related_name='userprofile')
    type_user = models.CharField(max_length=20, default='Musician', choices=PROFILE_TYPES)
    location = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=400, blank=True)
    website = models.CharField(max_length=50, blank='user@example.com')
    phonenumber = models.CharField(max_length=13, default='999-999-9999')
    profile_pic = models.ImageField(null=True)
    genre = models.CharField(max_length=300, blank=True)
    available = models.CharField(choices=AVALABILITY, max_length=20, blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    """
    Basic user profile creation in database
    """
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
