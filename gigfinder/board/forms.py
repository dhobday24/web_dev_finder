"""
Board app forms based on models
"""
# from django import forms
from django.forms.widgets import DateInput
from django.contrib.admin.widgets import AdminDateWidget
import floppyforms.__future__ as forms
from .models import Event, Musician_Advertisement
from address.forms import AddressField

#from board.models import Job_Posting


class EventForm(forms.ModelForm):
    """
    Defines the form for the Event model
    """
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['pub_date', 'event_user', 'event_application', 'event_lat_long',
                   'event_lat', 'event_long',]


class AdForm(forms.ModelForm):
    """
    Defines the form for the Musician Advertisements model
    """
    class Meta:
        model = Musician_Advertisement
        fields = '__all__'
        exclude = ['pub_date', 'musician_name', 'ad_application']


'''
class JobForm(forms.ModelForm):
    """
    Defines the form for the Job Postings model
    """
    class Meta:
        model = Job_Posting
        fields = '__all__'
        exclude = []
'''