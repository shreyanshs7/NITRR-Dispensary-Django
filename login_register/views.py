from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import UserProfile
from django.http import HttpResponse
import json
import jwt


@csrf_exempt
def UserProfileCreationAPIView(request):
	if request.method == 'POST':
		data = json.loads(request.body)

		
		username = data['user']['username']
		password = data['user']['password']
		email = data['user']['email']
		first_name = data['user']['first_name']
		last_name = data['user']['last_name']
		mobileNumber = data['mobileNumber']

		jwt_encode = jwt.encode(data , 'secret_key' , algorithm = 'HS256')

		user = User.objects.create_user(username = username , password = password , email = email)
		user.first_name = first_name
		user.last_name = last_name
		user.save()
		user_profile = UserProfile()
		user_profile.user = user
		user_profile.mobileNumber = mobileNumber
		user_profile.save()



		return HttpResponse(jwt_encode)




@csrf_exempt
def UserProfileDetailAPIView(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		jwt_token = data.pop('token')
		token_payload = jwt.decode(jwt_token , 'secret_key' , algorithm = 'HS256')
		return HttpResponse(str(token_payload))

@csrf_exempt
def UserProfileDeleteAPIView(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		jwt_token = data.pop('token')
		token_payload = jwt.decode(jwt_token , 'secret_key' , algorithm = 'HS256')
		username = token_payload['user']['username']
		user = User.objects.get(username = username)
		user.delete()
		return HttpResponse("User Deleted Successfully")


		


			




				
		
		


