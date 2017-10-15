from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator

	

class UserDetail(models.Model):
	name = models.CharField(max_length=120)
	username = models.CharField(max_length=120)
	mobile_number = models.IntegerField()
	blood = models.CharField(max_length=12,default="A+")
	email = models.EmailField(default="shreyanshss7@gmail.com")

	def __str__(self):
		return self.username