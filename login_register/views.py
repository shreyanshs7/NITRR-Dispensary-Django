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



def register(request):
	if request.method == "POST":

		name = request.POST.get('name')
		username = request.POST.get('username')
		mobile_number = request.POST.get('mobile_number')
		email = request.POST.get('email')
		age = request.POST.get('age')

		data = {
			'username' : username,
			'mobile_number' : mobile_number
		}

		token = jwt.encode(data , SECRET_KEY , algorithms=['HS256'] )

		data = {
			'success' : True ,
			'message' : "User registered",
			'token' : token
		}

		return JsonResponse(data,safe=False)


@csrf_exempt
def detail(request):
	if request.method == "POST":
		
		name = request.POST.get('user')
		
		user_details = AppointmentDetail.objects.filter(username=name)



		user_details_json = serializers.serialize("json",user_details)
		user_details_data = json.loads(user_details_json)
		user_details_list = []


		for data in user_details_data:
			user_details_list.append(data['fields'])

		user_details_api = json.dumps(user_details_list)	
		
		print(user_details_api)	

		return JsonResponse(user_details_api,safe=False)



				
		
		


