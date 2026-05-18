import streamlit as st
import requests
import uuid
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="Agentic Clinical Orchestrator", layout="centered")

st.title("🏥 Clinical Orchestrator")
st.markdown("---")

# Initialisation de l'ID de session pour le backend
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

st.sidebar.title("Paramètres")

if st.sidebar.button("Nouvelle session"):
    st.session_state.thread_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.rerun()

# Entrée utilisateur
if prompt := st.chat_input("Décrivez vos symptômes..."):
    # Ajouter le message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Appel au backend
    try:
        with st.spinner("L'agent réfléchit..."):
            response = requests.post(
                f"{BACKEND_URL}/chat",
                json={"message": prompt, "thread_id": st.session_state.thread_id}
            )
            response.raise_for_status()
            data = response.json()
            
            ai_content = data["response"]
            
            # Ajouter le message AI
            st.session_state.messages.append({"role": "assistant", "content": ai_content})
            with st.chat_message("assistant"):
                st.markdown(ai_content)
    except Exception as e:
        st.error(f"Erreur de connexion au backend : {e}")
        st.info("💡 **Conseil :** Assurez-vous que le backend est lancé. Vous pouvez utiliser `python run_all.py` pour lancer le backend et le frontend simultanément.")
