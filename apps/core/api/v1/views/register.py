from rest_framework import status, views
from rest_framework.response import Response

from apps.core.api.v1 import serializers


class RegisterView(views.APIView):

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "user": user.username,
                    "email": user.email,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
