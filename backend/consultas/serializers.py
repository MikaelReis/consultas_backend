from rest_framework import serializers
from django.utils.timezone import make_aware
from django.core.exceptions import ValidationError
from .models import Consulta
import bleach

class ConsultaSerializer(serializers.ModelSerializer):
    data = serializers.DateField(required=False)
    horario = serializers.TimeField(required=False)

    class Meta:
        model = Consulta
        fields = '__all__'

    def validate_paciente(self, value):
        cleaned_value = bleach.clean(value, strip=True)
        if len(cleaned_value) < 3:
            raise serializers.ValidationError("O nome do paciente deve ter pelo menos 3 caracteres.")
        return cleaned_value

    def validate(self, data):
        data_value = data.get("data")
        horario_value = data.get("horario")
        profissional = data.get("profissional")

        if not data_value:
            raise serializers.ValidationError({"data": "A data da consulta é obrigatória."})
        if not horario_value:
            raise serializers.ValidationError({"horario": "O horário da consulta é obrigatório."})
        if not profissional:
            raise serializers.ValidationError({"profissional": "O profissional é obrigatório."})

        conflito = Consulta.objects.filter(
            profissional=profissional,
            data=data_value,
            horario=horario_value
        ).exists()

        if conflito:
            raise serializers.ValidationError(
                {"non_field_errors": ["Já existe uma consulta agendada para este profissional nesse dia e horário."]}
            )

        return data
