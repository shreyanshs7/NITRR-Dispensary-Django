from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^create/$' , create_appointment , name = 'create_appointment'),
	url(r'^show/$' , show_appointment , name = 'show_appointment'),
	url(r'^treated/$' , treated , name = 'treated'),
	
	
]