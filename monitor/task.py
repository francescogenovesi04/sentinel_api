from celery import shared_task
from .models import TargetAPI
from .utils import check_api_update

@shared_task
def monitor_all_apis():
    targets = TargetAPI.objects.filter(is_active=True)
    for target in targets:
        check_api_update(target)
    return f"Controllate {targets.count()} API."