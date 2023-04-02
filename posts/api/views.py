from rest_framework.viewsets import ModelViewSet
from .serializer import PostSerializer
from posts.models import Post
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):

    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer

    # Agregar permisos al endpoint
    # isAdminUser = Solo para administradores
    # IsAuthenticated = Solo para usuarios logueados
    # IsAuthenticatedOrReadOnly = todos pueden leer pero solo los autenticados pueden cambiar
    permission_classes = []

    # metodos permitidos en el modelviewset
    # http_method_names = ['get','post']