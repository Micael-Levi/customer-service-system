from django.urls import path, include
from rest_framework import routers
from apps.tickets.api.v1 import views

router = routers.DefaultRouter()

router.register("tickets", views.TicketView, basename="tickets")
router.register("answers", views.AnswerView, basename="answers")
urlpatterns = [
    path("", include(router.urls)),
]
