# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import urllib2
# Create your views here.

def send_sos(request):
	if request.method == "POST":

		auth_key = "176332A81pH4L759c8aad6"

		sos_obj = SOS_Detail.objects.get(user=request.user)

		number1 = sos_obj.number1
		number2 = sos_obj.number2
		number3 = sos_obj.number3

		sender = request.user

		#location = something

		#message = ""

		send_sos_url = "https://control.msg91.com/api/sendhttp.php?authkey="+auth_keys+"&mobiles=91"+str(number1)+",91"+str(number2)+",91"+str(number3)+"&message="+str(message)+"&sender="+str(sender)+"&route=4&country=91"

		response = urllib2.urlopen(send_sos_url).read()

		return HttpResponse(response)