from django.urls import path, include
from rest_framework import routers
from .viewsets import user_viewset,post_viewset,comment_viewset
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
    path('user/edit', UserViewSet.edit_user, name='user_edit'),
    path('feed/explore', explore_list, name='explore'),
    path('feed/', post_list, name='feed'),
    path('feed/p/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('feed/create/', PostViewSet.create_post, name='create_post'),
    path('feed/<slug:slug>/edit/', edit_post_view, name='edit_post'),
    path('feed/<slug:slug>/update/', PostViewSet.as_view({'post': 'update_post'}), name='update_post'),
    path('feed/<slug:slug>/delete', PostViewSet.delete_post, name='delete_post'),
    # path('feed/<slug:slug>/update', PostViewSet.as_view({'put': 'update'}), name='update_post')
    # path('feed/create', PostViewSet.create_post, name='create_post'),
    # path('feed/<slug:slug>/edit', PostViewSet.edit_post, name='edit_post')
]
