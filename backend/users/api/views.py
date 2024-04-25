from django.contrib.auth import get_user_model
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView

from .serializers import UserSerializer, UserCreateSerializer

User = get_user_model()


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self) -> User:  # type: ignore
        user = get_object_or_404(User, id=self.request.user.id)
        return user


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
