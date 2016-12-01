from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.board, name='board'),
    url(r'^events/$', views.events, name='events'),
    url(r'^job_posts/$', views.job_posts, name='job_posts'),
    url(r'^talent_ads/$', views.musician_ads, name='musician_ads'),
    url(r'^events/(?P<event_id>[0-9]+)/$',
        views.long_description_event, name='long_description_event'),
    url(r'^job_posts/(?P<job_id>[0-9]+)/$',
        views.long_description_job, name='long_description_job'),
    url(r'^talent_ads/(?P<ad_id>[0-9]+)/$',
        views.long_description_musad, name='long_description_musad'),
    url(r'^event_submit/$', views.event_submit, name='event_submit'),
    url(r'^job_submit/$', views.job_submit, name='job_submit'),
    url(r'^ad_submit/$', views.ad_submit, name='ad_submit'),

]
