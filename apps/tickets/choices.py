class TicketChoises:

    @staticmethod
    def priority():
        return (
            ("low", "Low"),
            ("average", "Average"),
            ("High", "High"),
        )

    @staticmethod
    def status():
        return (
            ("open", "Open"),
            ("in_service", "In Service"),
            ("resolved", "Resolved"),
        )
