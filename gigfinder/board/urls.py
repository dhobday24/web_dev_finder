from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^events/', views.events, name = 'events')

]
