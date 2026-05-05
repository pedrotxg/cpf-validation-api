from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from Authentication.permissions import ValidApiToken
from apps.Claro.services import verificar_cpf_socio

from apps.Claro.serializers import SociosSerializer

#
## CONSULTA DE CPF NA BASE DE DADOS
#
@api_view(['GET'])
@permission_classes([ValidApiToken])
def consultar_cpf_no_db(request, cpf:str):
    try:
        # Validando CPF com Serializer
        serializer = SociosSerializer(data={"cpf": cpf})
        if not serializer.is_valid():
            return Response(
                {
                    "success": False,
                    "error": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        cpf_validado = serializer.validated_data["cpf"]

        localizado = verificar_cpf_socio(cpf=cpf_validado)
        if not localizado:
            return Response(
                {
                    "success": True,
                    "cpf": cpf,
                    "found": False
                },
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {
                "success": True,
                "cpf": cpf,
                "found": True
            },
            status=status.HTTP_200_OK
        )

    except Exception:
        return Response(
            {
                "success": False,
                "message": "Erro ao realizar consulta",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def health_check(request):
    return Response({"status": "ok"})

...