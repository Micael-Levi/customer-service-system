from rest_framework import serializers

from apps.tickets.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = (
            "ticket",
            "message",
            "sender",
            "created_at",
        )
        read_only_fields = (
            "created_by",
            "created_at",
        )

    def get_sender(self, obj):
        sender = obj.created_by

        return {
            "id": sender.id,
            "first_name": sender.first_name,
        }
