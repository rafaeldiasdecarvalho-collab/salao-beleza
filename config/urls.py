from django.contrib import admin
from django.urls import path
from salao import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("agendar/", views.agendar, name="agendar"),
    path("agendamento-enviado/", views.confirmacao, name="confirmacao"),
]
