from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from posts.models import Post, Group
from .serializers import PostSerializer, CommentSerializer, GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Операция отменена: Вы - не автор!')
        instance.delete()
        
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Операция отменена: Вы - не автор!')
        super().perform_update(serializer)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
    
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Операция отменена: Вы - не автор!')
        instance.delete()
    
    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Операция отменена: Вы - не автор!')
        super().perform_update(serializer)
    
class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
