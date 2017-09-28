# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SOS_Detail(models.Model):
	user = models.CharField(max_length=120)
	number1 = models.IntegerField()
	number2 = models.IntegerField()
	number3 = models.IntegerField()