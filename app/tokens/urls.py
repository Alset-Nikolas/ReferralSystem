from django.contrib import admin
from django.urls import include, path
from tokens import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
app_name = "tokens"

urlpatterns = [
    path("activate/", views.ActivateToken.as_view(), name='activate'),
]