from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = "Create user groups and define permissions"

    def handle(self, *args: Any, **kwargs: Any) -> None:
        group_names_permissions = {
            "Customers": ["add_ticket", "view_ticket"],
            "Support Agents": ["change_ticket", "view_ticket"],
            "Supervisors": ["change_ticket", "view_ticket"],
        }

        for group_name, perms_codenames in group_names_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Group "{group_name}" created successfully.')
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f'Group "{group_name}" already exists.')
                )

            permissions = Permission.objects.filter(codename__in=perms_codenames)
            group.permissions.set(permissions)
            self.stdout.write(
                self.style.SUCCESS(f'Permissions assigned to group "{group_name}".')
            )

        self.stdout.write(
            self.style.SUCCESS("All groups and permissions configured successfully!")
        )
