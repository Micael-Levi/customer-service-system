from rest_framework import views, permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from apps.core.api.v1 import serializers


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data
            return Response(user, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_401_UNAUTHORIZED)
