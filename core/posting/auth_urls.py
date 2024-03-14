from django.urls import path
from .views import login_view
from .views import logout_view
from .viewsets import UserViewSet

urlpatterns = [
    path('auth/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', UserViewSet.signup, name='signup')
]