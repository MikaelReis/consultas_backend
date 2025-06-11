from rest_framework import serializers
from .models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    data = serializers.DateField(required=False)
    horario = serializers.TimeField(required=False)

    class Meta:
        model = Consulta
        fields = '__all__'

    def validate_paciente(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("O nome do paciente deve ter pelo menos 3 caracteres.")
        return value

    def validate(self, data):
        if not data.get("data"):
            raise serializers.ValidationError({"data": "A data da consulta é obrigatória."})
        if not data.get("horario"):
            raise serializers.ValidationError({"horario": "O horário da consulta é obrigatório."})
        return data
