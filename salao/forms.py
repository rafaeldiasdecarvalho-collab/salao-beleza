from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ["nome", "telefone", "servico", "data", "horario", "observacoes"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
            "horario": forms.TimeInput(attrs={"type": "time"}),
            "observacoes": forms.Textarea(attrs={"rows": 3}),
        }
        labels = {
            "nome": "Seu nome",
            "telefone": "WhatsApp para contato",
            "servico": "Serviço desejado",
            "data": "Data preferida",
            "horario": "Horário preferido",
            "observacoes": "Observações (opcional)",
        }
