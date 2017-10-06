# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.
def add_medicine(request):
    if request.method == "POST":
        name = request.POST.get('medicine_name')
        quantity = request.POST.get('medicine_quantity')
        price = request.POST.get('medicine_price')
        temp_medicine = Medicins.objects.create(
                name = name,
                quantity = quantity,
                price = price
            )

        temp_medicine.save()

        data = {
        'success' : True ,
        'message' : "Appointment made"
        }

    return redirect('/appointment/show/')

def get_medicine_detail(request):
    if request.method == "POST":
        id = request.POST.get('id')
        temp_medicine = Medicins.objects.get(id=id)
        data = {
            'name' : temp_medicine.name,
            'price' : temp_medicine.price,
            'quantity' : temp_medicine.quantity,
        }
        response_json = {
            'success' : True,
            'medicine' : data
        }
    else:
        response_json = {
            'success' : False,
            'message' : 'Method not valid'
        }
    return JsonResponse(response_json)

def update_medicine(request):
    if request.method == "POST":
        id = request.POST.get('medicine_id')
        quantity = request.POST.get('medicine_quantity')
        price = request.POST.get('medicine_price')
        temp_medicine = Medicins.objects.get(id=id)
        temp_medicine.quantity = quantity
        temp_medicine.price = price
        temp_medicine.save()
        data = {
        'success' : True ,
        'message' : "Appointment made"
        }

    return redirect('/appointment/show/')