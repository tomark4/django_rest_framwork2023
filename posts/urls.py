from rest_framework.routers import DefaultRouter

# from posts.api.view import PostViewSet
from posts.api.views import PostModelViewSet

router = DefaultRouter()

router.register(prefix="posts", basename='posts',viewset=PostModelViewSet)