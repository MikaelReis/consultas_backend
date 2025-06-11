from rest_framework.test import APITestCase
from rest_framework import status
from backend.profissionais.models import Profissional
from .models import Consulta

class ConsultaTests(APITestCase):
    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome="Dr. Marcos",
            especialidade="Dermatologia",
            email="marcos@exemplo.com"
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


