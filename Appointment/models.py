# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class AppointmentDetail(models.Model):
	EMERGENCY = 'EG'
	REGULAR = 'RG'
	ISSUE_TYPE = (
		(EMERGENCY,'Emergency'),
		(REGULAR,'Regular'),
		)

	name = models.CharField(max_length=120,blank=False)
	medical_issue = models.CharField(max_length=200,blank=False)
	issue_type = models.CharField(max_length=120,choices=ISSUE_TYPE)
	date = models.DateField(auto_now=True)
	time = models.TimeField(auto_now=True)