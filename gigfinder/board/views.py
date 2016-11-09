from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event
# Create your views here.

def events(request):
    latest_events_list = Event.objects.order_by('-pub_date')[:5]
    template = loader.get_template('board/event_board.html')
    context = {
        'latest_events_list': latest_events_list,
    }
    return HttpResponse(template.render(context, request))
