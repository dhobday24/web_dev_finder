"""
Admin Backend  for the board app
"""
from django.contrib import admin
from .models import Event, Musician_Advertisement, Application
#from board.models import Job_Posting
# Register your models here.

admin.site.register(Event)
#admin.site.register(Job_Posting)
admin.site.register(Musician_Advertisement)
admin.site.register(Application)
