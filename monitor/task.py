from celery import shared_task
from .models import TargetAPI
from .utils import check_api_update

@shared_task
def run_sentinel_periodic_check():
    """
    Task periodico che controlla solo le API con monitoraggio attivo.
    """
    # Filtriamo solo le API dove is_auto_active è True
    active_apis = TargetAPI.objects.filter(is_auto_active=True)

    if not active_apis.exists():
        return "Nessuna API attiva per il monitoraggio automatico."

    for api in active_apis:
        check_api_update(api)

    return f"Controllate {active_apis.count()} API con successo."