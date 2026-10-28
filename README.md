# Salão Beleza — projeto inicial Django

Projeto didático de site para salão de cabeleireiro feminino.

## Requisitos
- Python 3.10 ou superior
- Terminal (macOS/Linux) ou PowerShell (Windows)

## Instalação

### macOS / Linux
```bash
cd salao-beleza
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Windows (PowerShell)
```powershell
cd salao-beleza
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abra http://127.0.0.1:8000 no navegador.

## Personalização importante
- Edite `salao/views.py` para alterar serviços, preços e número do WhatsApp.
- No arquivo `salao/views.py`, troque `5521999999999` pelo número do salão no formato internacional, só números (55 + DDD + telefone).
- O formulário salva solicitações de agendamento no banco SQLite local. Ainda não verifica conflitos de horário nem envia confirmação automática.
- Para consultar os pedidos, crie um usuário administrador:
  `python manage.py createsuperuser`
  Depois acesse http://127.0.0.1:8000/admin

## Estrutura
- `config/`: configurações e rotas principais do Django
- `salao/`: página inicial, formulário e modelo de agendamento
- `templates/`: HTML
- `static/`: CSS

## Google Sites
O Google Sites não executa Django dentro dele. Para publicar, hospede este projeto Django em um serviço compatível e, se quiser, coloque no Google Sites um link para o site de agendamento.
