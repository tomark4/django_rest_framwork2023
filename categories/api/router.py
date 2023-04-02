from rest_framework.routers import DefaultRouter
from .views import CategoryApiViewSet

router = DefaultRouter()

router.register(prefix="categories", basename="categories",viewset=CategoryApiViewSet)