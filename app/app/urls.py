# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path, re_path

urlpatterns = [
    path("", include("users.urls", namespace="users")),
    path("tokens/", include("tokens.urls", namespace="tokens")),
    path(
        'admin/login/',
        lambda r: redirect(
            f"/auth?{r.META['QUERY_STRING']}" if r.META['QUERY_STRING'] \
            else '/auth'
        )
    ),
    path("admin/", admin.site.urls),
   
]