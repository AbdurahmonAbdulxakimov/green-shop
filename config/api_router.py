from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter


app_name = "api"
urlpatterns = (path("users/", include("users.urls", namespace="users")),)
