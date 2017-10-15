from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from Dispensary.settings import SECRET_KEY
from django.http import HttpResponse,JsonResponse
import json
import jwt
from Appointment.models import *
from django.core import serializers
from .models import *
import random
import urllib2
from django.contrib.auth import authenticate


@csrf_exempt
def login(request):
	if request.method == "POST":

		username = request.POST.get("username")
		password = request.POST.get("password")

		#user = authenticate(username=username, password=password)

		user = User.objects.get(username=username)

		if user.check_password(password): 

			user_detail_obj = UserDetail.objects.get(username=user)

			mobile_number = user_detail_obj.mobile_number

			jwt_data = {
				'username' : user.username,
				'mobile_number' : mobile_number
		     }

		   	token = jwt.encode(jwt_data , SECRET_KEY , algorithm='HS256')

			

			data = {
				"success" : True,
				"message" : "User authenticated",
				'token' : token
			}

			return JsonResponse(data,safe=False)
		else:
			
			data = {
				"success" : False,
				"message" : "Invalid credentials"
 			}

 			return JsonResponse(data,safe=False)

		

		


@csrf_exempt
def register(request):
	if request.method == "POST":

		name = request.POST.get('name')
		username = request.POST.get('username')
		mobile_number = request.POST.get('mobile_number')
		password = request.POST.get('password')
		blood = request.POST.get('blood')

		if User.objects.filter(username=username).exists():
			data = {
			"success" : False,
			"message" : "Username already exists"
			}

			return JsonResponse(data,safe=False)

		else:

			user_detail = UserDetail.objects.create(
				name=name,
				username=username,
				mobile_number=mobile_number,
				blood=blood
				)
			user_detail.save()

			user_obj = User.objects.create_user(
				username=username,
				password=password
				)
			user_obj.save()


			auth_key = "176332A81pH4L759c8aad6"
			sender_id = "CodeCSE"
			otp = random.randint(2000,9999)

			send_otp_url = "https://control.msg91.com/api/sendotp.php?authkey="+auth_key+"&mobile=91"+str(mobile_number)+"&message=Your%20otp%20is%20"+str(otp)+"&sender="+sender_id+"&otp="+str(otp)+""

			response = urllib2.urlopen(send_otp_url).read()



			jwt_data = {
				'username' : username,
				'mobile_number' : mobile_number
			}

			token = jwt.encode(jwt_data , SECRET_KEY , algorithm='HS256' )

			data = {
				'success' : True ,
				'message' : "User registered",
				'token' : token
			}

			return JsonResponse(data,safe=False)


@csrf_exempt
def detail(request):
	if request.method == "POST":
		
		user_id = request.POST.get('user_id')
		
		user_obj = UserDetail.objects.get(id=user_id)

		user_details = AppointmentDetail.objects.filter(username=user_obj)



		user_details_json = serializers.serialize("json",user_details)
		user_details_data = json.loads(user_details_json)
		user_details_list = []


		for data in user_details_data:
			user_details_list.append(data['fields'])

		user_details_api = json.dumps(user_details_list)	
		
		print(user_details_api)	

		return JsonResponse(user_details_api,safe=False)



				
		
		


