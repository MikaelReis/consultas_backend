from rest_framework import serializers
from .models import Profissional

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['id', 'nome', 'especialidade', 'email', 'criado_em']

    def validate_nome(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome deve ter ao menos 3 caracteres.")
        return value

    def validate_especialidade(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("A especialidade não pode estar vazia.")
        return value
