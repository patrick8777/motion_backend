from rest_framework import serializers

from user.models import CustomUser
from .models import Post

User = CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'


