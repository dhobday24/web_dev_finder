"""
URL routes for the authentication app
"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib import admin
from authentication import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^home/$', views.home, name='home'),
    url(r'^home/profile/(?P<pk>[0-9]+)/$', views.edit_user, name='edit_user'),
    url(r'^home/update_success/(?P<pk>[0-9]+)/$', views.edit_user, name='edit_user'),
]
