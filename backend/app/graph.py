from langgraph.graph import StateGraph, END
from .state import AgentState

# Initialisation du workflow
workflow = StateGraph(AgentState)
# Ajoutez vos noeuds ici