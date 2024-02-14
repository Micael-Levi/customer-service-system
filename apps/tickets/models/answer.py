from django.db import models

from apps.tickets.models.ticket import Ticket
from sistema_atendimento_cliente import settings


class Answer(models.Model):
    ticket = models.ForeignKey(Ticket, related_name="answers", on_delete=models.CASCADE)
    message = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
