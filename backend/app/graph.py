from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from .state import AgentState
from .nodes.diagnostic_agent import diagnostic_node
from .nodes.supervisor import supervisor_node, route_next

# Initialisation de la mémoire
memory = MemorySaver()

# Initialisation du workflow
workflow = StateGraph(AgentState)

# Ajout des noeuds
workflow.add_node("diagnostic_agent", diagnostic_node)
workflow.add_node("supervisor", supervisor_node)

# Définition des arêtes
workflow.set_entry_point("supervisor")

workflow.add_edge("diagnostic_agent", END)

workflow.add_conditional_edges(
    "supervisor",
    route_next,
    {
        "diagnostic_agent": "diagnostic_agent",
        "__end__": END
    }
)

# Compilation du graphe avec mémoire
app_graph = workflow.compile(checkpointer=memory)
