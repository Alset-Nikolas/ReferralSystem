from django.contrib.auth.views import LogoutView
from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("", views.ProfileUserPage.as_view(), name='profile'),
    path("auth/", views.AuthUserByTelPage.as_view(), name='auth'),
    path("logout/", LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]