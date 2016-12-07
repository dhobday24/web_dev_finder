"""
Authentication App views
"""
from django.shortcuts import render
from board.models import *
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

import requests
from authentication.models import UserProfile
from authentication.forms import UserForm, RegistrationForm
from address.models import Address

from geocodio import GeocodioClient

client = GeocodioClient('2f48b44cbca3558fcc7888282c4824b54ce88bf')


def index(request):
    """
    Return the landing page
    """
    events = Event.objects.all()
    ads = Musician_Advertisement.objects.all()
    context = {
        'events': events,
        'ads':ads,
    }
    return render(request, 'index.html', context)


@csrf_exempt
def register(request):
    """
    Register a new user onto the platform
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # address = request.POST.get('address')
            # if address is not "":
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    """
    Render the registration success page
    """
    return render_to_response('registration/success.html')


def logout_page(request):
    """
    logout a user and display the logout page
    """
    logout(request)
    return render_to_response('registration/logout.html')


@login_required
def home(request):
    """
    Render the home page for a logged in user
    """
    address = request.user.userprofile.address
    profile_pic = request.user.userprofile.profile_pic
    soundcloud_username = request.user.userprofile.soundcloud_username
    # print(request.user.userprofile.address)
    return render_to_response('home.html', {'user': request.user, 'pk' : request.user.id, 'profile_pic': profile_pic, 'address': address, 'soundcloud_username': soundcloud_username})


@login_required() # only logged in users should access this
def edit_user(request, pk):
    """
    Update the user profile
    """
    # querying the User object with pk from url
    user = User.objects.get(pk=pk)

    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)

    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(User,
                                                 UserProfile,
                                                 fields=('type_user',
                                                         'address',
                                                         'bio',
                                                         'website',
                                                         'phonenumber',
                                                         'genre',
                                                         'available',
                                                         'profile_pic',
                                                         'soundcloud_username',))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES or None, instance=user)
            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES or None, instance=created_user)
                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/home/')

        return render(request, "registration/update.html", {
            "pk": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied


def update_success(request):
    """
    Render the registration success page
    """
    return render_to_response('registration/update_success.html')


def get_user_profile(request, username):
    current_user = request.user
    print(current_user)
    user = User.objects.get(username=username)
    soundcloud_username = user.userprofile.soundcloud_username
    profile_pic = user.userprofile.profile_pic
    return render(request, 'user_profile.html', {"user":user, 'profile_pic': profile_pic, "current_user":current_user, 'soundcloud_username': soundcloud_username})


def my_events(request):
    current_user = request.user
    all_events = Event.objects.all()
    context = {
        'all_events': all_events,
        'current_user': current_user,
    }
    return render(request, 'my_events.html', context, message=user.id+' has appplied for your events')


def my_ads(request):
    current_user = request.user
    all_ads = Musician_Advertisement.objects.all()
    context = {
        'all_ads': all_ads,
        'current_user': current_user,
    }
    return render(request, 'my_ads.html', context)


def show_applicants_event(request, event_id):
    event = Event.objects.filter(id = event_id).get()
    applications = EventApplication.objects.filter(event_name = event_id)
    context = {
        'applications' : applications
    }
    if request.method == 'POST':
        app_status = request.POST.get('app_status')
        applicant = request.POST.get('applicant')
        if app_status == 'Yes':
            cur_app = EventApplication.objects.get(event_name=event_id, user_who_applied=applicant)
            cur_app.status = True
            cur_app.save()
            event_ref = Event.objects.get(id=event_id)
            event_performer = cur_app.user_who_applied
            performer = UserProfile.objects.get(user_id=event_performer.id)
            performer_number = performer.phonenumber
            payload = {'number': performer_number,
                       'message': "Congratulations! You've been selected to perform at: " + event_ref.event_name +
                                  ". Check out all your other applications to your events on PITCH!"}
            requests.post('http://textbelt.com/text', data=payload)
        else:
            cur_app = EventApplication.objects.filter(event_name = event_id, user_who_applied = applicant).get()
            cur_app.status = False
            cur_app.save()
    return render(request, 'event_applicants.html', context)


def show_applicants_ad(request, ad_id):
    ad = Musician_Advertisement.objects.filter(id = ad_id).get()
    inqueries = AdApplication.objects.filter(ad_name = ad_id)
    context = {
        'inqueries' : inqueries
    }
    if request.method == 'POST':
        app_status = request.POST.get('app_status')
        inquery = request.POST.get('inquery')
        if app_status == 'Yes':
            cur_app = AdApplication.objects.filter(ad_name = ad_id, user_who_applied = inquery).get()
            cur_app.status = True
            cur_app.save()
        else:
            cur_app = AdApplication.objects.filter(ad_name = ad_id, user_who_applied = inquery).get()
            cur_app.status = False
            cur_app.save()
    return render(request, 'ad_applicants.html', context)
