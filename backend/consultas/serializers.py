from rest_framework import serializers

from .models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    class meta: 
        model = Consulta 
        fields = '__all__'

