from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from ..models import User, Relation
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
    followers = list(map(lambda x: x.follower.username, Relation.objects.filter(followed=User.objects.get(pk=request.user.pk))))
    following = list(map(lambda x: x.followed.username, Relation.objects.filter(follower=User.objects.get(pk=request.user.pk))))


    context = {
        'user_info': {
            'first_name': user.username,
            'email': user.email,
            'followers': followers,
            'following': following
        }
    }
    return render(request, 'profile.html', context)
