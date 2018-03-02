from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
		url(r'^register/$' , register , name = 'register'),
		url(r'^detail/$' , detail , name = 'detail'),
		url(r'^detail_angular/(?P<id>\d+)/$' , detail_angular ),
		url(r'^login/', login , name='login'),
		url(r'^api/$' , users_api)
		#url(r'^login_check/', login_check , name='login_check'),
]
