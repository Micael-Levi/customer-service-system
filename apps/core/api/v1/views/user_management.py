from rest_framework import generics, permissions
from django.contrib.auth import get_user_model

from apps.core.api.v1.serializers.custom_user import CustomUserSerializer

User = get_user_model()


class UserManagementView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
