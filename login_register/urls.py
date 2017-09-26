from django.conf.urls import url
from .views import (
		UserProfileCreationAPIView,
		UserProfileDetailAPIView,
		UserProfileDeleteAPIView,
		UserProfileUpdateAPIView,

	)


urlpatterns = [
	url(r'^registeration/$' , UserProfileCreationAPIView , name = 'UserProfileCreationAPIView'),
	url(r'^detail/$' , UserProfileDetailAPIView , name = 'UserProfileDetailAPIView'),
	url(r'^delete/$' , UserProfileDeleteAPIView , name = 'UserProfileDeleteAPIView'),
	url(r'^update/$' , UserProfileUpdateAPIView , name = 'UserProfileDeleteAPIView'),
]
