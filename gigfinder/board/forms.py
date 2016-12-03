"""
Board app forms based on models
"""
# from django import forms
from django.forms.widgets import DateInput
from django.contrib.admin.widgets import AdminDateWidget
import floppyforms.__future__ as forms
from board.models import Event, Job_Posting, Musician_Advertisement


class EventForm(forms.ModelForm):
    """
    Defines the form for the Event model
    """
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['pub_date', ]


class JobForm(forms.ModelForm):
    """
    Defines the form for the Job Postings model
    """
    class Meta:
        model = Job_Posting
        fields = '__all__'
        exclude = []


class AdForm(forms.ModelForm):
    """
    Defines the form for the Musician Advertisements model
    """
    class Meta:
        model = Musician_Advertisement
        fields = '__all__'
        exclude = []
