from rest_framework import serializers

from apps.tickets.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            "ticket",
            "message",
            "created_by",
            "created_at",
        )
        read_only_fields = (
            "created_by",
            "created_at",
        )
