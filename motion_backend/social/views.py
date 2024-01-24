from django.contrib.auth import authenticate, get_user_model
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Post
from .serializers import PostSerializer, UserSerializer

User = get_user_model()


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def token_obtain_pair_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(user_id=user_id)


class ToggleFollowView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        target_user_id = kwargs['user_id']
        target_user_profile = get_object_or_404(User, user_id=target_user_id)

        if request.user in target_user_profile.followers.all():
            target_user_profile.followers.remove(request.user)
        else:
            target_user_profile.followers.add(request.user)

        return Response({'message': 'Follow toggled successfully'})


class FollowersView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_profile = get_object_or_404(User, user_id=user_id)
        return user_profile.followers.all()


class FollowingView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user_profile = get_object_or_404(User, user_id=user_id)
        return user_profile.user.following.all()


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


def landing_view(request):
    return JsonResponse({'message': 'Welcome to Motion API!'})


class TroggleLikeView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post_id = kwargs['post_id']
        target_post = get_object_or_404(Post, pk=post_id)

        if request.user in target_post.likes.all():
            target_post.likes.remove(request.user)
            message = 'Like removed successfully'
        else:
            target_post.likes.add(request.user)
            message = 'Like added successfully'

        return Response({'message': message})
