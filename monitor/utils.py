import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_changes_with_ai(old_doc, new_doc):
    prompt = f"""
    Sei un esperto DevOps. Confronta queste due versioni di una documentazione API.
    Individua solo i 'Breaking Changes'.
    VECCHIA DOC: {old_doc[:2000]}
    NUOVA DOC: {new_doc[:2000]}
    Rispondi in italiano con un elenco puntato.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Errore AI: {str(e)}"

def check_api_update(target_api):
    print(f"\n--- TEST CONNESSIONE PER: {target_api.name} ---")
    print(f"URL utilizzata: {target_api.swagger_url}")

    try:
        response = requests.get(target_api.swagger_url, timeout=10)
        target_api.last_status = response.status_code

        if response.status_code == 200:
            print("SUCCESS: Pagina trovata!")
            new_content = response.text

            if target_api.last_content and target_api.last_content != new_content:
                print("CAMBIAMENTO RILEVATO: Chiamo OpenAI...")
                analysis = analyze_changes_with_ai(target_api.last_content, new_content)
                target_api.last_analysis = analysis
            else:
                print("INFO: Nessun cambiamento nel contenuto.")

            target_api.last_content = new_content
            target_api.save()
            return True
        else:
            print(f"ERRORE: Il server ha risposto con {response.status_code} (Non Trovato)")
            target_api.save()

    except Exception as e:
        print(f"ERRORE DI CONNESSIONE: {e}")
        target_api.last_status = 500
        target_api.save()

    return False