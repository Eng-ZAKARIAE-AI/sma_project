import os
import logging
from typing import List, Dict
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from ..state import AgentState

# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration de l'LLM
# Utilisation du slug complet pour OpenRouter et réduction de max_tokens au cas où
llm = ChatOpenAI(
    model="openai/gpt-4o", 
    temperature=0,
    max_tokens=256,
    base_url="https://openrouter.ai/api/v1"
)

SYSTEM_PROMPT = """
Tu es un agent de diagnostic clinique. 
Ton rôle est de poser des questions pertinentes au patient pour comprendre ses symptômes.
Tu dois poser un maximum de 5 questions au total (une par tour).
Si tu as assez d'informations pour une synthèse initiale, indique-le.
Sois empathique et professionnel."""

def diagnostic_node(state: AgentState):
    messages = state.get("messages", [])
    
    try:
        # Construction du prompt avec l'historique
        logger.info(f"Appel LLM avec {len(messages)} messages")
        response = llm.invoke([SystemMessage(content=SYSTEM_PROMPT)] + messages)
        
        # Mise à jour du compteur d'itérations si nécessaire
        count = state.get("iteration_count", 0) + 1
        
        return {
            "messages": [response],
            "iteration_count": count
        }
    except Exception as e:
        logger.error(f"Erreur dans diagnostic_node: {e}")
        # On relance l'exception pour que FastAPI la capture (500)
        # Mais au moins on aura le log
        raise e
