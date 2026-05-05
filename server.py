import os
import sys
from waitress import serve

BASE_DIR = os.getenv('BASE_DIR')
sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from core.wsgi import application

serve(application, host=os.getenv('HOST'), port=os.getenv('PORT'), threads=16)