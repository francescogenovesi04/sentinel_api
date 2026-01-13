from django.shortcuts import render, get_object_or_404
from .models import TargetAPI
from .utils import check_api_update

def dashboard(request):
    apis = TargetAPI.objects.all().order_by('-last_check')
    return render(request, 'monitor/dashboard.html', {'apis': apis})

def toggle_auto_monitor(request, pk):
    api = get_object_or_404(TargetAPI, pk=pk)
    api.is_auto_active = not api.is_auto_active
    api.save()
    # RIMANDA INDIETRO LA CARD COMPLETA
    return render(request, 'monitor/api_card.html', {'api': api})

def run_manual_check(request, pk):
    api = get_object_or_404(TargetAPI, pk=pk)
    check_api_update(api)
    # RIMANDA INDIETRO LA CARD COMPLETA DOPO L'AI
    return render(request, 'monitor/api_card.html', {'api': api})