from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class UserDetailAdmin(admin.ModelAdmin):
	list_display = ['name','username','blood','mobile_number']

admin.site.register(UserDetail,UserDetailAdmin)	
	
