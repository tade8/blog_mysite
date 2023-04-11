from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'comment_body']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
