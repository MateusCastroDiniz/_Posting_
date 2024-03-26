from django.urls import path
from .views import *
from .viewsets import UserViewSet


urlpatterns = [
    path('login', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', UserViewSet.signup, name='signup'),
    # path('edit/', user_edit_view.as_view(), name='edit_user')
]