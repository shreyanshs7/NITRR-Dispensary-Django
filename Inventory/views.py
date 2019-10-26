# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
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

@csrf_exempt
def get_medicine_detail(request,id):
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
    # else:
    #     response_json = {
    #         'success' : False,
    #         'message' : 'Method not valid'
    #     }
        return JsonResponse(response_json)

@csrf_exempt
def update_medicine(request,id):
    if request.method == "POST":
        print(request.body)
        #id = request.POST.get('id')
        body = json.loads(request.body)
        quantity = body['quantity']
        price = body['price']
        temp_medicine = Medicins.objects.get(id=id)
        temp_medicine.quantity = quantity
        temp_medicine.price = price
        temp_medicine.save()

        data = {
        'success' : True ,
        'message' : "Medicine updated"
        }

    return JsonResponse(data,safe=False)


def medicine_api(request):

    medicine_obj = Medicins.objects.all()

    medicine_list = []

    for obj in medicine_obj:
        temp_data = {
        "id": obj.id,
        "name":obj.name,
        "price": obj.price,
        "quantity": obj.quantity
        }

        medicine_list.append(temp_data)

        temp_data = {}


    data = {
        "success": True,
        "medicine_list" : medicine_list
    }    


    return JsonResponse(data,safe=False)

