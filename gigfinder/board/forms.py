from django import forms

from .models import Event, Job_Posting, Musician_Advertisement

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job_Posting
        fields = '__all__'

class AdForm(forms.ModelForm):
    class Meta:
        model = Musician_Advertisement
        fields = '__all__'
