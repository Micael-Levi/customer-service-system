from django.db import models
from django.contrib.auth import get_user_model

from apps.tickets.choices import TicketChoises

User = get_user_model()


class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(
        max_length=10,
        choices=TicketChoises.priority(),
        default="average",
    )
    status = models.CharField(
        max_length=20,
        choices=TicketChoises.status(),
        default="open",
    )
    user = models.ForeignKey(User, related_name="tickets", on_delete=models.CASCADE)
    attendant = models.ForeignKey(
        User,
        related_name="tickets_atendidos",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
