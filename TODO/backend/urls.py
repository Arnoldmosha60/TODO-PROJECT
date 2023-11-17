from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("todo.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('apis/', include('api.urls')),
    path('users/', include('user.urls')),
]
