from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import RegexValidator



def get_upload_url(instance , filename):
	return 'UserProfileImages/%s/%s'%(instance.user.username , filename)


class  UserProfile(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE , primary_key = True , related_name = 'profile')
	mobileNumber = models.IntegerField(default = 0)
	avatar = models.ImageField(upload_to = get_upload_url , default = '/static/UserProfile/defaultProfileImage.png' )



def create_user_profile(sender , **kwargs):
	if kwargs['created']:
		profile = UserProfile.objects.create(user = kwargs['instance'])


post_save.connect(create_user_profile, sender = User)