from typing import Literal, Dict
from ..state import AgentState

def supervisor_node(state: AgentState) -> Dict:
    """
    Le superviseur observe l'état actuel et prépare la suite.
    Ici, il pourrait formater des données ou analyser si le patient est fatigué.
    """
    return {}

def route_next(state: AgentState) -> Literal["diagnostic_agent", "__end__"]:
    count = state.get("iteration_count", 0)
    if count >= 5:
        return "__end__"
    return "diagnostic_agent"
