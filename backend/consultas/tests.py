from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from backend.profissionais.models import Profissional
from .models import Consulta

class ConsultaTests(APITestCase):
    def test_criar_consulta(self):
        profissional = Profissional.objects.create(
            nome="Dr. Marcos",
            especialidade="Dermatologia",
            email="marcos@exemplo.com"
        )

        data = {
            "profissional": profissional.id,
            "paciente": "Paciente 1",
            "data": "2025-06-10",
            "horario": "14:30:00"
        }

        response = self.client.post("/api/consultas/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Consulta.objects.count(), 1)
        self.assertEqual(Consulta.objects.get().paciente, "Paciente 1")



