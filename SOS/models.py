# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from login_register.models import UserDetail
# Create your models here.
class SOS_Detail(models.Model):
	user = models.ForeignKey('login_register.UserDetail')
	number1 = models.IntegerField()
	number2 = models.IntegerField()
	number3 = models.IntegerField()