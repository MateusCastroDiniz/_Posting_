from django.urls import path
from .views import login_view
from .views import logout_view

urlpatterns = [
    path('auth/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]