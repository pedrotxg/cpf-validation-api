from django.core.management.base import BaseCommand

from Authentication.models import ApiClient
from Authentication.services import ApiTokenService

# Ex. de uso: python manage.py criar_token_api --responsavel "Nome Do Responsavel"

class Command(BaseCommand):
    help = "Cria cliente API e gera token"

    def add_arguments(self, parser):
        parser.add_argument(
            "--responsavel",
            type=str,
            required=True,
            help="Nome do responsável"
        )

    def handle(self, *args, **options):
        responsavel = options["responsavel"]

        cliente, criado = ApiClient.objects.get_or_create(
            responsavel=responsavel,
            defaults={"ativo": True}
        )

        api_token, token_raw = ApiTokenService.criar_token(cliente)

        self.stdout.write(self.style.SUCCESS("Cliente pronto"))
        self.stdout.write(f"Responsável: {cliente.responsavel}")
        self.stdout.write(f"Prefixo: {api_token.prefix}")
        self.stdout.write("")
        self.stdout.write(self.style.WARNING("TOKEN (salve agora):"))
        self.stdout.write(token_raw)