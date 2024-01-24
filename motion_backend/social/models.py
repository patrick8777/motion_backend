from django.contrib.auth import get_user_model

from django.db import models

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.TextField()
    likes = models.ManyToManyField(to=User, related_name='liked_posts', blank=True)
