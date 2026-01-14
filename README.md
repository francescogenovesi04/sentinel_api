### SentinelAPI
AI-Powered Breaking Change Monitor

SentinelAPI è un sistema di monitoraggio intelligente progettato per sorvegliare le API esterne in tempo reale. Grazie all'integrazione tra Django e OpenAI, il sistema rileva automaticamente ogni modifica nelle documentazioni OpenAPI/Swagger, traducendo complessi cambiamenti tecnici in spiegazioni semplici e segnalando tempestivamente le "breaking changes".

## Funzionalità Principali

-Monitoraggio Asincrono: Gestione efficiente di task pesanti in background tramite Celery e Redis.

-Analisi AI Semantica: Utilizza GPT-4o/mini per interpretare il significato tecnico dei cambiamenti, non solo le differenze testuali.

-Dashboard Moderna: Interfaccia reattiva sviluppata con Tailwind CSS e HTMX per aggiornamenti istantanei senza ricaricare la pagina.

-Controllo Granulare: Gestione centralizzata dei target tramite Admin Panel con possibilità di attivare/disattivare il monitoraggio per ogni singola risorsa.


## Installazione e Setup

Nota sull'ambiente di sviluppo:

**Questa guida al setup è ottimizzata per Linux Mint. Tuttavia, i passaggi sono pienamente compatibili con Ubuntu, Debian e la maggior parte delle distribuzioni basate su kernel Linux che utilizzano il gestore pacchetti apt.**

0. Installa Redis (se non lo hai già)
 
    ```
    sudo apt update
    sudo apt install redis-server
    ```
   
2. Clonazione del Progetto

```
git clone <tuo-link-github>
cd sentinel_api
```

2. Ambiente Virtuale

```
python -m venv venv
source venv/bin/activate 
```

3. Installazione Dipendenze

```pip install -r requirements.txt```

4. Configurazione Variabili d'Ambiente

Crea un file .env nella root del progetto:

```
OPENAI_API_KEY=la_tua_chiave_qui
SECRET_KEY=tua_secret_key
DEBUG=True
```

5. Inizializzazione Database
   
```
python manage.py migrate
python manage.py createsuperuser
```

## Workflow & Daily Routine

Per il pieno funzionamento di SentinelAPI è necessario avviare i seguenti servizi in tre terminali separati:
Avvio Servizi

-Terminale A (Web Server): 

```python manage.py runserver```

-Terminale B (Celery Worker):

```celery -A core worker --loglevel=info```

-Terminale C (Celery Beat) (Gestisce la scansione automatica programmata, es. ogni 5 minuti):

```celery -A core beat --loglevel=info```
    
## Come Funziona

-Aggiunta Target: Inserisci l'URL di uno Swagger/OpenAPI JSON nell'Admin Panel di Django.

-Monitoraggio: * Manuale: Clicca su "Analizza Ora" nella dashboard per un controllo istantaneo.

-Automatico: Se il toggle è su ON, Celery Beat avvia il controllo ciclicamente.

-Confronto AI: Il sistema scarica la documentazione live, la confronta con l'ultima versione salvata e genera un report dettagliato tramite GPT-4o, evidenziando se le modifiche richiederanno interventi sul tuo codice.
