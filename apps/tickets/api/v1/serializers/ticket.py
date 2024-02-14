from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.tickets.models.ticket import Ticket

User = get_user_model()


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "title",
            "description",
            "priority",
            "status",
            "user",
            "attendant",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("usuario", "atendente", "criado_em", "atualizado_em")

    def create(self, validated_data):
        request = self.context.get("request")
        if request:
            validated_data["user"] = request.user
        return super().create(validated_data)
