from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TargetAPI
from .utils import check_api_update

# Questa è la funzione che mancava e causava l'errore!
def dashboard(request):
    apis = TargetAPI.objects.all().order_by('-last_check')
    return render(request, 'monitor/dashboard.html', {'apis': apis})

# Questa è la funzione per il bottone HTMX
def run_manual_check(request, pk):
    api = get_object_or_404(TargetAPI, pk=pk)

    # Eseguiamo il controllo (Scraping + AI)
    check_api_update(api)

    # Determiniamo il colore in base allo status
    status_color = "green" if api.last_status == 200 else "red"

    # Restituiamo il pezzo di HTML che aggiornerà la card
    return HttpResponse(f"""
        <div class="flex justify-between items-start mb-4">
            <h2 class="text-xl font-semibold">{api.name}</h2>
            <span class="px-2 py-1 rounded text-xs font-bold bg-{status_color}-900 text-{status_color}-300">
                HTTP {api.last_status}
            </span>
        </div>
        <p class="text-slate-400 text-sm mb-4 truncate">{api.swagger_url}</p>
        <div class="bg-slate-900/50 rounded-lg p-4 mb-4 border border-slate-700">
            <h3 class="text-xs uppercase text-slate-500 font-bold mb-2">Analisi AI Aggiornata</h3>
            <p class="text-sm text-slate-300 italic">{api.last_analysis or "Nessun cambiamento rilevato."}</p>
        </div>
        <button hx-post="/check/{api.pk}/" hx-target="closest .api-card" hx-swap="innerHTML" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition">
            Analizza Ora
        </button>
    """)