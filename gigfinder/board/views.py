from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event, Job_Posting, Musician_Advertisement
# Create your views here.

def events(request):
    latest_events_list = Event.objects.order_by('-pub_date')[:5]
    template = loader.get_template('board/event_board.html')
    context = {
        'latest_events_list': latest_events_list,
    }
    return HttpResponse(template.render(context, request))

def job_posts(request):
    latest_posts_list = Job_Posting.objects.order_by('-pub_date')[:5]
    template = loader.get_template('board/job_posts_board.html')
    context = {
        'latest_posts_list': latest_posts_list,
    }
    return HttpResponse(template.render(context, request))

def musician_ads(request):
    latest_ads_list = Musician_Advertisement.objects.order_by('-pub_date')[:5]
    template = loader.get_template('board/musician_ads_board.html')
    context = {
        'latest_ads_list': latest_ads_list,
    }
    return HttpResponse(template.render(context, request))
