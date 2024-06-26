from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.api.views import UserRetrieveUpdateView, UserCreateView

app_name = "users"

urlpatterns = [
    path("signup/", UserCreateView.as_view(), name="signup"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", UserRetrieveUpdateView.as_view(), name="me"),
]
