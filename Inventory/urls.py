from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^add', add_medicine , name = 'add_medicine'),
    url(r'^update/(?P<id>\d+)$', update_medicine , name = 'update_medicine'),
    url(r'^get_medicine_detail/(?P<id>\d+)/$', get_medicine_detail , name = 'get_medicine_detail'),
    url(r'^api/$', medicine_api ),
	# url(r'^show/$' , show_appointment , name = 'show_appointment'),		
]