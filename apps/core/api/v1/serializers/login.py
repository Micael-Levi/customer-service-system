from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("Username"),
    )
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(
            request=self.context.get("request"),
            username=username,
            password=password,
        )

        if not user:
            raise serializers.ValidationError({"Error": "Invalid credentials!"})

        refresh = RefreshToken.for_user(user)

        data = {
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
        }

        return data
