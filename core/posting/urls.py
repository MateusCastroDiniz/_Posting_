from django.urls import path, include
from rest_framework import routers
from .viewsets import user_viewset,post_viewset,comment_viewset
from .viewsets import *
from .viewsets.post_viewset import post_list

CommentRouter = routers.SimpleRouter()
CommentRouter.register(r"comments", CommentViewSet, basename='comments')

# PostRouter = routers.SimpleRouter()
# PostRouter.register(r"feed", PostViewSet, basename='feed')

UserRouter = routers.SimpleRouter()
UserRouter.register(r"account", UserViewSet, basename='account')

urlpatterns = [
    path('', include(CommentRouter.urls)),
    path('', include(UserRouter.urls)),
    path('profile/', user_viewset.user_config, name='profile'),
    path('feed/', post_list, name='feed')
]
