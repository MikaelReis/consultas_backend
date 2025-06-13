# 🩺 Consultas Backend

API RESTful para gestão de profissionais de saúde e agendamento de consultas, desenvolvida em Python com Django + Django REST Framework.

---

## 🚀 Funcionalidades

- Cadastro, edição, exclusão e listagem de profissionais (nome social, profissão, endereço, contato).
- CRUD de consultas médicas vinculadas a um profissional.
- Validações:
  - Sanitização de inputs (com `bleach`).
  - Nome com no mínimo 3 caracteres.
  - Campos obrigatórios: data e horário da consulta.
- Todos os retornos em JSON.

---

## 🛠 Tecnologias

- **Framework**: Django 5.2.3 + Django REST Framework  
- **Banco de dados**: PostgreSQL  
- **Contêiner**: Docker + Docker Compose  
- **CI/CD**: GitHub Actions (testes automáticos)  
- **Deploy**: Render (Docker + PostgreSQL)

---

## 📦 Setup Local

### Pré-requisitos

- Python 3.11+  
- Docker e Docker Compose  

### Instalação

```bash
git clone https://github.com/MikaelReis/consultas_backend.git
cd consultas_backend
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt

Rodando com Docker

docker-compose up -d --build
docker-compose ps  # Verifica contêineres

Verifique se o contêiner projetolacrei-db-1 está em execução.

Para criar as migrações e aplicar:

python manage.py makemigrations
python manage.py migrate

Crie um superusuário (opcional):

python manage.py createsuperuser

Execute:

python manage.py runserver

Acesse http://localhost:8000/api/ e o admin em http://localhost:8000/admin/.
✅ Testes

Os testes cobrem API de profissionais e consultas:

python manage.py test

Estão implementados com APITestCase:

    Verifica criação, validações, erros em campos obrigatórios.

    Testes automatizados rodando via GitHub Actions.

💾 Variáveis de Ambiente

No deploy (Render, GitHub Actions, Docker), as seguintes variáveis são usadas:

    DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT

    SECRET_KEY

    DEBUG

Exemplo no settings.py:

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.getenv('DB_NAME', 'lacrei_db'),
    'USER': os.getenv('DB_USER', 'mikael'),
    'PASSWORD': os.getenv('DB_PASSWORD', 'chat'),
    'HOST': os.getenv('DB_HOST', 'db'),
    'PORT': os.getenv('DB_PORT', '5432'),
  }
}

⚙️ Deploy

Feito no Render:

    Serviço Web (Docker)

    Banco PostgreSQL gerenciado

    Variáveis definidas nas configurações

    Deploy automático via git push

Endpoint base:

https://consultas‑backend.onrender.com/api/

🔍 Endpoints

    GET /api/profissionais/

    POST /api/profissionais/

    GET /api/profissionais/{id}/

    PUT /api/profissionais/{id}/

    DELETE /api/profissionais/{id}/

    GET /api/consultas/

    POST /api/consultas/

    GET /api/consultas/{id}/

    PUT /api/consultas/{id}/

    DELETE /api/consultas/{id}/

Filtros disponíveis, ex.:

GET /api/consultas/?profissional=3

📚 Documentação Técnica

    Sanitização com bleach nos serializers.

    Validações específicas (comprimento do nome, campo obrigatório data/hora).

    MQTT:

        CI com GitHub Actions

        Testes automatizados

        Containerização com Docker

        Deploy com Render

❗ Melhorias Pendentes

    Documentação visual via Swagger ou Redoc (pode ser adicionada via drf-spectacular).

    Mock/integracão com sistema de pagamentos (AssAs) — opcional mas valorizado.

    Pipeline de rollback no CI/CD (monitoramento e reverter deploy em caso de falhas).

📝 Registro de Alterações

    Model Profissional ajustada para incluir nome_social, contato e endereco.

    Refatoração de validações nos serializers.

    Atualização de workflows no GitHub Actions para conexão com DB.

    Deploy Docker no Render.

🔗 Links

    Repositório: https://github.com/MikaelReis/consultas_backend

    API: https://consultas-backend.onrender.com/api/
