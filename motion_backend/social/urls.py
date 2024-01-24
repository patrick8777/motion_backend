from django.urls import path

from .views import (
    PostListCreateView,
    PostDetailView,
    UserPostsView,
    ToggleFollowView,
    FollowersView,
    FollowingView,
    UserListView,
    landing_view, TroggleLikeView,
)

urlpatterns = [
    path('', landing_view, name='landing'),
    path('social/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('social/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/troggle-like/', TroggleLikeView.as_view(), name='troggle-like'),
    # path('social/posts/likes/', LikesView.as_view(), name='post-likes'),
    path('social/posts/user/<int:user_id>/', UserPostsView.as_view(), name='user-posts'),
    path('social/followers/toggle-follow/<int:user_id>/', ToggleFollowView.as_view(), name='toggle-follow'),
    path('social/followers/followers/<int:user_id>/', FollowersView.as_view(), name='followers'),
    path('social/followers/following/<int:user_id>/', FollowingView.as_view(), name='following'),
    path('users/', UserListView.as_view(), name='user-list'),
]
