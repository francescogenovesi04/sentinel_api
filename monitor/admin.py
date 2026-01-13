from django.contrib import admin
from .models import TargetAPI

@admin.register(TargetAPI)
class TargetAPIAdmin(admin.ModelAdmin):
    # Questi campi appariranno nella lista generale
    list_display = ('name', 'swagger_url', 'last_status', 'last_check')

    # Questi campi saranno visibili e modificabili quando clicchi su un'API
    fields = ('name', 'swagger_url', 'is_active', 'last_content', 'last_analysis')
    readonly_fields = ('last_analysis',) # L'analisi la scrive l'AI, noi la leggiamo solo