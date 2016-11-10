from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Event, Job_Posting, Musician_Advertisement
# Create your views here.

def board(request):
    return render(request, 'board/board.html')

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

def long_description_event(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    return render(request, 'board/event_long.html', {'event': event})

def long_description_job(request, job_id):
    job = get_object_or_404(Job_Posting, pk = job_id)
    return render(request, 'board/job_long.html', {'job': job})

def long_description_musad(request, ad_id):
    ad = get_object_or_404(Musician_Advertisement, pk = ad_id)
    return render(request, 'board/ad_long.html', {'ad': ad})
