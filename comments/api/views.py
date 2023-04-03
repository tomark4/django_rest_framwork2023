from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from .serializer import CommentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOwnerOrReadAndCreateOnly


class CommentsApiViewSet(ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  filter_backends  = [OrderingFilter, DjangoFilterBackend]
  permission_classes = [IsOwnerOrReadAndCreateOnly]
  ordering = ['-created']
  filterset_fields = ['post']