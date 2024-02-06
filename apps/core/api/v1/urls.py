from django.urls import path

from apps.core.api.v1 import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("users/", views.UserManagementView.as_view(), name="users"),
]
