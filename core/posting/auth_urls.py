from django.urls import path
from .views import login_view

urlpatterns = [
    path('auth/', login_view, name='login'),
]