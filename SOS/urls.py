from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^send/$' , send_sos , name = 'send_sos'),
	
]