from django.conf.urls import include, url
from django.contrib import admin
from authentication import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='register_success'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout_page, name='logout_page'),
    url(r'^home/$', views.home, name='home'),
]
