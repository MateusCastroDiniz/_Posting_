from django.urls import path, include
from rest_framework import routers
from .viewsets import user_viewset, post_viewset,comment_viewset
from .viewsets import *
from .viewsets.post_viewset import *
from .views import *

CommentRouter = routers.SimpleRouter()
CommentRouter.register(r"comments", CommentViewSet, basename='comments')

PostRouter = routers.SimpleRouter()
PostRouter.register(r"posts", PostViewSet, basename='posts')

UserRouter = routers.SimpleRouter()
UserRouter.register(r"account", UserViewSet, basename='account')

urlpatterns = [
    path('', include(CommentRouter.urls)),
    path('', include(PostRouter.urls)),
    path('', include(UserRouter.urls)),
    path('', landingpage_view, name=''),
    path('user/', user_viewset.user_config, name='user'),
    path('user/edit/<str:username>', user_viewset.edit_user, name='edit_user'),
    path('user/edit/img/profile_picture', user_viewset.edit_profile_picture, name='edit_profile_picture'),
    path('user/edit/img/remove_profipic/', user_viewset.delete_profile_picture, name='remove_profipic'),
    path('feed/explore', explore_list, name='explore'),
    path('feed/', post_list, name='feed'),
    path('feed/p/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('feed/create/', PostViewSet.create_post, name='create_post'),
    path('feed/<slug:slug>/update/', PostViewSet.as_view({'post': 'update_post'}), name='update_post'),
    path('feed/<slug:slug>/delete/', PostViewSet.delete_post, name='delete_post'),
]
