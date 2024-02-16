from django.contrib.auth import get_user_model
from rest_framework import serializers
from action_serializer import ModelActionSerializer
from apps.tickets.api.v1 import serializers as ticket_serializers

from apps.tickets import models

User = get_user_model()


class TicketSerializer(ModelActionSerializer):
    answers = ticket_serializers.AnswerSerializer(many=True)
    new_answer = serializers.CharField(
        write_only=True,
        required=False,
        allow_blank=True,
    )

    class Meta:
        model = models.Ticket
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
            "new_answer",
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
        extra_kwargs = {
            "new_answer": {"write_only": True},
        }

    def create(self, validated_data):
        request = self.context.get("request")
        if request:
            validated_data["user"] = request.user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        new_answer = validated_data.pop("new_answer", None)
        if new_answer:
            models.Answer.objects.create(
                ticket=instance,
                message=new_answer,
                created_by=self.context["request"].user,
            )
        return super().update(instance, validated_data)
