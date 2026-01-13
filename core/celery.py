import os
from celery import Celery

# Imposta il modulo delle impostazioni predefinito di Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('sentinel_api')

# Legge la configurazione dalle impostazioni di Django usando il prefisso CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carica automaticamente i task dalle app registrate
app.autodiscover_tasks()