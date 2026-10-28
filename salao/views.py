from django.shortcuts import render, redirect
from .forms import AgendamentoForm

def inicio(request):
    servicos = [
        {"nome": "Corte feminino", "descricao": "Um corte pensado para seu estilo.", "preco": "A partir de R$ 60"},
        {"nome": "Escova", "descricao": "Finalização com brilho e movimento.", "preco": "A partir de R$ 45"},
        {"nome": "Hidratação", "descricao": "Cuidado para fios macios e saudáveis.", "preco": "A partir de R$ 50"},
        {"nome": "Coloração", "descricao": "Realce sua beleza com uma nova cor.", "preco": "Sob consulta"},
    ]
    # Troque pelo WhatsApp real do salão: código do país + DDD + número, sem espaços.
    whatsapp = "5521999999999"
    mensagem = "Olá! Gostaria de informações sobre os serviços do salão."
    return render(request, "salao/inicio.html", {
        "servicos": servicos,
        "whatsapp_url": f"https://wa.me/{whatsapp}?text={mensagem.replace(' ', '%20')}",
    })

def agendar(request):
    if request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("confirmacao")
    else:
        form = AgendamentoForm()
    return render(request, "salao/agendar.html", {"form": form})

def confirmacao(request):
    return render(request, "salao/confirmacao.html")
