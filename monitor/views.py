from django.shortcuts import render, get_object_or_404
from .models import TargetAPI
from .utils import check_api_update

def dashboard(request):
    # Ordiniamo per ID così le card non saltano quando Celery le aggiorna
    apis = TargetAPI.objects.all().order_by('id')
    return render(request, 'monitor/dashboard.html', {'apis': apis})

def toggle_auto_monitor(request, pk):
    api = get_object_or_404(TargetAPI, pk=pk)
    api.is_auto_active = not api.is_auto_active
    api.save()
    return render(request, 'monitor/api_card.html', {'api': api})

def run_manual_check(request, pk):
    api = get_object_or_404(TargetAPI, pk=pk)
    check_api_update(api)
    return render(request, 'monitor/api_card.html', {'api': api})