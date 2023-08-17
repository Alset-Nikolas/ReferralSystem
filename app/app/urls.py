from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from django.conf import settings

urlpatterns = [
    path("users/", include("users.urls", namespace="users")),
    path("tokens/", include("tokens.urls", namespace="tokens")),
    path("admin/", admin.site.urls),
]