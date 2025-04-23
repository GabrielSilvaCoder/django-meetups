from .views import index, meetup_details
from django.urls import path

urlpatterns = [
    path('meetups/', index, name='all-meetups'),
    path('meetup/<slug:meetup_slug>', meetup_details, name='meetup-details')
]
