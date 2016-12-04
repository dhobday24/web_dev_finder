"""
Views for the board app
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from board.models import Event, Musician_Advertisement
#from board.models import Job_Posting
from board.forms import EventForm, AdForm
#from board.forms import JobForm
# Create your views here.


@login_required
def board(request):
    """
    Let a logged in user see the board page
    """
    return render(request, 'board/board.html')


def event_submit(request):
    """
    Allows for the submission for a one-time event listing
    """
    form_event = EventForm(request.POST or None, request.FILES or None)
    if form_event.is_valid():
        instance = form_event.save(commit=False)
        instance.event_user = request.user
        instance.save()
        return redirect('board')
    context = {
        'form_event': form_event,
    }
    return render(request, 'board/event_submit.html', context)


'''
def job_submit(request):
    """
    Allows for the submission of a regular job posting
    """
    form_job = JobForm(request.POST or None, request.FILES or None)
    if form_job.is_valid():
        instance = form_job.save(commit=False)
        instance.save()
        return redirect('board')
    context = {
        'form_job': form_job,
    }
    return render(request, 'board/job_submit.html', context)
'''


def ad_submit(request):
    """
    Allows a musician to post an ad on their availability
    """
    form_ad = AdForm(request.POST or None, request.FILES or None)
    if form_ad.is_valid():
        instance = form_ad.save(commit=False)
        instance.musician_name = request.user
        instance.save()
        return redirect('board')
    context = {
        'form_ad': form_ad,
    }
    return render(request, 'board/ad_submit.html', context)


def events(request):
    """
    Renders a page with a list of all the events
    """
    all_events = Event.objects.all()
    context = {
        'all_events': all_events,
    }
    return render(request, 'board/event_board.html', context)


'''
def job_posts(request):
    """
    Renders a page with all the regular job postings
    """
    all_jobs = Job_Posting.objects.all()
    context = {
        'all_jobs': all_jobs,
    }
    return render(request, 'board/job_posts_board.html', context)
'''


def musician_ads(request):
    """
    Renders a page with all the musicians looking for gigs
    """
    all_ads = Musician_Advertisement.objects.all()
    context = {
        'all_ads': all_ads,
    }
    return render(request, 'board/musician_ads_board.html', context)


def long_description_event(request, event_id):
    """
    A deep dive into a specific event
    Provides the user with a longer description of the event
    """
    event = get_object_or_404(Event, pk=event_id)
    name = event.event_name
    long_description = event.event_description_long
    date = event.event_date
    pub_date = event.pub_date
    event_image = event.event_image
    user_posted = event.event_user
    return render(request, 'board/event_long.html', {'name': name,
                                                     'long_description': long_description,
                                                     'date': date,
                                                     'event_image': event_image,
                                                     'user_posted': user_posted})


'''
def long_description_job(request, job_id):
    """
    A deep dive into a job posting
    Provides the user with a longer description of the job
    """
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
'''


def long_description_musad(request, ad_id):
    """
    A deep dive into a musician's ad
    Provides the user with a longer description of the musician and a link to the musician's profile
    """
    ad = get_object_or_404(Musician_Advertisement, pk=ad_id)
    name = ad.musician_name
    posting_name = ad.posting_name
    long_description = ad.ad_description_long
    start_availability = ad.start_availability
    end_availability = ad.end_availability
    ad_image = ad.ad_image
    name = ad.musician_name
    return render(request, 'board/ad_long.html', {'name': name,
                                                  'posting_name': posting_name,
                                                  'long_description': long_description,
                                                  'start_availability': start_availability,
                                                  'end_availability': end_availability,
                                                  'ad_image': ad_image,
                                                  })

def search_results(request):
    """
    render a page with the search results
    """
    all_posts = Event.objects.all()+Job_Posting.objects.all()+Musician_Advertisement.objects.all()
    context = {
        'all_posts' : all_posts,
    }
    return render(request, 'board/search_results.html', context)
