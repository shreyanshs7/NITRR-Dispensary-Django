from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^create/$' , create_appointment , name = 'create_appointment'),
	url(r'^show/$' , show_appointment , name = 'show_appointment'),
	url(r'^treated/(?P<id>\d+)/$' , treated , name = 'treated'),
	url(r'^api/$' , appointment_api ),
	url(r'^api/(?P<id>\d+)/$' , get_appointment_details ),
	
	
	
]