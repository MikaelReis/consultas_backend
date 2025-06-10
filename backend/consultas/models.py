from django.db import models

from backend.profissionais.models import Profissional

class Consulta(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    paciente = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()   
    criado_em = models.DateTimeField(auto_now_add=True)

