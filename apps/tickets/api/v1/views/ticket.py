from rest_framework import permissions, viewsets

from apps.tickets.api.v1.serializers.ticket import TicketSerializer
from apps.tickets.models import Ticket


class TicketView(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        return Ticket.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
