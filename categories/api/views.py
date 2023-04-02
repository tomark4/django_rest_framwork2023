from categories.models import Category
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class CategoryApiViewSet(ModelViewSet):
  serializer_class = CategorySerializer
  permission_classes = [IsAdminOrReadOnly]
  queryset = Category.objects.all()
  # filter queryset by default
  # queryset = Category.objects.filter(published=True)
  lookup_field = 'slug'
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ('published',)



