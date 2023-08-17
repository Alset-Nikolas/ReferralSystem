from django.contrib import admin
from django.urls import include, path
from users import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
app_name = "users"

urlpatterns = [
    path("auth/", views.AuthUserByTelPage.as_view(), name='auth'),
    path("logout/", LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("profile/", views.ProfileUserPage.as_view(), name='profile'),
]