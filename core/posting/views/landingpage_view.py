from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from ..models.user import User

def landingpage_view(request):
    return render(request, 'landingpage.html')
        