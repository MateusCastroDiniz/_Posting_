from django.urls import path, include
from rest_framework import routers
from .viewsets import *
from .views import login_view
from .viewsets.post_viewset import post_list

urlpatterns = [
    path('auth/', login_view, name='login'),
]