from rest_framework import permissions


class CanRespondTicket(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.group.filter(name__in=["Customers", "Support Agents"]):
            return True
        if view.action == "create":
            ticket_id = request.data.get("ticket")
            if ticket_id:
                Ticket = view.queryset.model.ticket.field.related_model
                ticket = Ticket.objects.filter(
                    id=ticket_id, status="waiting_user"
                ).first()
                return ticket and ticket.user == request.user
        return False
