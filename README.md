# cpf-validation-api
Projeto Django para validação de CPF e serviços relacionados.

Este repositório contém a aplicação responsável por validação e serviços auxiliares usados internamente. O README a seguir fornece instruções de instalação, execução básica e boas práticas sem expor dados sensíveis.

## Funcionalidade principal
- Validação de CPFs e endpoints/serviços associados.

## Estrutura do projeto (resumo)
- `manage.py` / `server.py` — scripts de execução.
- `requirements.txt` — dependências do Python.
- `apps/` — aplicações Django; contém subapps como `Claro` e `Authentication`.
- `core/` — configuração do projeto (settings, urls, wsgi/asgi).

Para detalhes, consulte os arquivos dentro de cada pasta.

## Dependências
Instale as dependências a partir de `requirements.txt`:

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Configuração
- Use variáveis de ambiente para qualquer configuração sensível (chaves, tokens, strings de conexão).
- Exemplos de variáveis:
  - `DJANGO_SECRET_KEY`
  - `DATABASE_URL`
  - `API_TOKEN`

- Adicione ao `.gitignore` arquivos que contenham segredos (por exemplo `.env`, credenciais locais).

## Executando localmente
- Rodar migrações:

```bash
python manage.py migrate
```

- Iniciar servidor de desenvolvimento:

```bash
python manage.py runserver
# ou (se usar server.py) python server.py
```

## Testes
- Execute os testes das aplicações Django com:

```bash
python manage.py test
```

## Boas práticas de Git e segurança
- Nunca comite arquivos com segredos ou tokens. Use `.env` e mantenha-o ignorado.
- Revise `requirements.txt` antes de publicar imagens/artefatos.
- Use branches para desenvolvimento e PRs para revisão de código.