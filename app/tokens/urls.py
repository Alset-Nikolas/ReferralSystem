from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path
from tokens import views

app_name = "tokens"

urlpatterns = [
    path("activate/", views.ActivateToken.as_view(), name='activate'),
]