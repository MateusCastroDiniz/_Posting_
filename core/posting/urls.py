from django.urls import path, include
from rest_framework import routers
from .viewsets import user_viewset,post_viewset,comment_viewset
from .viewsets import *
from .viewsets.post_viewset import *
from .views import *

CommentRouter = routers.SimpleRouter()
CommentRouter.register(r"comments", CommentViewSet, basename='comments')

PostRouter = routers.SimpleRouter()
PostRouter.register(r"feed", PostViewSet, basename='feed')

UserRouter = routers.SimpleRouter()
UserRouter.register(r"account", UserViewSet, basename='account')

urlpatterns = [
    # path('', include(CommentRouter.urls)),
    # path('', include(PostRouter.urls)),
    # path('', include(UserRouter.urls)),
    path('', landingpage_view, name=''),
    path('profile/', user_viewset.user_config, name='profile'),
    path('profile/edit', UserViewSet.edit_user, name='profile_edit'),
    path('feed/', post_list, name='feed'),
    path('feed/explore', explore_list, name='explore'),
    path('feed/p/<slug:slug>/detailed', PostDetail.as_view(), name='post_detail'),
    path('feed/<slug:slug>/edit', PostViewSet.edit_post, name='edit_post')
]
