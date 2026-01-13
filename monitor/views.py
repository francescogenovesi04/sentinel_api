from django.shortcuts import render, get_object_or_404
from .models import TargetAPI
from .utils import check_api_update

def dashboard(request):
    """
    Visualizza la dashboard. Ordiniamo per ID per evitare
    spostamenti delle card durante gli aggiornamenti.
    """
    apis = TargetAPI.objects.all().order_by('id')
    return render(request, 'monitor/dashboard.html', {'apis': apis})

def toggle_auto_monitor(request, pk):
    """
    Attiva/Disattiva il monitoraggio automatico salvando lo stato nel DB.
    HTMX aggiornerà la card mostrando se il controllo automatico è ON o OFF.
    """
    api = get_object_or_404(TargetAPI, pk=pk)
    api.is_auto_active = not api.is_auto_active
    api.save()
    return render(request, 'monitor/api_card.html', {'api': api})

def run_manual_check(request, pk):
    """
    Esegue il controllo manuale immediato. Django invia la richiesta,
    l'AI risponde e HTMX sostituisce la card con i nuovi dati.
    """
    api = get_object_or_404(TargetAPI, pk=pk)
    check_api_update(api)
    return render(request, 'monitor/api_card.html', {'api': api})