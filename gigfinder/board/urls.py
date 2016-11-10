from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.board, name = 'board'),
    url(r'^events/', views.events, name = 'events'),
    url(r'^job_posts/', views.job_posts, name = 'job_posts'),
    url(r'^talent_ads/', views.musician_ads, name = 'musician_ads'),
    url(r'^events/?P<event_id>[0-9]+/$', views.long_description_event, name = 'long_description_event')

]
