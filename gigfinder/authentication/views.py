"""
Authentication App views
"""
from django.shortcuts import render

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

from authentication.models import UserProfile
from authentication.forms import UserForm, RegistrationForm


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
                                                         'location',
                                                         'bio',
                                                         'website',
                                                         'phonenumber',
                                                         'genre',
                                                         'available'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return HttpResponseRedirect('/accounts/profile/')

        return render(request, "registration/update.html", {
            "noodle": pk,
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied
