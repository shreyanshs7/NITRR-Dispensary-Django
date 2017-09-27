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

@csrf_exempt
def UserProfileUpdateAPIView(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		jwt_token = data.pop('token')
		token_payload = jwt.decode(jwt_token , 'secret_key' , algorithm = 'HS256')
		username = token_payload['user']['username']
		user = User.objects.get(username = username)
		old_password = data['user'].pop('old_password')
		new_password = False;
		if user.check_password(old_password):
			user_fields = data.pop('user')
			user_fields_keys = user_fields.keys()
			profile_fields_keys = data.keys()
			if 'username' in user_fields_keys:
				return HttpResponse('Username cannot be changed!')
			
			if 'password' in user_fields_keys:
				new_password = user_fields.pop('password')
				user.set_password(new_password)
				user_fields_keys.remove('password')
			
			for key in user_fields_keys:
				setattr(user , key , user_fields[key])
			
			for key in profile_fields_keys:
				setattr(user.profile , key , data[key])
			user.save()
			user.profile.save()

			user_dict = {}
			user_dict['user']={}
			user_dict['user']['username'] = user.username
			user_dict['user']['email'] = user.email
			user_dict['user']['first_name'] = user.first_name
			user_dict['user']['last_name'] = user.last_name
			user_dict['mobileNumber']=user.profile.mobileNumber
			if new_password:
				user_dict['user']['password'] = new_password
			else:
				user_dict['user']['password'] = old_password

			data_encode = json.loads(json.dumps(user_dict))
			new_token = jwt.encode(data_encode ,'secret_key' , algorithm = 'HS256')

			return HttpResponse(new_token)

		


		


			




				
		
		


