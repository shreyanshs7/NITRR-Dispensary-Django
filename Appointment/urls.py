from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^create/$' , create_appointment , name = 'create_appointment'),
	
]