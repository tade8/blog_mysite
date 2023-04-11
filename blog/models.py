from uuid import uuid4
from django.db import models


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.PROTECT,
                             related_name='comments')
    comment_body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_body
