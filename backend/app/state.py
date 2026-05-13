from typing import Annotated, TypedDict, List
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    patient_info: dict
    clinical_synthesis: str
    physician_feedback: str
    iteration_count: int
    final_report: str