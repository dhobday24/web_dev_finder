from django.shortcuts import render

# Create your views here.
from authentication.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from board.models import *

def index(request):
    """
    Return the landing page
    """
    return render(request, 'index.html')


@csrf_exempt
def register(request):
    """
    Register a new user onto the platform
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
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
    return render_to_response('home.html', {'user': request.user, 'pk' : request.user.id})

