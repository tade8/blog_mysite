from rest_framework.mixins import CreateModelMixin, \
    RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Post, Comment
from .serializers import PostSerializer, \
    CommentSerializer, UpdatePostSerializer


class PostView(CreateModelMixin,
               RetrieveModelMixin,
               DestroyModelMixin,
               GenericViewSet
            ):
    queryset = Post.objects.select_related().all()
    serializer_class = PostSerializer


class PostDetailView(ModelViewSet):
    http_method_names = ['post', 'get', 'patch', 'delete']

    def get_serializer_context(self):
        return {'post_id': self.kwargs['post_pk']}

    def get_queryset(self):
        return Comment.objects.filter(
            post_id=self.kwargs['post_pk'])

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdatePostSerializer
        return CommentSerializer
