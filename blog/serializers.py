from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'comment_body', 'time_created']

    def create(self, validated_data):
        post_id = self.context['post_id']
        return Comment.objects.create(post_id=post_id,
                                      **validated_data)


class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at', 'comments']


class UpdatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['comment_body']
