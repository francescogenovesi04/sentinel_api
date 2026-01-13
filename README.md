🛡️ SentinelAPI: AI-Powered Breaking Change Monitor

SentinelAPI è un sistema di monitoraggio intelligente progettato per sorvegliare le API esterne in tempo reale. Utilizzando l'integrazione tra Django e OpenAI, il sistema rileva automaticamente ogni modifica nelle documentazioni OpenAPI/Swagger, traducendo complessi cambiamenti tecnici in spiegazioni semplici e segnalando tempestivamente le "breaking changes" che potrebbero interrompere il funzionamento dei tuoi software.
🚀 Funzionalità Principali

    Monitoraggio Asincrono: Gestione efficiente dei task pesanti in background grazie all'architettura basata su Celery e Redis.

    Analisi AI Semantica: Integrazione con OpenAI (GPT-4o/mini) per analizzare non solo le differenze testuali, ma il significato tecnico dei cambiamenti.

    Dashboard Moderna: Interfaccia reattiva sviluppata con Tailwind CSS e HTMX per aggiornamenti istantanei senza ricaricamento della pagina.

    Controllo Granulare: Gestione centralizzata dei target tramite Admin Panel e possibilità di attivare/disattivare il monitoraggio automatico per ogni singola card.

🛠️ Tech Stack
1. Il Cuore: Django (Python)

È il framework principale che coordina l'intera applicazione. Gestisce il database (SQLite), l'autenticazione tramite l'Admin Panel e la logica di comunicazione tra i vari servizi.
2. Il Cervello: OpenAI GPT-4o

A differenza di un normale software di "diff", SentinelAPI esegue un'analisi semantica. GPT-4o legge i file JSON e avvisa se, ad esempio, la rimozione di un parametro obbligatorio richiederà modifiche al tuo codice.
3. Il Braccio Operativo: Celery & Redis

Trasforma l'app in un software di livello professionale:

    Celery: Gestisce le code di lavoro, permettendo all'AI di lavorare senza bloccare la navigazione dell'utente.

    Redis: Funge da "ufficio postale" (Message Broker) che smista i compiti tra Django e i Worker.

4. Il Volto: Tailwind CSS & HTMX

    Tailwind CSS: Fornisce un design moderno, scuro e professionale con un sistema a card intuitivo.

    HTMX: Permette aggiornamenti dinamici della UI (come l'attivazione dei toggle o il trigger dell'analisi) inviando richieste parziali al server.

⚙️ Installazione e Setup

    Clonazione:
    Bash

git clone <tuo-link-github>
cd sentinel_api

Ambiente Virtuale:
Bash

python -m venv venv
source venv/bin/activate

Dipendenze:
Bash

pip install -r requirements.txt

Configurazione: Crea un file .env con le tue credenziali:
Snippet di codice

OPENAI_API_KEY=la_tua_chiave_qui
SECRET_KEY=tua_secret_key

Database:
Bash

    python manage.py migrate
    python manage.py createsuperuser

🔄 Workflow & Daily Routine
Avvio dei Servizi

Per far funzionare SentinelAPI sono necessari tre terminali attivi:

    Terminale A (Web Server): python manage.py runserver

    Terminale B (Celery Worker): celery -A core worker --loglevel=info

    Terminale C (Celery Beat): celery -A core beat --loglevel=info (Gestisce la ronda automatica ogni 5 minuti).

Flusso di Lavoro

    Aggiunta Target: Inserisci l'URL di uno Swagger/OpenAPI JSON nell'Admin Panel.

    Monitoraggio:

        Manuale: Clicca "Analizza Ora" per un controllo istantaneo via HTMX.

        Automatico: Se il toggle è su ON, Celery Beat avvia il controllo ciclicamente.

    Confronto AI: Il sistema scarica la documentazione live, la confronta con quella salvata nel database e genera un report dettagliato tramite GPT-4o.