from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^add', add_medicine , name = 'add_medicine'),
    url(r'^update', update_medicine , name = 'update_medicine'),
    url(r'^get_medicine_detail', get_medicine_detail , name = 'get_medicine_detail'),
	# url(r'^show/$' , show_appointment , name = 'show_appointment'),		
]