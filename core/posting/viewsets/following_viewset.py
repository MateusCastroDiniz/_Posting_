from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from ..models import Relation, User
from django.shortcuts import render
from ..serializers import RelationSerializer


class FollowingViewSet(viewsets.ModelViewSet):
    serializer_class = RelationSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

def user_following(request):
    following = list(map(lambda x: x.followed.username, Relation.objects.filter(follower=User.objects.get(pk=request.user.pk))))
    context = {
        'following': following
    }
    return render(request, 'following.html', context)


