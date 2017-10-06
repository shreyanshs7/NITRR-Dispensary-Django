# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from Inventory.models import *
from login_register.models import *

# Create your views here.
def create_appointment(request):
	if request.method == "POST":
		name = request.POST.get('name')
		medical_issue = request.POST.get('medical_issue')
		issue_type = request.POST.get('issue_type')

		if issue_type == 'Regular':
			issue_type = 'RG'

		if issue_type == 'Emergency':
			issue_type = 'EG'
			

		appointment_obj = AppointmentDetail.objects.create(
			name=name,
			medical_issue=medical_issue,
			issue_type=issue_type
			)

		appointment_obj.save()

		data = {
		'success' : True ,
		'message' : "Appointment made"
		}

		return JsonResponse(data,safe=False)

def show_appointment(request):

	appointment_obj = AppointmentDetail.objects.all()

	user_obj = UserDetail.objects.all()

	medicines = Medicins.objects.all()

	return render(request,'Medz.html',{'users' : user_obj , 'appointments' : appointment_obj, 'medicines': medicines})



