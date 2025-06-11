from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Profissional

class ProfissionalTests(APITestCase):
    def test_criar_profissional(self):
        data = {"nome": "Dra. Joana", "especialidade": "Clínica Geral"}
        response = self.client.post("/api/profissionais/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profissional.objects.count(),1)
        self.assertEqual(Profissional.objects.get().nome, "Dra. Joana")

    def test_profissional_nome_invalido(self):
        data = {"nome": "A", "especialidade": "Clínica Geral"}
        response = self.client.post("/api/profissionais/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("nome", response.data)
