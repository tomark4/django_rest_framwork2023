from django.contrib import admin
from django.urls import path, include
from posts.urls import router as router_post
from categories.api.router import router as router_categories
from comments.api.router import router as router_comments
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import settings

schema_view = get_schema_view(
   openapi.Info(
      title="Doc api blog",
      default_version='v1',
      description="Doc api blog",
      terms_of_service="https://jottasistemas.com/terms/policies",
      contact=openapi.Contact(email="contact@jotta.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router_post.urls)),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_comments.urls)),
    path('api/', include('users.api.router'))
]

if settings.DEBUG:
   from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
