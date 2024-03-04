from django.urls import path, include
from rest_framework import routers
from .viewsets import *
from .views import login_view
from .viewsets.post_viewset import post_list

CommentRouter = routers.SimpleRouter()
CommentRouter.register(r"comments", CommentViewSet, basename='comments')

PostRouter = routers.SimpleRouter()
PostRouter.register(r"feed", PostViewSet, basename='feed')

UserRouter = routers.SimpleRouter()
UserRouter.register(r"account", UserViewSet, basename='user')

urlpatterns = [
    path('', include(CommentRouter.urls)),
    path('', include(UserRouter.urls)),
    path('', include(PostRouter.urls)),
    path('feed/', post_list, name='post_list')
]
