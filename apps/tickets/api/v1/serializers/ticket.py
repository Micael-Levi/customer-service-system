from django.contrib.auth import get_user_model
from action_serializer import ModelActionSerializer
from apps.tickets.api.v1 import serializers

from apps.tickets.models.ticket import Ticket

User = get_user_model()


class TicketSerializer(ModelActionSerializer):
    answers = serializers.AnswerSerializer(many=True)

    class Meta:
        model = Ticket
        fields = (
            "id",
            "title",
            "description",
            "priority",
            "status",
            "user",
            "attendant",
            "created_at",
            "updated_at",
        )
        action_fields = {
            "retrieve": {
                "fields": (
                    "id",
                    "title",
                    "description",
                    "priority",
                    "status",
                    "user",
                    "attendant",
                    "created_at",
                    "updated_at",
                    "answers",
                )
            }
        }
        read_only_fields = ("user", "attendant", "created_at", "updated_at")

    def create(self, validated_data):
        request = self.context.get("request")
        if request:
            validated_data["user"] = request.user
        return super().create(validated_data)
