from django.conf.urls import url
from .views import (
		UserProfileCreationAPIView,
	)


urlpatterns = [
	url(r'^registeration/$' , UserProfileCreationAPIView , name = 'UserProfileCreationAPIView'),
]