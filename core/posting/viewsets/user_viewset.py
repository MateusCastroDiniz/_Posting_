from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from ..models import User
from django.shortcuts import render
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)


def user_config(request):
    user = request.user

    context = {
        'user_info': {
            'first_name': user.username,
            'email': user.email
        }
    }
    return render(request, 'user_config.html', context)
