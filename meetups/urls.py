from .views import index, meetup_details, confirm_registration
from django.urls import path

urlpatterns = [
    path('meetups/', index, name='all-meetups'),
    path('meetups/<slug:meetup_slug>/success', confirm_registration, name='confirm-registration'),
    path('meetup/<slug:meetup_slug>', meetup_details, name='meetup-details'),
]
