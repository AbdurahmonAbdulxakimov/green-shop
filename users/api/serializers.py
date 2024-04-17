from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import User as UserType

User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
        )


class UserCreateSerializer(serializers.ModelSerializer[UserType]):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password",
        )

        def create(self, validated_data):
            user = super().create(validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user
