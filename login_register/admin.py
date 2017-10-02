from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class UserDetailAdmin(admin.ModelAdmin):
	list_display = ['username','age','mobile_number','email']

admin.site.register(UserDetail,UserDetailAdmin)	
	
