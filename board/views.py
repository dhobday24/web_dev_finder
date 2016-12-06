"""
Views for the board app
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required


from address.models import Address
from .models import Event, Musician_Advertisement, EventApplication, AdApplication
from .forms import EventForm, AdForm
from geocodio import GeocodioClient
#from board.models import Job_Posting
#from board.forms import JobForm

client = GeocodioClient('2f48b44cbca3558fcc7888282c4824b54ce88bf')

# Create your views here.


@login_required
def board(request):
    """
    Let a logged in user see the board page
    """
    user = request.user
    return render(request, 'board/board.html')


def event_submit(request):
    """
    Allows for the submission for a one-time event listing
    """
    form_event = EventForm(request.POST or None, request.FILES or None)
    if form_event.is_valid():
        instance = form_event.save(commit=False)
        instance.event_user = request.user
        event_lat_long = client.geocode(instance.event_address)
        event_lat_long = event_lat_long.coords
        instance.event_lat = event_lat_long[0]
        instance.event_long = event_lat_long[1]
        instance.save()
        # instance.save()
        return redirect('board')
    context = {
        'form_event': form_event,
    }
    return render(request, 'board/event_submit.html', context)


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
    #print(all_events.event_name)
    context = {
        'all_events': all_events,
    }
    return render(request, 'board/event_board.html', context)


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
    browsing_userid = request.user.id
    event_lat = event.event_lat
    event_long = event.event_long
    app = EventApplication.objects.filter(event_name = event.id, user_who_applied=request.user)
    all_apps = EventApplication.objects.filter(event_name = event.id)
    event_booked = False
    for single_app in all_apps:
        if single_app.status == True:
            event_booked = True


    print(all_apps)

    return render(request, 'board/event_long.html', {'name': name,
                                                     'event': event,
                                                     'long_description': long_description,
                                                     'date': date,
                                                     'event_image': event_image,
                                                     'user_posted': user_posted,
                                                     'browser_id': browsing_userid,
                                                     'event_lat': event_lat,
                                                     'event_long': event_long,
                                                     'app': app,
                                                     'event_booked': event_booked,
                                                     })


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
    app = AdApplication.objects.filter(ad_name = ad.id, user_who_applied=request.user)
    return render(request, 'board/ad_long.html', {'name': name,
                                                  'ad': ad,
                                                  'posting_name': posting_name,
                                                  'long_description': long_description,
                                                  'start_availability': start_availability,
                                                  'end_availability': end_availability,
                                                  'ad_image': ad_image,
                                                  'app': app,
                                                  })

# ef search_results(request):
#     """
#     render a page with the search results
#     """
#     query = request.GET.get('q')
#     all_posts = Event.objects.all().filter(Event.event_name=query)
#     all_ads = Musician_Advertisement.objects.all().filter(Musician_Advertisement.posting_name=query)
#
#     context = {
#         'all_posts' : all_posts,
#         'all_ads': all_ads,
#     }

def search_results(request):
    """
    render a page with the search results
    """

    query = request.GET.get('search')
    all_posts = Event.objects.filter(event_name = query)
    all_ads = Musician_Advertisement.objects.filter(posting_name=query)
    context = {
        'all_posts' : all_posts,
        'all_ads': all_ads,
    }
    print(query)
    if query:
        all_posts = Event.objects.filter(event_name = query)
        all_ads = Musician_Advertisement.objects.filter(posting_name=query)
        return render(request, 'board/search_results.html', context)
    return render(request, 'board/search_results.html', context)


def apply_for_event(request):
    if request.method == 'POST':
        app_id = request.POST.get("app_event")
        username = request.user
        application = EventApplication.objects.create(user_who_applied=username, event_name = Event.objects.filter(id = app_id).get())
    return render(request, 'board/apply_for_event.html')

def request_musician(request):
    if request.method == 'POST':
        app_id = request.POST.get("app_ad")
        username = request.user
        print(app_id)
        application = AdApplication.objects.create(user_who_applied=username, ad_name = Musician_Advertisement.objects.filter(id = app_id).get())
    return render(request, 'board/apply_for_ad.html')


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
