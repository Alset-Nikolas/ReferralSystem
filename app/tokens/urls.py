from django.urls import path
from tokens import views

app_name = "tokens"

urlpatterns = [
    path("activate/", views.ActivateToken.as_view(), name='activate'),
]