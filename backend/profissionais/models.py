from django.db import models

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True) 
    criado_em = models.DateTimeField(auto_now_add=True)

