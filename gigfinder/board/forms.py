import floppyforms.__future__ as forms
#from django import forms
from django.forms.widgets import DateInput
from django.contrib.admin.widgets import AdminDateWidget
from .models import Event, Job_Posting, Musician_Advertisement


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['pub_date',]

class JobForm(forms.ModelForm):
    class Meta:
        model = Job_Posting
        fields = '__all__'
        exclude = []

class AdForm(forms.ModelForm):
    class Meta:
        model = Musician_Advertisement
        fields = '__all__'
        exclude = []
