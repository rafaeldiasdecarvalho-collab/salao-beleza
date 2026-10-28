from django.db import models

class Agendamento(models.Model):
    SERVICOS = [
        ("Corte", "Corte"),
        ("Escova", "Escova"),
        ("Coloração", "Coloração"),
        ("Hidratação", "Hidratação"),
        ("Tratamento capilar", "Tratamento capilar"),
    ]

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    servico = models.CharField(max_length=40, choices=SERVICOS)
    data = models.DateField()
    horario = models.TimeField()
    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["data", "horario"]

    def __str__(self):
        return f"{self.nome} — {self.servico} — {self.data} {self.horario}"
