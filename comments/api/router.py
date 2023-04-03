from rest_framework.routers import DefaultRouter
from .views import CommentsApiViewSet

router = DefaultRouter()

router.register(prefix="comments",basename="comments", viewset=CommentsApiViewSet)