from django.db import transaction
from apps.Claro.models import SociosCPF
import logging
import os


@transaction.atomic
def inserir_socios(col1:str, col2:str, cpf:str):
    logging.log(20, msg=f"Inserted data in {os.getenv('TB_CLIENTE')} with successfull...")
    return SociosCPF.objects.create(col1=col1, col2=col2, cpf=cpf)

@transaction.atomic
def remover_todos_socios():
    deletados, _ = SociosCPF.objects.all().delete()
    logging.log(20, msg=f"All data from {os.getenv('TB_CLIENTE')} deleted as successfull...")
    return deletados

@transaction.atomic
def verificar_cpf_socio(cpf:str):
    return SociosCPF.objects.filter(cpf=cpf).exists()