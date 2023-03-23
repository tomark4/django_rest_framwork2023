from django.contrib import admin
from django.urls import path, include
# from posts.views import Home
from posts.urls import router as router_post

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('post/',Home.as_view())
    # path('api/posts/', PostApiView.as_view())
    path('api/', include(router_post.urls))
]
