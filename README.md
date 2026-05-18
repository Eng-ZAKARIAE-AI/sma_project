# Agentic Clinical Orchestrator

## Description
Solution d'orientation clinique multi-agents basée sur LangGraph.

## Installation
1. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
2. Configurez votre fichier `.env` avec votre clé API (OpenRouter par défaut).

## Utilisation

### Lancer le Backend
Depuis la racine du projet :
```bash
python -m backend.app.api
```
Le backend sera disponible sur `http://localhost:8000`. Vous pouvez changer le port avec la variable d'environnement `PORT`.

### Lancer le Frontend (Streamlit)
Depuis la racine du projet :
```bash
streamlit run frontend/app.py
```
### Lancer les deux
python -m run_all.py

## Structure du projet
- `backend/` : Logique LangGraph et API FastAPI.
- `frontend/` : Interface utilisateur Streamlit.
- `mcp_server/` : Serveur Model Context Protocol (en option).