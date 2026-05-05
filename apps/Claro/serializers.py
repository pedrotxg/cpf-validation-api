from rest_framework import serializers
from apps.Claro.models import SociosCPF
import re


class SociosSerializer(serializers.ModelSerializer):
    cpf = serializers.CharField()

    class Meta:
        model = SociosCPF
        fields = ['cpf']

    def validate_cpf(self, value):
        # garantir string
        if not isinstance(value, str):
            raise serializers.ValidationError("CPF deve ser texto.")

        # remover espaços
        value = value.strip()

        # validar tamanho = 11
        if len(value) != 11:
            raise serializers.ValidationError("CPF deve conter 11 caracteres.")

        # validar padrão 123***45678
        # 3 números + 3 asteriscos + 5 números
        if not re.fullmatch(r'\d{3}\*{3}\d{5}', value):
            raise serializers.ValidationError(
                "CPF deve estar no formato 123***45678."
            )

        return value