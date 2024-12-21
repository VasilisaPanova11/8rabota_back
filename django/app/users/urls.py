from django.urls import path
from .views import (
    Login,
    Register,
    Logout,
    UserList,
    SettingsView,
    UserAPIListCreateView,
    UserAPIView,
)

app_name = "users"

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("register/", Register.as_view(), name="register"),
    path("logout/", Logout.as_view(), name="logout"),
    path("list/", UserList.as_view(), name="list"),
    path("settings/", SettingsView.as_view(), name="settings"),
    path("api", UserAPIListCreateView.as_view(), name="api"),
    path("api/<int:pk>", UserAPIView.as_view(), name="api-one-action"),
]
