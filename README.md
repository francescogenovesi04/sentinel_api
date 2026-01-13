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

## Come funziona Sentinel?

    Ogni volta che aggiungi un'API, il database crea una nuova riga nel modello TargetAPI.

    Da quel momento:

    Il Worker sa che deve scaricare quel file.

    L'AI sa che deve confrontare ogni nuova versione con quella precedentemente salvata nel campo last_content.

    Il Beat (l'orologio) aggiunge quell'API al giro di ronda ogni 5 minuti, a patto che il toggle sia su ON.

1. Il Cuore: Django (Python)

È il framework principale che tiene insieme tutto.

    Perché Django? È solido, "batteries-included" e gestisce la sicurezza e il database (SQLite in questo caso) in modo professionale.

    Il Ruolo: Gestisce l'Admin, salva le versioni delle API e coordina le chiamate verso OpenAI e il frontend.

2. Il Cervello: OpenAI API (GPT-4o)

Non è una semplice ricerca di testo, ma un'analisi semantica.

    La Tecnologia: Usiamo il modello GPT-4o (o 4o-mini) per leggere due file JSON e capire "cosa significa" il cambiamento.

    Il Vantaggio: Mentre un software normale ti direbbe solo "la riga 10 è cambiata", l'AI ti spiega: "Attenzione, hanno rimosso il parametro della chiave API, il tuo codice si romperà".

3. Il Braccio Operativo: Celery & Redis

Questa è la parte che trasforma un sito in un software "pro".

    Celery: È il gestore dei compiti in background. Grazie a lui, l'analisi pesante dell'AI non blocca il sito; il sito rimane veloce mentre Celery lavora "dietro le quinte".

    Redis: Funziona da "ufficio postale" (Message Broker). Django imbuca i messaggi in Redis e Celery li passa a ritirare per eseguirli.

4. Il Volto: Tailwind CSS & HTMX

Qui hai evitato di scrivere migliaia di righe di JavaScript complicato (come React o Vue).

    Tailwind CSS: Ti ha permesso di creare quel design scuro e moderno usando solo classi pronte, senza scrivere CSS da zero.

    HTMX: È la vera magia. Ti permette di aggiornare le card o cambiare il toggle (Auto ON/OFF) senza ricaricare mai la pagina. Invia una richiesta al server e sostituisce solo il pezzetto di HTML necessario.

    1. La Scintilla (Chi attiva il flow)

## work flow

    Il processo può iniziare in due modi:

    Manualmente: Tu clicchi il tasto "Analizza Ora" sulla Dashboard; HTMX invia una richiesta al server senza ricaricare la pagina.

    Automaticamente: Celery Beat (l'orologio) controlla ogni 5 minuti quali API hanno il toggle su "Auto: ON" e invia un comando al Worker.

2. Il Recupero dei Dati (Il ruolo di Django e lo Scraper)

    Django (tramite il Celery Worker) recupera dal database la "VECCHIA DOC" (salvata nel campo last_content).

    Contemporaneamente, il sistema effettua uno scraping in tempo reale dell'URL Swagger per scaricare la "NUOVA DOC" (il JSON attuale dell'API).

3. Il Confronto (Il "Chi" e il "Come")

Qui entra in gioco il vero cervello del sistema: OpenAI GPT-4o.

    Il Worker invia entrambi i JSON (vecchio e nuovo) alle API di OpenAI.

    L'AI non si limita a vedere se le virgole sono cambiate, ma esegue un'analisi semantica.

    GPT-4o agisce come un esperto programmatore: legge le differenze e decide quali sono "Breaking Changes" (modifiche critiche) e quali sono trascurabili.

4. L'Aggiornamento Finale

    Il Report: L'AI restituisce una spiegazione testuale dei cambiamenti.

    Salvataggio: Django salva il nuovo report nel campo last_analysis e sovrascrive last_content con il nuovo JSON (che diventerà il "passato" per il prossimo controllo).

    Visualizzazione: Se il controllo è manuale, HTMX aggiorna istantaneamente la card sulla Dashboard mostrandoti il risultato.
