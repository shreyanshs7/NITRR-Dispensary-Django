# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

class AppointmentDetailAdmin(admin.ModelAdmin):
	list_display = ['name','date','time']

admin.site.register(AppointmentDetail,AppointmentDetailAdmin)	