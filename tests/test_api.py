import os
import requests
import json
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BACKEND_URL = "http://localhost:8000/chat"

def test_api_key_validity():
    """
    Teste si la clé API est valide en appelant directement OpenRouter.
    Cela permet de s'assurer que le problème ne vient pas du backend.
    """
    print("\n--- Test de validité de la clé API (Direct OpenRouter) ---")
    if not OPENAI_API_KEY:
        print("❌ Erreur : OPENAI_API_KEY non trouvée dans le fichier .env")
        return False
    
    # On utilise OpenRouter comme configuré dans le backend
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-4o",
        "messages": [{"role": "user", "content": "Hello, respond with only 'OK'"}],
        "max_tokens": 10
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            content = response.json()['choices'][0]['message']['content']
            print(f"✅ Clé API valide ! Réponse : {content}")
            return True
        else:
            print(f"❌ Clé API invalide ou erreur OpenRouter : {response.status_code}")
            print(f"Détails : {response.text}")
            return False
    except Exception as e:
        print(f"❌ Erreur lors de l'appel direct à l'API : {e}")
        return False

def test_backend_chat():
    """
    Teste l'endpoint /chat du backend pour vérifier l'intégration complète.
    """
    print("\n--- Test de l'endpoint Backend (/chat) ---")
    payload = {
        "message": "Bonjour, j'ai mal à la tête depuis ce matin.",
        "thread_id": "test_user"
    }
    
    try:
        response = requests.post(BACKEND_URL, json=payload, timeout=30)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"✅ Réponse du backend : {response.json().get('response')}")
        else:
            print(f"❌ Erreur backend : {response.text}")
    except Exception as e:
        print(f"❌ Impossible de se connecter au backend à {BACKEND_URL}")
        print("   Assurez-vous que le backend est lancé (ex: python -m backend.app.api)")

if __name__ == "__main__":
    # 1. Vérifier la clé API d'abord
    is_key_valid = test_api_key_validity()
    
    # 2. Si la clé est valide, tester le backend
    if is_key_valid:
        test_backend_chat()
    else:
        print("\n⚠️ Le test du backend est ignoré car la clé API semble invalide.")
