from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action
from django.shortcuts import render, redirect, get_object_or_404
from ..models import Relation, User
from ..serializers import RelationSerializer


class RelationViewSet(viewsets.ModelViewSet):
    serializer_class = RelationSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @classmethod
    @action(detail=True, methods=['post'])

    def follow_user(self, request, username):
        follower = request.user
        followed = User.objects.get(username=username)
        if request.method == 'POST':
            relation = Relation.objects.create(follower=follower, followed=followed)
            relation.save()
            return redirect('user_detail', username=username)
        return render(request, 'user_detail.html')
    
    @classmethod
    @action(detail=True, methods=['post'])
    def unfollow_user(self, request, username):
        follower = request.user
        unfollow_user = User.objects.get(username=username)
        if request.method == 'POST':
            relation = Relation.objects.get(follower=follower, followed=unfollow_user)
            relation.delete()
            return redirect('user_detail', username=username)
        return render(request, 'user_detail.html')

def user_following(request):
    following = list(map(lambda x: x.followed.username, Relation.objects.filter(follower=User.objects.get(pk=request.user.pk))))

    context = {
        'following': following
    }
    return render(request, 'friends_list.html', context)


def user_list(request):
    user_list = User.objects.all()
    following = list(map(lambda x: x.followed.username, Relation.objects.filter(follower=User.objects.get(pk=request.user.pk))))

    search = request.GET.get('search')

    if search:
        user_list = User.objects.filter(username__icontains=search)

    context = {'user_list': user_list, 'following': following}
    return render(request, 'find_friend.html', context=context)