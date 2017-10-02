# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import urllib2
import random
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def send_otp(request):
	if request.method == "POST":

		auth_key = "176332A81pH4L759c8aad6"
		sender_id = "CodeCSE"
		mobile_number = request.POST.get("number")
		otp = random.randint(2000,9999)

		send_otp_url = "https://control.msg91.com/api/sendotp.php?authkey="+auth_key+"&mobile=91"+str(mobile_number)+"&message=Your%20otp%20is%20"+str(otp)+"&sender="+sender_id+"&otp="+str(otp)+""

		response = urllib2.urlopen(send_otp_url).read()

		if response['type'] == 'success':
			data = {
				'success' : True,
				'message' : "OTP sent successfully"
			}		

		else:
			data = {
				'success' : False,
				'message' : "OTP not sent"
			}



		return JsonResponse(data,safe=False)


@csrf_exempt
def verify_otp(request):
	if request.method == "POST":

		otp = request.POST.get("otp")
		auth_key = "176332A81pH4L759c8aad6"
		mobile_number = request.POST.get("number")

		verify_otp_url = "https://control.msg91.com/api/verifyRequestOTP.php?authkey="+auth_key+"&mobile=91"+mobile_number+"&otp="+str(otp)+""

		response = urllib2.urlopen(verify_otp_url).read()

		if response['type'] == 'success':
			data = {
				"success" : True,
				"message" : "Number verified"
			}

		else:
			data = {
				"success" : False,
				"message" : "Number verification failed"
			} 	

		return JsonResponse(data,safe=False)
