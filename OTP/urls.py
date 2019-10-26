from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^send/$' , send_otp , name = 'send_otp'),
	url(r'^verify/$' , verify_otp , name = 'verify_otp'),
]