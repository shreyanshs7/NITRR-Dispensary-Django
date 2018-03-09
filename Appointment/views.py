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

		#send_mail('Appointment Confirmation','Your appointment has been made', settings.EMAIL_HOST_USER , [str(user_obj.email)] , fail_silently=False)
	


		return JsonResponse(data,safe=False)

def show_appointment(request):

	appointment_obj = AppointmentDetail.objects.filter(treated=False)

	user_obj = UserDetail.objects.all()

	medicines = Medicins.objects.all()

	return render(request,'Medz.html',{'users' : user_obj , 'appointments' : appointment_obj, 'medicines': medicines})

@csrf_exempt
def treated(request,id):
		try:

			appointment_obj = AppointmentDetail.objects.get(id=id)

			appointment_obj.treated = True

			appointment_obj.save()

			data = {
			"success": True,
			"message" : "Patient Treated"
			}
		except Exception as e:

			data = {
				'success' : False,
				'message' : "Appointment doesnot exist"
			}	

		return JsonResponse(data,safe=False)


def appointment_api(request):
	
	appointment_obj = AppointmentDetail.objects.all()

	appointment_list = []

	for app in appointment_obj:

		temp_data = {
			"id" : app.id,
			"name" : app.name,
			"medical_issue" : app.medical_issue,
			"issue_type" : app.issue_type,
			"date" : app.date,
			"time" : app.time,
			"treated" : app.treated

		}

		appointment_list.append(temp_data)
		temp_data = {}


	data = {
		"success" : True,
		"appointment_list" : appointment_list
	}	

	return JsonResponse(data,safe=False)

def get_appointment_details(request,id):
	
	appointment_obj = AppointmentDetail.objects.get(id=id)

	appointment_detail = {

			"id" : appointment_obj.id,
			"name" : appointment_obj.name,
			"medical_issue" : appointment_obj.medical_issue,
			"issue_type" : appointment_obj.issue_type,
			"date" : appointment_obj.date,
			"time" : appointment_obj.time,
			"treated" : appointment_obj.treated

	}

	data = {
	"success" : True,
	"appointment_detail" : appointment_detail
	}


	return JsonResponse(data,safe=False)








