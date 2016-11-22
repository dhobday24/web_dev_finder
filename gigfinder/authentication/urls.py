from django.conf.urls import include, url
from django.contrib import admin
from authentication import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
]
