from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import TargetAPI
from .utils import check_api_update

def dashboard(request):
    """Visualizza la lista di tutte le API monitorate."""
    apis = TargetAPI.objects.all().order_by('-last_check')
    return render(request, 'monitor/dashboard.html', {'apis': apis})

def run_manual_check(request, pk):
    """Esegue il controllo AI tramite HTMX senza ricaricare la pagina."""
    api = get_object_or_404(TargetAPI, pk=pk)

    # Esegue lo scraping e l'analisi AI
    check_api_update(api)

    # Determina il colore in base al successo della chiamata
    status_color = "green" if api.last_status == 200 else "red"
    status_text = f"HTTP {api.last_status}" if api.last_status else "HTTP Error"

    # Restituisce il frammento HTML per aggiornare la card
    return HttpResponse(f"""
        <div class="flex justify-between items-start mb-4">
            <h2 class="text-xl font-semibold">{api.name}</h2>
            <span class="px-2 py-1 rounded text-xs font-bold bg-{status_color}-900 text-{status_color}-300">
                {status_text}
            </span>
        </div>
        <p class="text-slate-400 text-sm mb-4 truncate">{api.swagger_url}</p>
        <div class="bg-slate-900/50 rounded-lg p-4 mb-4 border border-slate-700">
            <h3 class="text-xs uppercase text-slate-500 font-bold mb-2">Analisi AI Aggiornata</h3>
            <div class="text-sm text-slate-300 italic whitespace-pre-line">
                {api.last_analysis or "Nessun cambiamento rilevato rispetto all'ultima versione."}
            </div>
        </div>
        <button hx-post="/check/{api.pk}/"
                hx-target="closest .api-card"
                hx-swap="innerHTML"
                class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition">
            Analizza Ora
        </button>
    """)