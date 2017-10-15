# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from Inventory.models import *
from login_register.models import *
from django.views.decorators.csrf import csrf_exempt
from Dispensary.settings import SECRET_KEY
import jwt
from django.conf import settings
from django.core.mail import send_mail
from .filters import UserFilter


# Create your views here.
@csrf_exempt
def create_appointment(request):
	if request.method == "POST":
		print(request.POST)
		name = request.POST.get('name')
		medical_issue = request.POST.get('medical_issue')
		issue_type = request.POST.get('issue_type')
		
		token = request.POST.get('token')

		jwt_data = jwt.decode(token, settings.SECRET_KEY, algorithm=['HS256'])
		print(jwt_data)

		username = jwt_data['username']

		user_obj = UserDetail.objects.get(username=username)

		

		if issue_type == 'Regular':
			issue_type = 'Regular'

		if issue_type == 'Emergency':
			issue_type = 'Emergency'
			
			
		appointment_obj = AppointmentDetail.objects.create(
			name=name,
			username=user_obj,
			medical_issue=medical_issue,
			issue_type=issue_type
			)

		appointment_obj.save()

		data = {
		'success' : True ,
		'message' : "Appointment made"
		}

		send_mail('Appointment Confirmation','Your appointment has been made', settings.EMAIL_HOST_USER , [str(user_obj.email)] , fail_silently=False)

		return JsonResponse(data,safe=False)

def show_appointment(request):

	appointment_obj = AppointmentDetail.objects.filter(treated=False)

	user_obj = UserDetail.objects.all()

	medicines = Medicins.objects.all()

	return render(request,'Medz.html',{'users' : user_obj , 'appointments' : appointment_obj, 'medicines': medicines})

@csrf_exempt
def treated(request):

	if request.method == "POST":

		app_id = request.POST.get('app_id')

		appointment_obj = AppointmentDetail.objects.get(id=app_id)

		appointment_obj.treated = True

		appointment_obj.save()

		return HttpResponse("Appointment treated")












