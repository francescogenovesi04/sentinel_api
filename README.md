#  SentinelAPI: AI-Powered Breaking Change Monitor

SentinelAPI è un sistema di monitoraggio intelligente per API esterne. Utilizza Django e OpenAI per rilevare automaticamente cambiamenti nelle documentazioni OpenAPI/Swagger e avvisare gli sviluppatori sulle "breaking changes" rilevate.

Monitoraggio di Terze Parti: Inserisci le API che usi nel tuo lavoro o nei tuoi progetti (es. Stripe, PayPal, o l'API di un fornitore). Se loro cambiano qualcosa e il tuo codice si rompe, SentinelAPI te lo dice prima che i tuoi utenti se ne accorgano.

##  Funzionalità principali
- **Monitoraggio Asincrono:** Gestione dei task in background tramite Celery e Redis.
- **Analisi AI:** Integrazione con OpenAI (GPT-4o-mini) per spiegare i cambiamenti tecnici in linguaggio naturale.
- **Admin Dashboard:** Gestione centralizzata dei target API da monitorare.
- **Portabilità:** Configurazione tramite variabili d'ambiente (.env).

##  Tech Stack
- **Backend:** Django 5.x
- **Task Queue:** Celery & Redis
- **AI:** OpenAI API
- **Networking:** Requests (Scraping)

---
### Installazione

Se vuoi clonare questo progetto localmente:

##    Clonazione: git clone <tuo-link-github>

##   Installazione dipendenze: pip install -r requirements.txt

##    Configurazione: Crea un file .env con la tua OPENAI_API_KEY.

##    Migrazioni: python manage.py migrate

### Guida all'Avvio (Daily Routine)

Essendo un'architettura distribuita, il progetto richiede l'attivazione di tre componenti. Segui questi passi ogni volta che riprendi lo sviluppo:

### 1. Prerequisiti (Solo la prima volta)
Assicurati che Redis sia attivo sul tuo sistema Linux Mint:

sudo systemctl start redis-server

## 2. Attivazione Ambiente Virtuale

Apri il terminale nella cartella del progetto:
Bash

source venv/bin/activate

## 3. Avvio dei Servizi

Per far funzionare SentinelAPI sono necessari due terminali separati:

Terminale A: Server Web (UI & Admin)
Bash

python manage.py runserver

Terminale B: Worker Celery (Processore Task AI)
Bash

celery -A core worker --loglevel=info

Terminale C: Celery Beat (L'orologio)

Gestisce i controlli automatici ogni 5 minuti basandosi sul tasto Auto ON/OFF.
Bash

source venv/bin/activate
celery -A core beat --loglevel=info

