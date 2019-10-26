# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

class SOS_DetailAdmin(admin.ModelAdmin):
	list_display = ['user','number1','number2','number3']

admin.site.register(SOS_Detail,SOS_DetailAdmin)	