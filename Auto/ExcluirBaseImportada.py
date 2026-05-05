import os
import sys
sys.path.insert(0,"")

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from apps.Claro.services import remover_todos_socios


if __name__ == "__main__":
    remover_todos_socios()
    