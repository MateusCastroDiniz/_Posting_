from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from ..models import Relation, User
from django.shortcuts import render
from ..serializers import RelationSerializer


class FollowersViewSet(viewsets.ModelViewSet):
    serializer_class = RelationSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

def user_followers(request):
    followers = list(map(lambda x: x.follower.username, Relation.objects.filter(followed=User.objects.get(pk=request.user.pk))))
    context = {
        'followers': followers
    }
    return render(request, 'follower.html', context)
