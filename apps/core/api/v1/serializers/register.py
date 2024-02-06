from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[password_validation.validate_password],
    )
    confirm_password = serializers.CharField(
        write_only=True,
        required=True,
        label="Confirm password",
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "confirm_password",
            "email",
            "first_name",
            "last_name",
            "phone_number",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise ValidationError({"Error": "Passwords do not match!"})
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        return user
