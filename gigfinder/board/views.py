from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event, Job_Posting, Musician_Advertisement
# Create your views here.

def events(request):
    latest_events_list = Event.objects.order_by('-pub_date')[:5]
    context = {
        'latest_events_list': latest_events_list,
    }
    return render(request, 'board/event_board.html', context)

def job_posts(request):
    latest_posts_list = Job_Posting.objects.order_by('-pub_date')[:5]
    context = {
        'latest_posts_list': latest_posts_list,
    }
    return render(request, 'board/job_posts_board.html', context)

def musician_ads(request):
    latest_ads_list = Musician_Advertisement.objects.order_by('-pub_date')[:5]
    context = {
        'latest_ads_list': latest_ads_list,
    }
    return render(request, 'board/musician_ads_board.html', context)
