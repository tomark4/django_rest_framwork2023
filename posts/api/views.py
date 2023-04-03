from rest_framework.viewsets import ModelViewSet
from .serializer import PostSerializer, PostCreateSerializer
from posts.models import Post
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class PostModelViewSet(ModelViewSet):

    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
    lookup_field = 'slug'
    # Agregar permisos al endpoint
    # isAdminUser = Solo para administradores
    # IsAuthenticated = Solo para usuarios logueados
    # IsAuthenticatedOrReadOnly = todos pueden leer pero solo los autenticados pueden cambiar
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__slug','category']
    # metodos permitidos en el modelviewset
    # http_method_names = ['get','post']

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return PostCreateSerializer
        return PostSerializer