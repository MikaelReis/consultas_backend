from django.db import models

class Profissional(models.Model):
    nome = models.CharFiled(max_lenght=100)
    especialidade = models.CharField(max_lenght=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    
