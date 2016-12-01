from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Event, Job_Posting, Musician_Advertisement
from .forms import EventForm, JobForm, AdForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def board(request):
    return render(request, 'board/board.html')


def event_submit(request):
    form_event = EventForm(request.POST or None, request.FILES or None)
    if form_event.is_valid():
        instance = form_event.save(commit=False)
        instance.save()
        return redirect('board')
    context = {
        'form_event': form_event,
    }
    return render(request, 'board/event_submit.html', context)


def job_submit(request):
    form_job = JobForm(request.POST or None, request.FILES or None)
    if form_job.is_valid():
        instance = form_job.save(commit=False)
        instance.save()
        return redirect('board')
    context = {
        'form_job': form_job,
    }
    return render(request, 'board/job_submit.html', context)


def ad_submit(request):
    form_ad = AdForm(request.POST or None, request.FILES or None)
    if form_ad.is_valid():
        instance = form_ad.save(commit=False)
        instance.save()
        return redirect('board')
    context = {
        'form_ad': form_ad,
    }
    return render(request, 'board/ad_submit.html', context)


def events(request):
    all_events = Event.objects.all()
    context = {
        'all_events': all_events,
    }
    return render(request, 'board/event_board.html', context)


def job_posts(request):
    all_jobs = Job_Posting.objects.all()
    context = {
        'all_jobs': all_jobs,
    }
    return render(request, 'board/job_posts_board.html', context)


def musician_ads(request):
    all_ads = Musician_Advertisement.objects.all()
    context = {
        'all_ads': all_ads,
    }
    return render(request, 'board/musician_ads_board.html', context)


def long_description_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    name = event.event_name
    long_description = event.event_description_long
    date = event.event_date
    pub_date = event.pub_date
    event_image = event.event_image
    return render(request, 'board/event_long.html', {'name': name,
                                                     'long_description': long_description,
                                                     'date': date,
                                                     'event_image': event_image})


def long_description_job(request, job_id):
    job = get_object_or_404(Job_Posting, pk=job_id)
    name = job.posting_name
    long_description = job.job_description_long
    start_date = job.start_date
    end_date = job.end_date
    pay = job.pay
    job_image = job.job_image
    return render(request, 'board/job_long.html', {'name': name,
                                                   'long_description': long_description,
                                                   'start_date': start_date,
                                                   'end_date': end_date,
                                                   'pay': pay,
                                                   'job_image': job_image})


def long_description_musad(request, ad_id):
    ad = get_object_or_404(Musician_Advertisement, pk=ad_id)
    name = ad.musician_name
    long_description = ad.ad_description_long
    start_availability = ad.start_availability
    end_availability = ad.end_availability
    ad_image = ad.ad_image
    return render(request, 'board/ad_long.html', {'name': name,
                                                  'long_description': long_description,
                                                  'start_availability': start_availability,
                                                  'end_availability': end_availability,
                                                  'ad_image': ad_image})

def search_results(request):
    all_posts = Event.objects.all() + Job_Posting.objects.all() + Musician_Advertisement.objects.all()
    context = {
        'all_posts' : all_posts,
    }
    return render(request, 'board/search_results.html', context)
