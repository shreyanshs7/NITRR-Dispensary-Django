# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import urllib2
from Dispensary.settings import SECRET_KEY
import jwt
from django.conf import settings
from login_register.models import UserDetail
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def send_sos(request):
	if request.method == "POST":
		print(request.POST)
		auth_keys = "176332A81pH4L759c8aad6"

		token = request.POST.get('token')
		address = request.POST.get('address')
		jwt_data = jwt.decode(token, settings.SECRET_KEY, algorithm=['HS256'])

		print(jwt_data)

		sender = jwt_data['username']

		user_obj = UserDetail.objects.get(username=sender)

		sos_obj = SOS_Detail.objects.get(user=user_obj)

		number1 = sos_obj.number1
		number2 = sos_obj.number2
		number3 = sos_obj.number3

		

		#location = something
		

		message = "This is a test message from "+str(user_obj.name)+" "+str(address)+""

		send_sos_url = "https://control.msg91.com/api/sendhttp.php?authkey="+auth_keys+"&mobiles=91"+str(number1)+",91"+str(number2)+",91"+str(number3)+"&message="+str(message)+"&sender=SOSSOS&route=4&country=91"

		response = urllib2.urlopen(send_sos_url).read()

		print(response)

		data = {
		"success" : True,
		"message" : "SOS sent"
		}

		return JsonResponse(data,safe=False)