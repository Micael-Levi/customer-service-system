from rest_framework import viewsets
from apps.tickets.api.v1.serializers import AnswerSerializer

from apps.tickets.models import Answer


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
