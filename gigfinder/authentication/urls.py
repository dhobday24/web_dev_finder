from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from authentication import views

urlpatterns = [
    url(r'^register/$', auth_views.register, name='register')
    url(r'^login/$', auth_views.user_login, name='login'),
    url(r'^logout/$', auth_views.user_logout, name='logout'),
    ]