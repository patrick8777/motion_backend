from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

User = CustomUser


class FollowAdmin(admin.ModelAdmin):
    list_display = ['follower', 'followee']


class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Groups', {'fields': ('groups',)}),
    )
    readonly_fields = ['date_joined']
    list_display = ['email', 'id', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'get_followers_count',
                    'get_posts_count']
    ordering = ['email']

    def get_followers_count(self, obj):
        return obj.followers.count()

    get_followers_count.short_description = 'Followers Count'

    def get_posts_count(self, obj):
        return obj.post_set.count()

    get_posts_count.short_description = 'Posts Count'

    def get_like_count(self, obj):
        return obj.liked_posts.count()

    get_like_count.short_description = 'Liked Posts Count'


# Register your models here.
admin.site.register(CustomUser)
