from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date, time
from .models import Consulta
from backend.profissionais.models import Profissional

class ConsultaTests(APITestCase):
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome_social="Dr. Marcos",
            profissao="Dermatologia",
            endereco="Rua A, 123",
            contato="(11) 91234-5678"
        )

    def test_criar_consulta_valida(self):
        data = {
            "profissional": self.profissional.id,
            "paciente": "Paciente 1",
            "data": "2025-06-10",
            "horario": "14:30:00"
        }
        response = self.client.post("/api/consultas/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Consulta.objects.count(), 1)
        self.assertEqual(Consulta.objects.get().paciente, "Paciente 1")

    def test_criar_consulta_nome_curto(self):
        data = {
            "profissional": self.profissional.id,
            "paciente": "AB",
            "data": "2025-06-10",
            "horario": "14:30:00"
        }
        response = self.client.post("/api/consultas/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("O nome do paciente deve ter pelo menos 3 caracteres.", str(response.data))

    def test_criar_consulta_sem_data(self):
        data = {
            "profissional": self.profissional.id,
            "paciente": "Paciente 2",
            "horario": "15:00:00"
        }
        response = self.client.post("/api/consultas/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("A data da consulta é obrigatória.", str(response.data))

    def test_criar_consulta_sem_horario(self):
        data = {
            "profissional": self.profissional.id,
            "paciente": "Paciente 3",
            "data": "2025-06-11"
        }
        response = self.client.post("/api/consultas/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("O horário da consulta é obrigatório.", str(response.data))

class ConsultaConflitoTests(APITestCase):
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome_social="Dr. Ana",
            contato="ana@email.com",
            endereco="Rua A, 123",
            profissao="Psicóloga"
        )
        self.url = "/api/consultas/"
        self.dados_base = {
            "profissional": self.profissional.id,
            "paciente": "Maria",
            "data": date.today().isoformat(),
            "horario": time(10, 0).isoformat()
        }

    def test_nao_permite_consulta_mesmo_horario_profissional(self):
        # 1. Cria a primeira consulta (deve funcionar)
        response1 = self.client.post(self.url, self.dados_base, format='json')
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)

        # 2. Tenta criar uma segunda com mesmo profissional, data e horário
        response2 = self.client.post(self.url, self.dados_base, format='json')
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("non_field_errors", response2.data)

