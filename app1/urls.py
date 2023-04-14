from django.urls import path
from app1.views import *

app_name='something'

urlpatterns=[
    path('corosals/',corosals,name='corosals'),
]