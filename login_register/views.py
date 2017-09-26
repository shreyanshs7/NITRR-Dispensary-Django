from __future__ import unicode_literals
from django.shortcuts import render
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json


@csrf_exempt
def UserProfileCreationAPIView(request):
	if request.method == 'POST':
		print request.POST
		return JsonResponse(request.POST, safe=False)

