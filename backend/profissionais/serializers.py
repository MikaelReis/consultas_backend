from rest_framework import serializers
import bleach
from .models import Profissional


class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['id', 'nome_social', 'profissao', 'endereco', 'contato', 'criado_em']

    def validate_nome_social(self, value):
        value = bleach.clean(value.strip())
        if len(value) < 3:
            raise serializers.ValidationError("O nome social deve ter ao menos 3 caracteres.")
        return value

    def validate_profissao(self, value):
        value = bleach.clean(value.strip())
        if not value:
            raise serializers.ValidationError("A profissão não pode estar vazia.")
        return value

    def validate_endereco(self, value):
        value = bleach.clean(value.strip())
        if not value:
            raise serializers.ValidationError("O endereço é obrigatório.")
        return value

    def validate_contato(self, value):
        value = bleach.clean(value.strip())
        if not value:
            raise serializers.ValidationError("O contato é obrigatório.")
        return value


